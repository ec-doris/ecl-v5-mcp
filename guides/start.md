# Building with the ECL EC MCP Server

This server provides static EC HTML examples, Twig templates, a starter page,
bundled CSS/JavaScript/assets, and focused guides. The shared assets target
**ECL v5.3.1**; the existing examples and other guides are being audited in
batches from the v5.0.1 baseline. Consult `__DIR__/update-status.md` for each
item’s verification status. The server does not render arbitrary component
parameters. Use the six tool names below; it does not expose tools named `get_component_examples` or `get_component`.

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
recorded version first. The current handler matches filename prefixes: `file`
also returns `file-upload`, and `site-footer` also returns the EU footer. Select
the intended EC family and its helpers; do not install every returned entry
unconditionally. Imported ECL components remain separate dependencies. Tooltip
has no standalone Twig template, so `component_template("tooltip")` currently
fails; use its HTML example. These delivery issues remain tracked for a later
batch. For plain HTML, use `component` instead.

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

Current topics are `assets`, `background`, `border`, `clearfix`, `colours`,
`dimension`, `display`, `flex`, `float`, `grid`, `icons`, `media`, `shadow`,
`spacing`, `start`, `typography`, `utility-classes`, and `z-index`. Use
`guide_list` rather than assuming a topic exists.

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
- the WebTools loader for icons;
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
- Missing icon: load `https://webtools.europa.eu/load.js` and use the correct
  standard or family-specific class pattern from `guide("icons")`.
- Interactive component does nothing: verify `assets/ecl-ec.js`, the exact
  `data-ecl-auto-init` value and hooks, and the `ECL.autoInit()` call.
- Broken ARIA relationship: make the instance IDs unique and update every
  `aria-controls`, `aria-labelledby`, `for`, or component-specific target at the
  same time.
- Layout changes at an unexpected width: ECL is mobile-first; responsive classes
  use `min-width` and continue upward until overridden.

The shared assets are from ECL v5.3.1, pinned to commit
`0b3ca5a9190e1c32ff00fc092380e3a8f3571a05`; their provenance and checksums are in
`__DIR__/docs/ecl-v5.3.1-assets.json`. The MCP package version is separate from
the ECL version. Content-file edits are read on each tool call; changes to
`index.js` require a server restart or client reconnect.

Setup reference: [official EC getting started](https://ec.europa.eu/component-library/ec/getting-started/).
