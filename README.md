# Hello MCP Server

A basic Node.js MCP server that provides a "hello" tool returning "Hello, world!".

## Installation

1. Install dependencies:
   ```bash
   npm install github:ec-doris/ecl-v5-mcp
   ```

## Running the Server

To run the server using stdio transport:
```bash
node index.js
```

This server is designed to be used with MCP clients that communicate via stdio.

Configure the client to connect to this server for MCP tool calls.

### VS Code Extension
```json
{
    "servers": {
        "ecl": {
            "type": "stdio",
            "command": "node",
            "args": [
                "/Users/xxx/ecl_v5_mcp/index.js"
            ]
        }
    }
}
```