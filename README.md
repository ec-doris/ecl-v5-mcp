# ECL v5 MCP Server

An MCP server that provides European Commission (EC) Europa Component Library
examples, Twig templates, starter markup, v5.3.1 assets and focused
implementation guides. Content is read from this checkout on every MCP request,
so guide and example edits are visible without rebuilding the server.

The ECL content target is v5.3.1 at commit
`0b3ca5a9190e1c32ff00fc092380e3a8f3571a05`; the MCP package version is
independent.

## Two servers, one content source

This repository ships two interchangeable implementations of the same MCP
server. Both read the same `components/`, `guides/`, `skills/`, `assets/`,
`fonts/` and `starter-template.html`, and expose identical tools and resources.

| Variant | Transport | Entry point | Install |
|---|---|---|---|
| Node.js | stdio | `index.js` | `npm` |
| Python ([FastMCP](https://gofastmcp.com)) | Streamable HTTP | `src/ecl_v5_mcp/` | `uv`, from a checkout or Docker |

Use the Node variant for a local MCP client that launches the server itself.
Use the Python variant to run the server once and let clients connect over the
network.

## Stdio server (Node.js)

### Installation

```bash
npm install github:ec-doris/ecl-v5-mcp
```

The npm package contains only the Node server and the content; the Python
files are excluded through `files` in `package.json`.

### Running

```bash
node node_modules/ecl-v5-mcp/index.js
```

### VS Code .vscode/mcp.json example

```json
{
    "servers": {
        "ecl": {
            "type": "stdio",
            "command": "node",
            "args": [
                "/Users/xxx/ecl-v5-mcp/index.js"
            ]
        }
    }
}
```

Be sure to use the full path of the `index.js` file.

## HTTP server (Python / FastMCP)

### Running from a checkout

Requires [uv](https://docs.astral.sh/uv/) and Python 3.12+.

```bash
git clone https://github.com/ec-doris/ecl-v5-mcp.git
cd ecl-v5-mcp
uv sync
uv run ecl-v5-mcp-http
```

The server listens on `http://127.0.0.1:8000` and provides:

| Path | Purpose |
|---|---|
| `/mcp` | MCP endpoint (streamable HTTP, stateless) |
| `/health` | Health check, returns `{"status": "ok"}` |
| `/assets/…` | The ECL CSS, JavaScript, favicons and logos |
| `/fonts/…` | The Inter font files |

`/assets` and `/fonts` are served as siblings, so the stylesheets' relative
`../fonts/…` URLs resolve. The `assets` guide uses the public base URL in place
of a local path, so agents download the assets from the server instead of
copying them from disk.

### Configuration

Each setting can be passed as a command-line flag or environment variable
(`uv run ecl-v5-mcp-http --help`):

| Flag | Environment variable | Default | Description |
|---|---|---|---|
| `--host` | `HOST` | `127.0.0.1` | Bind address |
| `--port` | `PORT` | `8000` | Bind port |
| `--public-base-url` | `PUBLIC_BASE_URL` | `http://HOST:PORT` | Externally reachable URL used in guides for `/assets` and `/fonts`. Set this behind a proxy or in Docker. |
| `--content-dir` | `ECL_CONTENT_DIR` | repository root | Directory containing the content folders |
| `--transport` | `MCP_TRANSPORT` | `http` | `http`, or `stdio` for local testing |

The server has no authentication. Bind it to `127.0.0.1` (the default) or put
it behind a network boundary or reverse proxy that you control.

### Docker

```bash
docker build -t ecl-v5-mcp-http .
docker run --rm -p 8000:8000 \
    -e PUBLIC_BASE_URL=http://localhost:8000 \
    ecl-v5-mcp-http
```

The image contains only the Python server and the content, runs as a non-root
user, and binds to `0.0.0.0:8000`.

### VS Code .vscode/mcp.json example

```json
{
    "servers": {
        "ecl": {
            "type": "http",
            "url": "http://localhost:8000/mcp"
        }
    }
}
```

## Tools and resources

Both servers register eight tools: `guide`, `guide_list`, `components_list`,
`component`, `component_template`, `starter_template`, `skill_list` and
`skill_get`. They also expose the same read-only content as MCP resources for
clients that support `resources/list` and `resources/read`:

- `ecl://skill/ecl-component-development`
- `ecl://starter-template`
- `ecl://guide/{topic}`
- `ecl://component/{id}/html`
- `ecl://component/{id}/twig/{filename}`

Tools remain available for clients without MCP resource support.

## Working with the content

Call `skill_list` and `skill_get` when the consuming agent needs the reusable ECL
implementation workflow. Then call `guide_list` and `components_list` first.
Use `component` for rendered HTML examples, `component_template` for the exact
available EC Twig family, and `starter_template` for a complete page shell. The
guides cover the v5.3.1 assets, utilities, colours, icons, branding, images and
runtime setup.

The ECL skill is intended to be incorporated into the consuming project's own
agent skills directory. It instructs an agent to build reusable local ECL
components from the server's HTML and Twig foundations; it does not ask the
agent to copy the MCP repository's component catalogue into the application.

The `europa-component-library` symlink is a separate upstream checkout used for
tagged-source comparison during maintenance. It is not a runtime dependency
and is not copied into the published package. The active MCP contract is EC
only; legacy EU files retained for traceability are not advertised.

For the supported page setup, copy the `assets/` and `fonts/` directories as
siblings (or download them from the HTTP server), load the dependencies
described by `guide("assets")`, and initialize the supplied ECL bundle with
`ECL.autoInit()` after the page markup.

## Development

Content changes (guides, components, skills, assets) need no code changes: both
servers pick them up automatically.

Tool or resource behaviour is implemented twice, in `index.js` and in
`src/ecl_v5_mcp/`. When you change one, change the other in the same way. In
particular, `templateFamilies` in `index.js` and `TEMPLATE_FAMILIES` in
`src/ecl_v5_mcp/content.py` must stay identical.

`tests/test_parity.py` starts `node index.js` and checks that the Python server
returns byte-identical tool results, error messages, resource listings and
resource contents. It is skipped when Node or `node_modules` is missing.

```bash
npm ci                 # needed for the parity tests
uv run pytest          # unit, HTTP and parity tests
uv run ruff check
uv run ruff format
npx prettier --check index.js
```
