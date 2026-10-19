from __future__ import annotations

import pytest
from fastmcp import Client

from ecl_v5_mcp.content import DEFAULT_CONTENT_DIR, Content
from ecl_v5_mcp.server import create_server

ROOT = DEFAULT_CONTENT_DIR
PLACEHOLDER = "https://ecl.example.test"


@pytest.fixture
def content() -> Content:
    return Content(ROOT, PLACEHOLDER)


@pytest.fixture
async def client(content: Content):
    async with Client(create_server(content)) as connected:
        yield connected
