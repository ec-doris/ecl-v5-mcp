# syntax=docker/dockerfile:1

# HTTP (FastMCP) variant of the ECL v5 MCP server.
# The Node stdio server (index.js) is not included in this image.

FROM astral/uv:0.12.15-debian AS uv

# ---- builder ----
FROM python:3.12-slim-bookworm AS builder
COPY --from=uv /usr/local/bin/uv /usr/local/bin/uv
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy UV_PYTHON_DOWNLOADS=0 UV_NO_DEV=1
WORKDIR /app
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project
COPY pyproject.toml uv.lock README.md ./
COPY src ./src
RUN --mount=type=cache,target=/root/.cache/uv uv sync --frozen --no-editable

# ---- runtime ----
FROM python:3.12-slim-bookworm AS runtime
RUN useradd --create-home --uid 10001 app
WORKDIR /app
COPY --from=builder --chown=app:app /app/.venv /app/.venv
COPY --chown=app:app components ./components
COPY --chown=app:app guides ./guides
COPY --chown=app:app skills ./skills
COPY --chown=app:app assets ./assets
COPY --chown=app:app fonts ./fonts
COPY --chown=app:app starter-template.html ./
ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    ECL_CONTENT_DIR=/app \
    HOST=0.0.0.0 \
    PORT=8000
USER app
EXPOSE 8000
HEALTHCHECK CMD ["python", "-c", "import os, urllib.request; urllib.request.urlopen(f'http://127.0.0.1:{os.environ[\"PORT\"]}/health')"]
CMD ["ecl-v5-mcp-http"]
