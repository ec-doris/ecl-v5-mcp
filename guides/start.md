# Building with the ECL EC MCP Server

This server provides static EC HTML examples, Twig templates, a starter page,
bundled CSS/JavaScript/assets, focused guides, and a reusable ECL implementation
skill. The shared assets and reference materials target **ECL v5.3.1**. The
server does not render arbitrary component parameters. Use the eight tool names
below; it does not expose tools named
`get_component_examples` or `get_component`.

## Reusable agent skill

Call `skill_list` to discover the available implementation skills and
`skill_get` with `id: "ecl-component-development"` to retrieve the complete
`SKILL.md` file. The skill is intended for incorporation into the consuming
project's own agent skills directory. It tells an agent how to create reusable
local ECL components from the server's rendered HTML and Twig foundations,
including ECL's whitespace-sensitive markup conventions.

The server returns the file content; installation into a particular agent's
skills directory remains a client- or project-specific operation.

## Available MCP tools

### `starter_template`

Returns `starter-template.html`, an EC page shell with the required asset
links, site header, navigation, breadcrumbs, main region, footer, and ECL
auto-initialization. Its setup uses v5.3.1 assets; the site-wide markup audit is
still pending, so treat it as an integration starting point.

```json
{ "tool": "starter_template", "parameters": {} }
```

### `components_list`

Returns the available component IDs and advertised HTML and Twig calls. The
current list also includes a legacy EU footer; choose EC examples. The tooltip
Twig call is advertised but has no standalone template, as noted below.

```json
{ "tool": "components_list", "parameters": {} }
```

### `component`

Returns the reusable, fully rendered HTML examples in
`components/{id}.html`:

```json
{
  "tool": "component",
  "parameters": { "id": "button" }
}
```

The result often contains several named variants so an agent can see every
supported markup branch, extension hook, and EC color mode. Select the complete
example that matches the task; do not insert the entire response into a page
unless all demonstrations are actually wanted. Preserve the chosen example's
required BEM classes, `data-ecl-*` hooks, ARIA relationships, and IDs. Make IDs
unique when using more than one instance.

### `component_template`

Returns a JSON object of matching Twig filenames and source text:

```json
{
  "tool": "component_template",
  "parameters": { "id": "accordion" }
}
```

Use this when inspecting templates for a Twig application, checking their
recorded version first. The current handler uses explicit EC template families:
`file` does not include `file-upload`, and `site-footer` returns only the EC
footer and section helpers. Imported ECL components remain separate
dependencies. Tooltip has no standalone Twig template, so
`component_template("tooltip")` currently fails; use its HTML example. The
layout-wrapper Twig helper is an upstream layout reference and is intentionally
not part of the active component contract. For plain HTML, use `component`
instead.

### `guide_list`

Returns every available guide topic with a short snippet and a valid `guide`
call:

```json
{ "tool": "guide_list", "parameters": {} }
```

### `guide`

Returns a focused guide by its filename topic:

```json
{
  "tool": "guide",
  "parameters": { "topic": "spacing" }
}
```

### `skill_list`

Returns the reusable agent skills provided by this server, including their IDs,
descriptions, files, resource URIs, and valid `skill_get` calls:

```json
{ "tool": "skill_list", "parameters": {} }
```

### `skill_get`

Returns the complete `SKILL.md` content for a skill. Save the returned text as
the skill's `SKILL.md` in the consuming project's supported skills directory
when the project chooses to install it:

```json
{
  "tool": "skill_get",
  "parameters": { "id": "ecl-component-development" }
}
```

## MCP resources

Clients that support MCP resources can read the same content without using a
tool call. Resources are read-only and are useful for documents that the agent
may cite, attach, cache, or load on demand. The server exposes:

- `ecl://skill/ecl-component-development`
- `ecl://starter-template`
- `ecl://guide/{topic}`
- `ecl://component/{id}/html`
- `ecl://component/{id}/twig/{filename}`

The tool and resource paths intentionally overlap. Tools are the compatibility
path for clients that do not support resources; resources provide a better
document-oriented path for templates, examples, guides, and the skill itself.

Current topics include `assets`, `background`, `border`, `clearfix`, `colours`,
`dimension`, `disablescroll`, `display`, `flex`, `float`, `grid`, `html-tag`,
`icons`, `icons-without-webtools`, `images`, `logos`, `media`, `print`,
`screen-reader`, `shadow`, `spacing`, `start`, `typography`,
`utility-classes`, and `z-index`. Use `guide_list` rather than assuming a topic
exists; it is the authoritative list.

## Recommended workflow

### 1. Start from the page shell

Call `starter_template` when creating a new EC page. Retain the document
language, viewport metadata, stylesheet ordering, print media attribute,
JavaScript dependencies, WebTools loader, `no-js`/`has-js` switch, and
`ECL.autoInit()` call. Replace demonstration content and links with the
application's real content.

For an existing application, do not replace its whole shell automatically.
Compare it with the starter and add only missing ECL prerequisites.

### 2. Copy and load the assets

Call `guide("assets")` and follow its copy paths and load order. In summary, the
package's `assets/` and `fonts/` directories must remain siblings so the local
Inter fallbacks resolve. The normal EC setup includes:

- reset, main component, color-mode, utility, and print CSS;
- the EC browser JavaScript bundle;
- the WebTools loader for icons and WebTools-managed actions such as Add to
  calendar;
- Duet Date Picker when the datepicker is used;
- favicons and EC logo assets.

