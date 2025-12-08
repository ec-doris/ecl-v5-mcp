# Getting Started with ECL EC via MCP Server

This guide provides instructions for AI coding agents on how to use the Europa Component Library (ECL) EC system through the Model Context Protocol (MCP) server.

## Overview

The ECL EC MCP server provides tools to access ECL components, guides, and starter templates for building European Commission-compliant web applications.

## Available Tools

### 1. starter_template
**Purpose:** Get the base HTML template for ECL EC applications.

**Usage:**
```json
{
  "tool": "starter_template",
  "parameters": {}
}
```

**Returns:** Complete HTML starter template with all necessary CSS/JS includes and a basic page structure.

### 2. components_list
**Purpose:** List all available ECL components.

**Usage:**
```json
{
  "tool": "components_list",
  "parameters": {}
}
```

**Returns:** JSON array of components with their IDs and call information for retrieving each component.

### 3. component(id)
**Purpose:** Get the HTML implementation of a specific ECL component.

**Usage:**
```json
{
  "tool": "component",
  "parameters": {
    "id": "button"
  }
}
```

**Parameters:**
- `id`: The component identifier (e.g., "accordion", "button", "card")

**Returns:** HTML markup for the specified component.

### 4. guide_list
**Purpose:** List all available documentation guides.

**Usage:**
```json
{
  "tool": "guide_list",
  "parameters": {}
}
```

**Returns:** JSON array of guides with snippets and call information.

### 5. guide(topic)
**Purpose:** Get detailed documentation for a specific topic.

**Usage:**
```json
{
  "tool": "guide",
  "parameters": {
    "topic": "start"
  }
}
```

**Parameters:**
- `topic`: The guide topic (e.g., "start", "colours", "typography", "utility-classes")

### 6. component_template(id)
**Purpose:** Get the Twig template(s) for a specific ECL component.

**Usage:**
```json
{
  "tool": "component_template",
  "parameters": {
    "id": "accordion"
  }
}
```

**Parameters:**
- `id`: The component identifier (e.g., "accordion", "button", "mega-menu")

**Returns:** JSON object containing template filenames as keys and their Twig content as values. Components with multiple templates (like mega-menu) return all related templates.

## Workflow for Building ECL Applications

### Step 1: Get the Starter Template
Begin by calling `starter_template` to obtain the base HTML structure. This provides:
- Proper HTML5 doctype and meta tags
- ECL CSS and JavaScript includes
- Basic page structure with header, navigation, breadcrumbs, main, and footer
- Language selector and navigation components

### Step 2: Copy Required Assets
Use the `guide("assets")` tool to get instructions on copying ECL assets to your project. The guide contains paths to the assets directory that need to be copied.

### Step 3: Add Components
1. Call `components_list` to see all available components
2. For each component you need, call `component(id)` with the appropriate ID
3. Integrate the returned HTML into your page structure

### Step 4: Apply Styling
Use the following guides for styling information:
- `guide("colours")` - Color palette and usage
- `guide("typography")` - Text styling and hierarchy
- `guide("utility-classes")` - Utility classes for layout and spacing

## Component Categories

Components are organized into categories including:
- **Layout:** Containers, grids, spacing
- **Navigation:** Menus, breadcrumbs, pagination
- **Forms:** Inputs, buttons, selects, checkboxes
- **Content:** Cards, accordions, tabs, tables
- **Feedback:** Notifications, modals, tooltips
- **Media:** Images, videos, galleries

## Best Practices

1. **Always start with the starter template** - It includes all necessary dependencies
2. **Copy assets as instructed** - ECL requires specific CSS/JS files
3. **Use semantic HTML** - ECL components follow accessibility standards
4. **Always use utility classes for spacing and layout** - Refer to the utility classes guide
5. **Typography and colors** - Follow the typography and color guides for consistency
6. **Test responsiveness** - ECL is mobile-first and responsive
7. **Follow the design system** - Use provided colors, typography, and spacing
8. **Avoid custom CSS** - Rely on ECL classes to ensure compatibility and maintainability

## Caveats
- ECL is extremely verbose on it's classes use. Make sure to include all necessary classes for components to render correctly. Even <p>, <ul> and <div> tags may need specific classes.
- Some components may require JavaScript to function properly. Ensure that the ECL JS files are included in your project.
- ECL is not fault tolerant, meaning missing classes or incorrect structure may lead to broken components. Take your time to follow the documentation closely.
- Most ECL applications are "spaceless" meaning there should be no spaces, tabs or new lines between many HTML tags. This is important for components like buttons and inputs to render correctly. If you are experiencing issues, check for unwanted whitespace in your HTML.

## Example Usage

To create a simple page with a button:

1. Get starter template
2. Get button component: `component("button")`
3. Insert button HTML into the main content area
4. Style as needed using utility classes

## Troubleshooting

- If a component isn't found, check `components_list` for valid IDs
- If a guide topic doesn't exist, use `guide_list` to see available topics
- Ensure assets are properly copied from the paths specified in `guide("assets")`

## Additional Resources

- Official ECL Documentation: https://ec.europa.eu/component-library/
- WebTools Icons: https://webtools.europa.eu/showcase/demo?comp=icons</content>
<parameter name="filePath">/Users/brownrl/Herd/ecl_v5_mcp/guides/start.md