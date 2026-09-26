import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import * as z from "zod/v4";
import { fileURLToPath } from "url";
import { dirname, join } from "path";
import { readdir } from "fs/promises";
import { createHash } from "crypto";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

// Utility functions
async function readFileContent(filePath) {
  const fs = await import("fs/promises");
  return await fs.readFile(filePath, "utf-8");
}

async function readDir(dirPath) {
  return await readdir(dirPath);
}

const skillsDirectory = join(__dirname, "skills");

function parseSkillFrontmatter(content, fallbackId) {
  const frontmatter = content.match(/^---\s*\n([\s\S]*?)\n---/);
  const metadata = frontmatter?.[1] || "";
  const name = metadata.match(/^name:\s*(.+)$/m)?.[1]?.trim() || fallbackId;
  const description =
    metadata.match(/^description:\s*(.+)$/m)?.[1]?.trim() || "";
  const version =
    metadata.match(/^\s+version:\s*(.+)$/m)?.[1]?.trim() || "1.0.0";

  return { name, description, version };
}

async function listSkills() {
  try {
    const entries = await readdir(skillsDirectory, { withFileTypes: true });
    const skills = [];

    for (const entry of entries) {
      if (!entry.isDirectory()) {
        continue;
      }

      const id = entry.name;
      const filePath = join(skillsDirectory, id, "SKILL.md");

      try {
        const content = await readFileContent(filePath);
        const metadata = parseSkillFrontmatter(content, id);
        skills.push({
          id,
          name: metadata.name,
          description: metadata.description,
          version: metadata.version,
          sha256: createHash("sha256").update(content).digest("hex"),
          file: "SKILL.md",
          resource: `ecl://skill/${encodeURIComponent(id)}`,
          call: {
            tool: "skill_get",
            parameters: { id },
          },
        });
      } catch (error) {
        // A skill directory without a readable SKILL.md is not advertised.
      }
    }

    return skills.sort((left, right) => left.id.localeCompare(right.id));
  } catch (error) {
    return [];
  }
}

async function getSkill(id) {
  const skills = await listSkills();
  const skill = skills.find((entry) => entry.id === id);

  if (!skill) {
    throw new Error(
      `Skill '${id}' not found. Please call the skill_list tool to see available skills.`,
    );
  }

  return {
    ...skill,
    content: await readFileContent(join(skillsDirectory, id, skill.file)),
  };
}

// Keep template discovery aligned with ECL component families instead of
// using a broad filename prefix. Prefix matching makes `file` include
// `file-upload` and exposes the legacy EU footer through the EC `site-footer`
// family. The families below mirror the helper Twig files shipped for the
// pinned EC release. Retired legacy files remain on disk for traceability but
// are not advertised or returned as part of an active EC family.
const templateFamilies = {
  carousel: ["carousel.html.twig", "slider-pager.html.twig"],
  "category-filter": [
    "category-filter.html.twig",
    "category-filter-items.html.twig",
  ],
  checkbox: ["checkbox-group.html.twig", "checkbox-item.html.twig"],
  file: ["file.html.twig"],
  "file-upload": ["file-upload.html.twig", "file-upload-status.html.twig"],
  gallery: [
    "gallery.html.twig",
    "gallery-item.html.twig",
    "gallery-overlay.html.twig",
  ],
  "highlighted-search": ["highlighted-search.html.twig"],
  "list-illustration": [
    "list-illustration.html.twig",
    "list-illustration-item.html.twig",
  ],
  "mega-menu": [
    "mega-menu.html.twig",
    "mega-menu-item.html.twig",
    "mega-menu-featured-item.html.twig",
  ],
  menu: ["menu.html.twig", "menu-item.html.twig"],
  "navigation-list": [
    "navigation-list.html.twig",
    "navigation-list-item.html.twig",
  ],
  "page-header": ["page-header.html.twig", "page-header-expandable.html.twig"],
  quiz: ["quiz.html.twig", "quiz-card.html.twig"],
  radio: ["radio-group.html.twig", "radio-button.html.twig"],
  "site-footer": [
    "site-footer-ec.html.twig",
    "site-footer-ec-section.html.twig",
  ],
  "site-header": [
    "site-header.html.twig",
    "site-header-language-switcher.html.twig",
  ],
  "story-card": [
    "story-card.html.twig",
    "story-card-card.html.twig",
    "slider-pager.html.twig",
  ],
  tag: ["tag.html.twig", "tag-set.html.twig"],
  timeline: ["timeline.html.twig", "timeline-set.html.twig"],
};

function getTemplateFiles(componentId, files) {
  const family = templateFamilies[componentId] || [`${componentId}.html.twig`];
  return family.filter((file) => files.includes(file));
}

const server = new McpServer(
  {
    name: "ecl-v5-server",
    version: "5.3.1",
  },
  {
    instructions:
      "For ECL implementation work, use skill_get for the reusable local-component workflow, then use guide_list and components_list as the live ECL inventory. The server supplies read-only HTML, Twig, starter-template, guide, and skill content; adapt it into the consuming project rather than copying the catalogue wholesale.",
  },
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
      throw new Error(
        `Guide for topic '${topic}' not found. Please call the guide_list tool to see available guides.`,
      );
    }
  },
);

