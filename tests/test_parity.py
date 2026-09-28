"""Check that the Python server matches the Node stdio server (index.js).

Starts ``node index.js`` over stdio and compares tool metadata, tool output,
error messages, resource listings and resource contents. Skipped when Node or
``node_modules`` is unavailable (run ``npm ci`` first).
"""

from __future__ import annotations

import shutil
from pathlib import Path

import pytest
from fastmcp import Client
from fastmcp.client.transports import StdioTransport

from ecl_v5_mcp.content import Content
from ecl_v5_mcp.server import create_server

from .conftest import ROOT

pytestmark = pytest.mark.skipif(
    shutil.which("node") is None
    or not (ROOT / "node_modules" / "@modelcontextprotocol" / "sdk").is_dir(),
    reason="node and node_modules are required (run `npm ci`)",
)


@pytest.fixture
async def clients():
    node = Client(StdioTransport("node", [str(ROOT / "index.js")], cwd=str(ROOT)))
    # Node replaces __DIR__ with its own directory; use the same value.
    python = Client(create_server(Content(ROOT, str(Path(ROOT)))))
    async with node, python:
        yield node, python


def _dump(result) -> tuple:
    return (
        bool(result.is_error),
        [(block.type, block.text) for block in result.content],
    )


def _tool_key(tool) -> tuple:
    schema = tool.input_schema
    return (
        tool.name,
        tool.description,
        sorted(schema.get("properties", {}).items()),
        sorted(schema.get("required", [])),
    )


async def test_server_info_matches(clients):
    node, python = clients
    for field in ("name", "version"):
        assert getattr(python.server_info, field) == getattr(node.server_info, field)
    assert python.instructions == node.instructions


async def test_tools_match(clients):
    node, python = clients
    node_tools = sorted(map(_tool_key, await node.list_tools()))
    python_tools = sorted(map(_tool_key, await python.list_tools()))
    assert python_tools == node_tools


def _calls(content: Content) -> list[tuple[str, dict]]:
    calls: list[tuple[str, dict]] = [
        ("guide_list", {}),
        ("components_list", {}),
        ("starter_template", {}),
        ("skill_list", {}),
        ("skill_get", {"id": "ecl-component-development"}),
        ("skill_get", {"id": "missing"}),
        ("guide", {"topic": "missing"}),
        ("guide", {"topic": "../README"}),
        ("component", {"id": "missing"}),
        ("component", {"id": "../starter-template"}),
        ("component_template", {"id": "missing"}),
    ]
    calls += [
        ("guide", {"topic": file.removesuffix(".md")}) for file in content.guide_files()
    ]
    for component_id in content.component_ids():
        calls.append(("component", {"id": component_id}))
        calls.append(("component_template", {"id": component_id}))
    return calls


async def test_tool_results_match(clients):
    node, python = clients
    for name, args in _calls(Content(ROOT, str(ROOT))):
        expected = _dump(await node.call_tool(name, args, raise_on_error=False))
        actual = _dump(await python.call_tool(name, args, raise_on_error=False))
        assert actual == expected, f"{name}({args}) differs"


async def test_resources_match(clients):
    node, python = clients

    def key(resource) -> tuple:
        return (
            str(resource.uri),
            resource.name,
            resource.mime_type,
            resource.description,
        )

    node_resources = sorted(map(key, await node.list_resources()))
    python_resources = sorted(map(key, await python.list_resources()))
    assert python_resources == node_resources

    for uri, *_ in node_resources:
        expected = [c.text for c in await node.read_resource(uri)]
        actual = [c.text for c in await python.read_resource(uri)]
        assert actual == expected, f"{uri} differs"
