# ECL v5 MCP Server

A Node.js MCP server that provides European Commission (EC) Europa Component
Library examples, Twig templates, starter markup, v5.3.1 assets and focused
implementation guides. Content is read from this checkout on every MCP request,
so guide and example edits are visible without rebuilding the server.

The ECL content target is v5.3.1 at commit
`0b3ca5a9190e1c32ff00fc092380e3a8f3571a05`; the MCP package version is
independent. This repository is updated incrementally. See
[update-status.md](update-status.md) for audited rows and
[previous-sessions.md](previous-sessions.md) for the handoff history.

## Installation

1. Install dependencies:
```bash
npm install github:ec-doris/ecl-v5-mcp
```

## Running the Server

To run the server using stdio transport:
```bash
node node_modules/ecl-v5-mcp/index.js
```

This server is designed to be used with MCP clients that communicate via stdio.
It registers six tools: `guide`, `guide_list`, `components_list`, `component`,
`component_template` and `starter_template`.

Configure the client to connect to this server for MCP tool calls.

### VS Code .vscode/mcp.json Example
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

## Working with the content

Call `guide_list` and `components_list` first. Use `component` for rendered HTML
examples, `component_template` for the exact available EC Twig family, and
`starter_template` for a complete page shell. The guides cover the v5.3.1
assets, utilities, colours, icons, branding, images and runtime setup.

The `europa-component-library` symlink is a separate upstream checkout used for
tagged-source comparison during maintenance. It is not a runtime dependency
and is not copied into the published package. The active MCP contract is EC
only; legacy EU files retained for traceability are not advertised.

For the supported page setup, copy the `assets/` and `fonts/` directories as
siblings, load the dependencies described by `guide("assets")`, and initialize
the supplied ECL bundle with `ECL.autoInit()` after the page markup.
