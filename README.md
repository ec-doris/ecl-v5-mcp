# ECL v5 MCP Server

A basic Node.js MCP server that provides comprehensive ECL EC support.

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

be sure to use the full path of the `index.js` file. 
