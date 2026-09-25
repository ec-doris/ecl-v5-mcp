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

// Keep template discovery aligned with ECL component families instead of
// using a broad filename prefix. Prefix matching makes `file` include
// `file-upload` and exposes the legacy EU footer through the EC `site-footer`
// family. The families below mirror the helper Twig files shipped for the
// pinned EC release. Retired legacy files remain on disk for traceability but
// are not advertised or returned as part of an active EC family.
const templateFamilies = {
    carousel: ["carousel.html.twig", "slider-pager.html.twig"],
    "category-filter": ["category-filter.html.twig", "category-filter-items.html.twig"],
    checkbox: ["checkbox-group.html.twig", "checkbox-item.html.twig"],
    file: ["file.html.twig"],
    "file-upload": ["file-upload.html.twig", "file-upload-status.html.twig"],
    gallery: ["gallery.html.twig", "gallery-item.html.twig", "gallery-overlay.html.twig"],
    "highlighted-search": ["highlighted-search.html.twig"],
    "list-illustration": ["list-illustration.html.twig", "list-illustration-item.html.twig"],
    "mega-menu": ["mega-menu.html.twig", "mega-menu-item.html.twig", "mega-menu-featured-item.html.twig"],
    menu: ["menu.html.twig", "menu-item.html.twig"],
    "navigation-list": ["navigation-list.html.twig", "navigation-list-item.html.twig"],
    "page-header": ["page-header.html.twig", "page-header-expandable.html.twig"],
    quiz: ["quiz.html.twig", "quiz-card.html.twig"],
    radio: ["radio-group.html.twig", "radio-button.html.twig"],
    "site-footer": ["site-footer-ec.html.twig", "site-footer-ec-section.html.twig"],
    "site-header": ["site-header.html.twig", "site-header-language-switcher.html.twig"],
    "story-card": ["story-card.html.twig", "story-card-card.html.twig", "slider-pager.html.twig"],
    tag: ["tag.html.twig", "tag-set.html.twig"],
    timeline: ["timeline.html.twig", "timeline-set.html.twig"],
};

function getTemplateFiles(componentId, files) {
    const family = templateFamilies[componentId] || [`${componentId}.html.twig`];
    return family.filter(file => files.includes(file));
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
                const component = {
                    id,
                    component_call: {
                        tool: "component",
                        parameters: { id }
                    },
                };
                if (getTemplateFiles(id, files).length > 0) {
                    component.template_call = {
                        tool: "component_template",
                        parameters: { id }
                    };
                }
                components.push(component);
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
            const twigFiles = getTemplateFiles(id, files);

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
