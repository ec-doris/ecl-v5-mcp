# ECL v5 MCP Server

A Node.js MCP server that provides European Commission (EC) Europa Component
Library examples, Twig templates, starter markup, v5.3.1 assets and focused
implementation guides. Content is read from this checkout on every MCP request,
so guide and example edits are visible without rebuilding the server.

The ECL content target is v5.3.1 at commit
`0b3ca5a9190e1c32ff00fc092380e3a8f3571a05`; the MCP package version is
independent.

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
It registers eight tools: `guide`, `guide_list`, `components_list`, `component`,
`component_template`, `starter_template`, `skill_list` and `skill_get`.
It also exposes the same read-only content as MCP resources for clients that
support `resources/list` and `resources/read`.

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

When supported by the MCP client, read-only resources are available at:

- `ecl://skill/ecl-component-development`
- `ecl://starter-template`
- `ecl://guide/{topic}`
- `ecl://component/{id}/html`
- `ecl://component/{id}/twig/{filename}`

Tools remain available for clients without MCP resource support.

The `europa-component-library` symlink is a separate upstream checkout used for
tagged-source comparison during maintenance. It is not a runtime dependency
and is not copied into the published package. The active MCP contract is EC
only; legacy EU files retained for traceability are not advertised.

For the supported page setup, copy the `assets/` and `fonts/` directories as
siblings, load the dependencies described by `guide("assets")`, and initialize
the supplied ECL bundle with `ECL.autoInit()` after the page markup.