Do not copy `./europa-component-library` into the application. That path is a
development symlink used to verify this MCP package against the base
repository; it is not a runtime dependency and is not shipped in the npm
package.

### 3. Discover and choose a component

Call `components_list`, then call `component` with an exact returned ID. Review
all named examples and choose the smallest variant that completely matches the
requested behavior.

```json
{
  "tool": "component",
  "parameters": { "id": "notification" }
}
```

Do not synthesize component markup from memory. ECL components are structurally
strict, and seemingly redundant wrappers, modifier classes, accessibility
attributes, and JavaScript hooks often have a purpose.

### 4. Adapt content without breaking the contract

It is normally safe to replace visible text, URLs, image sources and alternative
text, and unique IDs together with every reference to them. Preserve:

- root, element, and modifier classes required by the chosen variant;
- `data-ecl-auto-init` and component-specific `data-ecl-*` hooks;
- hidden fallback content and initial state;
- ARIA roles, state, relationships, and accessible labels;
- required nesting and sibling order;
- native element types, button `type`, form names, and values where relevant.

Do not author `data-ecl-auto-initialized`; the ECL runtime adds it. Do not copy
an ID unchanged when the page already contains it.

### 5. Apply layout and utility guidance

Use the focused guides instead of guessing class names. Common calls are:

- `guide("grid")` for containers, rows, columns, offsets, and gutters;
- `guide("spacing")` for responsive logical margin and padding;
- `guide("display")` and `guide("flex")` for responsive layout;
- `guide("typography")` and `guide("colours")` for text and color modes;
- `guide("icons")` for WebTools families and accessibility;
- `guide("images")` and `guide("logos")` for EC visual-content and branding
  decisions;
- `guide("html-tag")` for the optional bare-tag preset;
- `guide("disablescroll")`, `guide("print")` and `guide("screen-reader")` for
  document utilities;
- `guide("utility-classes")` for a cross-guide inventory.

Prefer a component's built-in layout and spacing before layering utilities on
its internal elements. Use utilities for intentional composition or documented
customization, not to reconstruct an existing component.

### 6. Initialize and test behavior

The starter switches `no-js` to `has-js` in the head and initializes after the
DOM content and classic EC bundle have loaded:

```html
<script src="assets/ecl-ec.js"></script>
<script>
  ECL.autoInit();
</script>
```

For ES modules, use the single import-and-initialize script in `guide("assets")`.

This initializes elements bearing supported `data-ecl-auto-init` values. If
markup is inserted after auto-initialization, call `ECL.autoInit()` again after
insertion, or scope a new call to a parent container:

```js
ECL.autoInit({ root: document.querySelector("#dynamic-content") });
```

The root must contain the component roots: the query scans descendants, not the
root itself. Already initialized nodes are skipped. In v5.3.1, the returned
`update()` function reuses the original node list and does **not** discover new
nodes. Use the component’s lifecycle API when changing or removing an existing
instance; the returned `destroy()` clears all registered ECL instances, not just
those inside the supplied root.

Test at EC breakpoints (480px, 768px, 996px, and 1140px), with keyboard and
screen-reader interaction, without JavaScript where a fallback exists, in RTL
when relevant, and in print when the content must print correctly.

## Choosing HTML or Twig

| Need                                     | Tool                 |
| ---------------------------------------- | -------------------- |
| Copy a ready-to-adapt HTML example       | `component`          |
| Install or inspect official Twig sources | `component_template` |
| Build a complete new EC page shell       | `starter_template`   |
| Discover valid component IDs             | `components_list`    |
| Discover documentation topics            | `guide_list`         |
| Learn a utility or setup contract        | `guide`              |

The Twig parameter contract is documented in comments and package source, but
the MCP tool returns source rather than rendering caller-supplied data. The HTML
examples are already rendered and contain no Twig syntax.

## Troubleshooting

- “Component not found”: call `components_list` and use an exact ID.
- “Guide not found”: call `guide_list` and use an exact topic.
- Unstyled utility: confirm `ecl-ec-utilities.css` is loaded before the main EC
  stylesheet, with the media attribute for the intended output, and that the
  class exists in the relevant focused guide. Some utilities use `!important`.
- Missing icon or WebTools-managed action: load
  `https://webtools.europa.eu/load.js` on an approved origin and use the
  relevant contract from `guide("icons")` or the component guide. The loader
  is external and origin-sensitive.
- Interactive component does nothing: verify `assets/ecl-ec.js`, the exact
  `data-ecl-auto-init` value and hooks, and the `ECL.autoInit()` call.
- Broken ARIA relationship: make the instance IDs unique and update every
  `aria-controls`, `aria-labelledby`, `for`, or component-specific target at the
  same time.
- Layout changes at an unexpected width: ECL is mobile-first; responsive classes
  use `min-width` and continue upward until overridden.

The shared assets are from ECL v5.3.1, pinned to commit
`0b3ca5a9190e1c32ff00fc092380e3a8f3571a05`. The provenance manifest is not
shipped because it is not needed by the MCP runtime. Content-file edits are read
on each tool call; changes to `index.js` require a server restart or client
reconnect.

Setup reference: [official EC getting started](https://ec.europa.eu/component-library/ec/getting-started/).

For terminology and related EC resources, consult the official
[glossary](https://ec.europa.eu/component-library/ec/resources/glossary/),
[eUI resource](https://ec.europa.eu/component-library/ec/resources/eui/) and
[WebTools resource](https://ec.europa.eu/component-library/ec/resources/webtools/)
pages. They are reference links, not additional MCP tools or implementation
scope.
