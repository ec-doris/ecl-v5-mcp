---
name: ecl-component-development
description: Build reusable local European Commission ECL components and pages by using this MCP server's live HTML, Twig, starter template, assets, guides, and implementation contracts. Use for ECL/EC work in HTML, Twig, Blade, Vue, or another project framework; do not use for unrelated design systems.
metadata:
  version: 1.0.0
---

# ECL Component Development

Use this skill when an application needs a reusable local component, page, layout,
form, navigation element, or interactive behavior based on the European
Commission Europa Component Library (ECL).

The goal is to create and maintain the component in the consuming project. The
MCP server supplies authoritative ECL basis material; it is not a replacement
for the project's component layer. Do not leave repeated raw ECL markup in
pages when the application needs a reusable component.

## Discover the live ECL contract

Use the MCP server's current output instead of remembered ECL markup. When the
tools are available:

1. Call `skill_list`, then `skill_get` for this skill when the host has not
   already loaded it.
2. Call `guide_list` and `components_list` before choosing a guide, component,
   or template. These lists are authoritative for the installed server version.
3. Call `guide` for the focused topic, `component` for rendered HTML examples,
   and `component_template` for every Twig file in the component family.
4. Use `starter_template` and `guide("assets")` for a new standalone EC page.

When the host supports MCP resources, the equivalent read-only URIs are:

- `ecl://starter-template`
- `ecl://guide/{topic}`
- `ecl://component/{id}/html`
- `ecl://component/{id}/twig/{filename}`
- `ecl://skill/ecl-component-development`

Tools remain the compatibility path for clients that do not expose resources.

## Build the local project component

First search the consuming project for an existing ECL wrapper and follow its
framework, naming, props, slots, events, attribute-forwarding, and test
conventions. Reuse it when it already satisfies the requirement.

If it is missing:

1. Confirm the exact ECL component ID with `components_list`.
2. Inspect the complete rendered HTML example and every advertised Twig file.
3. Translate the Twig contract into the project's native component API. Keep
   the component reusable and compose existing local ECL subcomponents instead
   of copying their markup into every caller.
4. Preserve the ECL DOM contract: root and modifier classes, wrappers and
   nesting, native element types, `data-ecl-*` hooks, ARIA relationships,
   unique IDs, hidden fallback content, button types, form names, values, and
   extension attributes.
5. Add tests for the states and accessibility relationships the project
   supports, then use the component from the consuming page.

Rendered HTML is a reference for adaptation, not a page section to paste in
full. Choose the smallest complete variant and replace only content that is
safe to vary, such as visible text, URLs, image sources, and alternative text.
Do not copy showcase headings, explanatory text, demo IDs, color-mode examples,
or every variant unless the page actually needs them.

## Whitespace is part of the ECL contract

Do not treat whitespace as harmless formatting when adapting ECL markup.

- Many official Twig templates use `{% apply spaceless %}` and whitespace-control
  delimiters such as `{{- ... -}}`, `{%- ... -%}`. Preserve those controls when
  translating or extending the template.
- Do not add a formatted newline or indentation between inline icons, labels,
  indicators, and text nodes without checking the rendered result. HTML
  collapses such whitespace into a visible text gap and can change wrapping,
  label extraction, or icon/label alignment.
- Preserve meaningful spaces inside labels and translated strings. Do not apply
  a generic `trim()` or move text across elements merely to make source code
  prettier.
- Preserve ECL label wrappers such as `ecl-button__label` and
  `data-ecl-label="true"`; do not replace them with an unwrapped text node.
- When a component uses a macro, include, `spaceless` block, or trim marker,
  treat its exact placement as intentional. Compare the adapted output with the
  source example rather than normalizing all whitespace mechanically.
- Use component CSS and documented utilities for layout and gaps. Do not use
  literal spaces or extra text nodes as a substitute for the component's
  spacing contract.

Whitespace-sensitive review is especially important for buttons, links, labels,
icons, indicators, breadcrumbs, list items, and inline metadata. Check both the
browser appearance and the accessible text/name after adaptation.

## Assets, runtime, and verification

For a standalone page, preserve the starter's document metadata, stylesheet
ordering, print setup, WebTools loader, `no-js`/`has-js` switch, and guarded
`ECL.autoInit()` call. For an existing application, add only missing
prerequisites through its established asset pipeline; do not replace its shell
automatically.

Use `guide("assets")` for the current asset paths and load order. Use
`guide("icons")` before implementing icons. Use focused utility guides instead
of inventing ECL class names or token names.

When markup is inserted after initialization, initialize it through the
application's runtime or the documented ECL lifecycle/update mechanism. Do not
author `data-ecl-auto-initialized`; the runtime owns that attribute.

Verify relevant responsive breakpoints, keyboard behavior, accessible names and
relationships, no-JavaScript fallback, RTL behavior, and print output. If a
tool call conflicts with the skill or the local project, follow the live server
and project evidence and report the inconsistency rather than inventing a new
ECL contract.
