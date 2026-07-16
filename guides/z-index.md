# ECL Z-index Utilities (EC preset, v5.0.1)

The EC preset provides six non-responsive stacking-order utilities. They set
only `z-index` and do not establish positioning. Whether the value participates
in stacking and creates a stacking context depends on the element's layout and
ancestors.

## Required CSS

Load the EC utilities stylesheet:

```html
<link rel="stylesheet" href="assets/ecl-ec-utilities.css" />
```

Call `guide("assets")` for the complete asset setup. These rules are not in
`ecl-ec.css` and are also present in `ecl-ec-print.css`. No JavaScript or color
mode stylesheet is required.

When compiling Sass, use `@ecl/utility-z-index` and its `z-index.scss` entry
point with the EC theme.

## Exact EC classes

| Class                | Declaration                | Intended tier                      |
| -------------------- | -------------------------- | ---------------------------------- |
| `ecl-u-z-highlight`  | `z-index: 1 !important`    | Just above ordinary content        |
| `ecl-u-z-navigation` | `z-index: 10 !important`   | Navigation and persistent page UI  |
| `ecl-u-z-dropdown`   | `z-index: 15 !important`   | Temporarily opened menus/dropdowns |
| `ecl-u-z-modal`      | `z-index: 50 !important`   | Modal-layer content                |
| `ecl-u-z-overlay`    | `z-index: 100 !important`  | Overlay-layer content              |
| `ecl-u-z-max`        | `z-index: 9999 !important` | Exceptional always-on-top content  |

The compiled v5.0.1 EC assets contain no `ecl-u-z-auto` or
`ecl-u-z-zero` classes. The shared utility README is stale for the EC theme: it
also says modal is 20 and omits overlay, while the EC theme and compiled CSS use
the table above. To reset a utility, remove it; use a project rule if an
explicit `auto` or `0` is required.

## Usage

For ordinary positioned elements:

```html
<header class="ecl-u-z-navigation" style="position: sticky; top: 0">...</header>
```

`z-index` participates when the element is positioned (`relative`, `absolute`,
`fixed`, or `sticky`) and also on flex/grid items. Adding only
`ecl-u-z-navigation` to an ordinary non-positioned block outside those contexts
may have no visible effect.

Use the lowest shared tier that expresses the element's role. Do not solve a
local overlap by reaching immediately for `ecl-u-z-max`; doing so makes later
layering harder to reason about.

## Stacking-context limits

A child cannot escape its ancestor's stacking context, even with 9999:

```html
<div style="position: relative; z-index: 1">
  <div class="ecl-u-z-max">Still inside the ancestor's z-index 1 context</div>
</div>
<div style="position: relative; z-index: 2">
  Can paint above that whole tree
</div>
```

Common stacking-context creators include a positioned element with a non-auto
z-index, fixed/sticky positioning, transforms, opacity below 1, filters,
isolation, and several containment properties. When a utility appears not to
work, inspect the entire ancestor chain and sibling stacking contexts rather
than only increasing the number.

## Component and accessibility guidance

- Prefer the z-index already supplied by an ECL modal, dropdown, navigation, or
  overlay component. Add a utility only for an intentional custom layer.
- Visual stacking does not manage focus, keyboard containment, dismissal,
  inert background content, or dialog semantics. Use the complete ECL component
  contract for interactive overlays.
- `ecl-u-z-overlay` being numerically above `ecl-u-z-modal` is the actual EC
  scale. Structure related backdrop and dialog layers according to their
  component CSS rather than assuming the names alone define their relationship.
- All six declarations use `!important`; remove conflicting z-index utilities
  instead of relying on HTML class order.
