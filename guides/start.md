# Building with the ECL EC MCP Server

This server provides static, reusable EC v5.0.1 markup, the matching Twig
templates, a complete starter page, bundled CSS/JavaScript/assets, and focused
guides. It does not generate a component from arbitrary parameters and it does
not expose tools named `get_component_examples` or `get_component`.

## Available MCP tools

### `starter_template`

Returns `starter-template.html`, a complete EC page with the required asset
links, site header, navigation, breadcrumbs, main region, footer, and ECL
auto-initialization.

```json
{ "tool": "starter_template", "parameters": {} }
```

### `components_list`

Returns the authoritative list of available component IDs. Each item includes
the valid calls for its reusable HTML and Twig source.

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

Returns a JSON object whose keys are the component-owned Twig filenames and
whose values are the exact EC v5.0.1 Twig sources:

```json
{
  "tool": "component_template",
  "parameters": { "id": "accordion" }
}
```

Use this when integrating the official templates into a Twig application. Some
components have multiple owned templates or partials, so consume every returned
entry. Imported ECL components remain separate dependencies. For plain HTML,
use `component` instead.

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
read-only development symlink used to verify this MCP package against the base
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

The starter calls:

```html
<script>
  document.documentElement.classList.remove("no-js");
  document.documentElement.classList.add("has-js");

  if (typeof ECL !== "undefined") {
    ECL.autoInit();
  }
</script>
```

This initializes elements bearing supported `data-ecl-auto-init` values. If
markup is inserted after auto-initialization, call the update function returned
by `ECL.autoInit()` or initialize the relevant component according to the
application's runtime architecture; do not assume new DOM is discovered
automatically.

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
- Unstyled utility: confirm `ecl-ec-utilities.css` is loaded after the main EC
  stylesheet and that the class exists in the relevant focused guide.
- Missing icon: load `https://webtools.europa.eu/load.js` and use the correct
  standard or family-specific class pattern from `guide("icons")`.
- Interactive component does nothing: verify `assets/ecl-ec.js`, the exact
  `data-ecl-auto-init` value and hooks, and the `ECL.autoInit()` call.
- Broken ARIA relationship: make the instance IDs unique and update every
  `aria-controls`, `aria-labelledby`, `for`, or component-specific target at the
  same time.
- Layout changes at an unexpected width: ECL is mobile-first; responsive classes
  use `min-width` and continue upward until overridden.

The package and its compiled assets target the EC preset at ECL v5.0.1, pinned
to base-repository commit `eceefe9468e44f7ce9c57801c91c4c0c057548b4`.
