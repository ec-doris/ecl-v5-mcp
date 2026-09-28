"""Command-line entry point: ``uv run ecl-v5-mcp-http``."""

from __future__ import annotations

import argparse
import os
from pathlib import Path

import uvicorn

from ecl_v5_mcp.content import DEFAULT_CONTENT_DIR, Content
from ecl_v5_mcp.server import create_app, create_server


def main() -> None:
    parser = argparse.ArgumentParser(
        description="ECL v5 MCP server (FastMCP). Serves MCP over streamable "
        "HTTP at /mcp, plus /health, /assets and /fonts."
    )
    parser.add_argument(
        "--transport",
        choices=["http", "stdio"],
        default=os.environ.get("MCP_TRANSPORT", "http"),
        help="Transport to use (default: http; env MCP_TRANSPORT)",
    )
    parser.add_argument(
        "--host",
        default=os.environ.get("HOST", "127.0.0.1"),
        help="Bind address (default: 127.0.0.1; env HOST)",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=int(os.environ.get("PORT", "8000")),
        help="Bind port (default: 8000; env PORT)",
    )
    parser.add_argument(
        "--public-base-url",
        default=os.environ.get("PUBLIC_BASE_URL"),
        help="Externally reachable base URL used in guides for /assets and "
        "/fonts (default: http://HOST:PORT; env PUBLIC_BASE_URL)",
    )
    parser.add_argument(
        "--content-dir",
        type=Path,
        default=Path(os.environ.get("ECL_CONTENT_DIR", DEFAULT_CONTENT_DIR)),
        help="Directory containing components/, guides/, skills/, assets/, "
        "fonts/ and starter-template.html (default: repository root; env "
        "ECL_CONTENT_DIR)",
    )
    args = parser.parse_args()
    root = args.content_dir.resolve()

    if args.transport == "stdio":
        # Same behaviour as index.js: guides point at the local checkout.
        create_server(Content(root, str(root))).run("stdio", show_banner=False)
        return

    base_url = (args.public_base_url or f"http://{args.host}:{args.port}").rstrip("/")
    uvicorn.run(create_app(Content(root, base_url)), host=args.host, port=args.port)


if __name__ == "__main__":
    main()