server.registerTool(
  "skill_list",
  {
    description:
      "List reusable AI agent skills provided by this ECL MCP server",
    inputSchema: {},
  },
  async () => {
    return {
      content: [
        { type: "text", text: JSON.stringify(await listSkills(), null, 2) },
      ],
    };
  },
);

server.registerTool(
  "skill_get",
  {
    description:
      "Get the complete SKILL.md content for an ECL implementation skill",
    inputSchema: {
      id: z.string().describe("The skill ID returned by skill_list"),
    },
  },
  async ({ id }) => {
    const skill = await getSkill(id);
    return {
      content: [{ type: "text", text: skill.content }],
    };
  },
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
      const mdFiles = files.filter((file) => file.endsWith(".md"));
      const guides = [];

      for (const file of mdFiles) {
        const filePath = join(__dirname, "guides", file);
        const content = await readFileContent(filePath);
        const snippet = content.substring(0, 120);
        const topic = file.replace(".md", "");
        guides.push({
          topic,
          snippet: snippet + (content.length > 120 ? "..." : ""),
          call: {
            tool: "guide",
            parameters: { topic },
          },
        });
      }

      return {
        content: [{ type: "text", text: JSON.stringify(guides, null, 2) }],
      };
    } catch (error) {
      throw new Error(`Failed to list guides: ${error.message}`);
    }
  },
);

server.registerTool(
  "components_list",
  {
    description:
      "List all available components with their IDs and call information",
    inputSchema: {},
  },
  async () => {
    try {
      const files = await readDir(join(__dirname, "components"));
      const htmlFiles = files.filter(
        (file) => file.endsWith(".html") && !file.endsWith(".html.twig"),
      );
      const components = [];

      for (const file of htmlFiles) {
        const id = file.replace(".html", "");
        const component = {
          id,
          component_call: {
            tool: "component",
            parameters: { id },
          },
        };
        if (getTemplateFiles(id, files).length > 0) {
          component.template_call = {
            tool: "component_template",
            parameters: { id },
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
  },
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
      throw new Error(
        `Component with id '${id}' not found. Please call the components_list tool to see available components.`,
      );
    }
  },
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
  },
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
      throw new Error(
        `Failed to get templates for component '${id}': ${error.message}`,
      );
    }
  },
);

function registerTextResource(
  name,
  uri,
  filePath,
  mimeType,
  description,
  processContent = (content) => content,
) {
  server.registerResource(
    name,
    uri,
    {
      mimeType,
      description,
    },
    async (resourceUri) => ({
      contents: [
        {
          uri: resourceUri.href,
          mimeType,
          text: processContent(await readFileContent(filePath)),
        },
      ],
    }),
  );
}

async function registerContentResources() {
  registerTextResource(
    "starter-template",
    "ecl://starter-template",
    join(__dirname, "starter-template.html"),
    "text/html",
    "Complete ECL EC starter page template",
  );

  const guideFiles = (await readDir(join(__dirname, "guides")))
    .filter((file) => file.endsWith(".md"))
    .sort();

  for (const file of guideFiles) {
    const topic = file.replace(".md", "");
    registerTextResource(
      `guide-${topic}`,
      `ecl://guide/${encodeURIComponent(topic)}`,
      join(__dirname, "guides", file),
      "text/markdown",
      `ECL implementation guide: ${topic}`,
      (content) => content.replace(/__DIR__/g, __dirname),
    );
  }

  const componentFiles = (await readDir(join(__dirname, "components")))
    .filter((file) => file.endsWith(".html") && !file.endsWith(".html.twig"))
    .sort();
  const componentIds = componentFiles.map((file) => file.replace(".html", ""));
  const templateFiles = await readDir(join(__dirname, "components"));

  for (const id of componentIds) {
    registerTextResource(
      `component-${id}-html`,
      `ecl://component/${encodeURIComponent(id)}/html`,
      join(__dirname, "components", `${id}.html`),
      "text/html",
      `Rendered ECL HTML examples for component: ${id}`,
    );

    for (const file of getTemplateFiles(id, templateFiles)) {
      registerTextResource(
        `component-${id}-twig-${file}`,
        `ecl://component/${encodeURIComponent(id)}/twig/${encodeURIComponent(file)}`,
        join(__dirname, "components", file),
        "text/plain",
        `ECL Twig template for component ${id}: ${file}`,
      );
    }
  }

  for (const skill of await listSkills()) {
    registerTextResource(
      `skill-${skill.id}`,
      `ecl://skill/${encodeURIComponent(skill.id)}`,
      join(skillsDirectory, skill.id, skill.file),
      "text/markdown",
      `Reusable AI agent skill: ${skill.name}`,
    );
  }
}

await registerContentResources();

const transport = new StdioServerTransport();
await server.connect(transport);
console.error("ECL V5 MCP server is running...");
