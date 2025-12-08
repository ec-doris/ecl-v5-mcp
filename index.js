import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import * as z from "zod/v4";
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

// Utility functions
async function readFileContent(filePath) {
    const fs = await import("fs/promises");
    return await fs.readFile(filePath, "utf-8");
}

async function readDir(dirPath) {
    const fs = await import("fs/promises");
    return await fs.readdir(dirPath);
}

const server = new McpServer(
    {
        name: "ecl-v5-server",
        version: "1.0.0",
    }
);

server.registerTool(
    "guide",
    {
        description: "Get the content of a guide markdown file",
        inputSchema: {
            topic: z.string().describe("The topic of the guide"),
        },
    },
    async ({ topic }) => {
        const filePath = join(__dirname, "guides", `${topic}.md`);
        try {
            const content = await readFileContent(filePath);
            const processedContent = content.replace(/__DIR__/g, __dirname);
            return {
                content: [{ type: "text", text: processedContent }],
            };
        } catch (error) {
            throw new Error(`Guide for topic '${topic}' not found. Please call the guide_list tool to see available guides.`);
        }
    }
);

server.registerTool(
    "guide_list",
    {
        description: "List all available guides with snippets",
        inputSchema: {},
    },
    async () => {
        try {
            const files = await readDir(join(__dirname, "guides"));
            const mdFiles = files.filter(file => file.endsWith('.md'));
            const guides = [];

            for (const file of mdFiles) {
                const filePath = join(__dirname, "guides", file);
                const content = await readFileContent(filePath);
                const snippet = content.substring(0, 120);
                const topic = file.replace('.md', '');
                guides.push({
                    topic,
                    snippet: snippet + (content.length > 120 ? '...' : ''),
                    call: {
                        tool: "guide",
                        parameters: { topic }
                    }
                });
            }

            return {
                content: [{ type: "text", text: JSON.stringify(guides, null, 2) }],
            };
        } catch (error) {
            throw new Error(`Failed to list guides: ${error.message}`);
        }
    }
);

server.registerTool(
    "components_list",
    {
        description: "List all available components with their IDs and call information",
        inputSchema: {},
    },
    async () => {
        try {
            const files = await readDir(join(__dirname, "components"));
            const htmlFiles = files.filter(file => file.endsWith('.html') && !file.endsWith('.html.twig'));
            const components = [];

            for (const file of htmlFiles) {
                const id = file.replace('.html', '');
                components.push({
                    id,
                    component_call: {
                        tool: "component",
                        parameters: { id }
                    },
                    template_call: {
                        tool: "component_template",
                        parameters: { id }
                    }
                });
            }

            return {
                content: [{ type: "text", text: JSON.stringify(components, null, 2) }],
            };
        } catch (error) {
            throw new Error(`Failed to list components: ${error.message}`);
        }
    }
);

server.registerTool(
    "component",
    {
        description: "Get the HTML content of a component by its ID",
        inputSchema: {
            id: z.string().describe("The ID of the component"),
        },
    },
    async ({ id }) => {
        const filePath = join(__dirname, "components", `${id}.html`);
        try {
            const content = await readFileContent(filePath);
            return {
                content: [{ type: "text", text: content }],
            };
        } catch (error) {
            throw new Error(`Component with id '${id}' not found. Please call the components_list tool to see available components.`);
        }
    }
);

server.registerTool(
    "starter_template",
    {
        description: "Get the starter template HTML content",
        inputSchema: {},
    },
    async () => {
        const filePath = join(__dirname, "starter-template.html");
        try {
            const content = await readFileContent(filePath);
            return {
                content: [{ type: "text", text: content }],
            };
        } catch (error) {
            throw new Error(`Failed to read starter template: ${error.message}`);
        }
    }
);

server.registerTool(
    "component_template",
    {
        description: "Get the Twig template(s) for a component by its ID",
        inputSchema: {
            id: z.string().describe("The ID of the component"),
        },
    },
    async ({ id }) => {
        try {
            const files = await readDir(join(__dirname, "components"));
            const twigFiles = files.filter(file => file.startsWith(`${id}`) && file.endsWith('.html.twig'));

            if (twigFiles.length === 0) {
                throw new Error(`No templates found for component '${id}'`);
            }

            const templates = {};
            for (const file of twigFiles) {
                const filePath = join(__dirname, "components", file);
                const content = await readFileContent(filePath);
                templates[file] = content;
            }

            return {
                content: [{ type: "text", text: JSON.stringify(templates, null, 2) }],
            };
        } catch (error) {
            throw new Error(`Failed to get templates for component '${id}': ${error.message}`);
        }
    }
);

const transport = new StdioServerTransport();
await server.connect(transport);
console.error("ECL V5 MCP server is running...");