from __future__ import annotations

import json

import pytest
from starlette.testclient import TestClient

from ecl_v5_mcp.content import Content
from ecl_v5_mcp.server import create_app

from .conftest import PLACEHOLDER, ROOT

EXPECTED_TOOLS = {
    "guide",
    "guide_list",
    "components_list",
    "component",
    "component_template",
    "starter_template",
    "skill_list",
    "skill_get",
}


def text(result) -> str:
    return result.content[0].text


async def test_lists_all_tools(client):
    tools = await client.list_tools()
    assert {tool.name for tool in tools} == EXPECTED_TOOLS


async def test_guide_replaces_dir_placeholder(client):
    body = text(await client.call_tool("guide", {"topic": "assets"}))
    assert f"{PLACEHOLDER}/assets/*" in body
    assert "__DIR__" not in body


@pytest.mark.parametrize(
    ("tool", "args"),
    [
        ("guide", {"topic": "../README"}),
        ("guide", {"topic": "missing"}),
        ("component", {"id": "../starter-template"}),
        ("component", {"id": "missing"}),
        ("component_template", {"id": "missing"}),
        ("skill_get", {"id": "missing"}),
    ],
)
async def test_unknown_or_traversal_inputs_are_errors(client, tool, args):
    result = await client.call_tool(tool, args, raise_on_error=False)
    assert result.is_error
    assert "not found" in text(result) or "No templates" in text(result)


async def test_component_template_uses_family(client):
    templates = json.loads(
        text(await client.call_tool("component_template", {"id": "file"}))
    )
    assert list(templates) == ["file.html.twig"]


async def test_components_list_includes_template_call(client):
    components = json.loads(text(await client.call_tool("components_list", {})))
    accordion = next(c for c in components if c["id"] == "accordion")
    assert accordion["template_call"]["tool"] == "component_template"


async def test_resources_are_listed_and_readable(client):
    uris = {str(resource.uri) for resource in await client.list_resources()}
    assert "ecl://starter-template" in uris
    assert "ecl://guide/assets" in uris
    assert "ecl://component/accordion/html" in uris
    assert "ecl://skill/ecl-component-development" in uris

    guide = await client.read_resource("ecl://guide/assets")
    assert f"{PLACEHOLDER}/fonts/*" in guide[0].text


def test_http_routes():
    app = create_app(Content(ROOT, PLACEHOLDER))
    with TestClient(app) as http:
        assert http.get("/health").json() == {"status": "ok"}

        css = http.get("/assets/ecl-ec.css")
        assert css.status_code == 200
        assert css.headers["content-type"].startswith("text/css")

        assert http.get("/fonts/InterVariable.woff2").status_code == 200
        assert http.get("/assets/../README.md").status_code == 404
