"""FastMCP server exposing the same tools and resources as ``index.js``."""

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

from fastmcp import FastMCP
from fastmcp.exceptions import ResourceError, ToolError
from fastmcp.resources import Resource
from fastmcp.resources.base import ResourceContent, ResourceResult
from fastmcp.tools.base import ToolResult
from mcp.types import TextContent
from pydantic import Field
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from starlette.routing import Mount
from starlette.staticfiles import StaticFiles

from ecl_v5_mcp.content import Content, ContentError, encode_uri_component, to_json

SERVER_NAME = "ecl-v5-server"
SERVER_VERSION = "5.3.1"
INSTRUCTIONS = (
    "For ECL implementation work, use skill_get for the reusable local-component "
    "workflow, then use guide_list and components_list as the live ECL inventory. "
    "The server supplies read-only HTML, Twig, starter-template, guide, and skill "
    "content; adapt it into the consuming project rather than copying the "
    "catalogue wholesale."
)


class LiveFileResource(Resource):
    """A text resource re-read from disk on every request, like index.js."""

    path: Path = Field(description="Absolute path of the backing file")
    dir_placeholder: str | None = Field(
        default=None,
        exclude=True,
        description="If set, replace __DIR__ with this value (guides only)",
    )

    async def read(self) -> ResourceResult:
        try:
            text = self.path.read_text(encoding="utf-8")
            if self.dir_placeholder is not None:
                text = text.replace("__DIR__", self.dir_placeholder)
        except OSError as error:
            raise ResourceError(f"Failed to read resource {self.uri}") from error
        return ResourceResult(
            contents=[ResourceContent(content=text, mime_type=self.mime_type)]
        )


def _text(text: str) -> ToolResult:
    return ToolResult(content=[TextContent(type="text", text=text)])


def _run(fn: Callable[[], str]) -> ToolResult:
    try:
        return _text(fn())
    except ContentError as error:
        raise ToolError(str(error)) from error


def create_server(content: Content) -> FastMCP:
    """Build a FastMCP server over ``content``."""
    mcp = FastMCP(
        SERVER_NAME,
        instructions=INSTRUCTIONS,
        version=SERVER_VERSION,
        mask_error_details=False,
    )

    # Tools ----------------------------------------------------------------
    # output_schema=None keeps results as plain text content, matching Node.

    @mcp.tool(
        description="Get the content of a guide markdown file", output_schema=None
    )
    def guide(topic: str = Field(description="The topic of the guide")) -> ToolResult:
        return _run(lambda: content.guide(topic))

    @mcp.tool(
        description="List reusable AI agent skills provided by this ECL MCP server",
        output_schema=None,
    )
    def skill_list() -> ToolResult:
        return _run(lambda: to_json(content.skill_list()))

    @mcp.tool(
        description="Get the complete SKILL.md content for an ECL implementation skill",
        output_schema=None,
    )
    def skill_get(
        id: str = Field(description="The skill ID returned by skill_list"),
    ) -> ToolResult:
        return _run(lambda: content.skill(id))

    @mcp.tool(description="List all available guides with snippets", output_schema=None)
    def guide_list() -> ToolResult:
        return _run(lambda: to_json(content.guide_list()))

    @mcp.tool(
        description="List all available components with their IDs and call information",
        output_schema=None,
    )
    def components_list() -> ToolResult:
        return _run(lambda: to_json(content.components_list()))

    @mcp.tool(
        description="Get the HTML content of a component by its ID", output_schema=None
    )
    def component(
        id: str = Field(description="The ID of the component"),
    ) -> ToolResult:
        return _run(lambda: content.component(id))

    @mcp.tool(description="Get the starter template HTML content", output_schema=None)
    def starter_template() -> ToolResult:
        return _run(content.starter_template)

    @mcp.tool(
        description="Get the Twig template(s) for a component by its ID",
        output_schema=None,
    )
    def component_template(
        id: str = Field(description="The ID of the component"),
    ) -> ToolResult:
        return _run(lambda: to_json(content.component_template(id)))

    # Resources ------------------------------------------------------------
    # Concrete (non-template) resources so they appear in resources/list,
    # exactly as registered by index.js.

    def add(
        name: str,
        uri: str,
        path: Path,
        mime_type: str,
        description: str,
        dir_placeholder: str | None = None,
    ) -> None:
        mcp.add_resource(
            LiveFileResource(
                uri=uri,
                name=name,
                path=path.resolve(),
                mime_type=mime_type,
                description=description,
                dir_placeholder=dir_placeholder,
            )
        )

    add(
        "starter-template",
        "ecl://starter-template",
        content.starter_template_path,
        "text/html",
        "Complete ECL EC starter page template",
    )

    for file in sorted(content.guide_files()):
        topic = file.replace(".md", "", 1)
        add(
            f"guide-{topic}",
            f"ecl://guide/{encode_uri_component(topic)}",
            content.guides_dir / file,
            "text/markdown",
            f"ECL implementation guide: {topic}",
            content.dir_placeholder,
        )

    files = content.component_files()
    for component_id in sorted(content.component_ids()):
        encoded_id = encode_uri_component(component_id)
        add(
            f"component-{component_id}-html",
            f"ecl://component/{encoded_id}/html",
            content.components_dir / f"{component_id}.html",
            "text/html",
            f"Rendered ECL HTML examples for component: {component_id}",
        )
        for file in content.template_files(component_id, files):
            add(
                f"component-{component_id}-twig-{file}",
                f"ecl://component/{encoded_id}/twig/{encode_uri_component(file)}",
                content.components_dir / file,
                "text/plain",
                f"ECL Twig template for component {component_id}: {file}",
            )

    for skill in content.skill_list():
        add(
            f"skill-{skill['id']}",
            f"ecl://skill/{encode_uri_component(skill['id'])}",
            content.skills_dir / skill["id"] / skill["file"],
            "text/markdown",
            f"Reusable AI agent skill: {skill['name']}",
        )

    # HTTP-only routes -----------------------------------------------------

    @mcp.custom_route("/health", methods=["GET"], include_in_schema=False)
    async def health(_: Request) -> Response:
        return JSONResponse({"status": "ok"})

    return mcp


def create_app(content: Content, path: str = "/mcp") -> Starlette:
    """ASGI app: MCP at ``path``, plus /health, /assets and /fonts.

    ``assets/`` and ``fonts/`` are mounted as siblings so the CSS's relative
    ``../fonts/...`` URLs resolve for pages loading the served stylesheets.
    """
    app = create_server(content).http_app(path=path, stateless_http=True)
    for directory in ("assets", "fonts"):
        app.router.routes.append(
            Mount(
                f"/{directory}",
                app=StaticFiles(directory=content.root / directory),
                name=directory,
            )
        )
    return app
