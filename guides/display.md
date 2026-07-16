# ECL Display Utilities (EC preset, v5.0.1)

Display utilities set an element's CSS `display` or `box-sizing` value. The EC
preset supplies 47 classes: nine display values at each of five breakpoints,
plus two non-responsive box-sizing utilities.

## Required CSS

Load the EC utilities stylesheet before using these classes:

```html
<link rel="stylesheet" href="assets/ecl-ec-utilities.css" />
```

Call `guide("assets")` for the complete asset setup. These rules are in
`ecl-ec-utilities.css`, not `ecl-ec.css`. They are also included in the supplied
`ecl-ec-print.css`. No JavaScript is required.

When compiling ECL from Sass packages, use `@ecl/utility-display`; its Sass
entry point is `display.scss` and it depends on `@ecl/grid` for breakpoints.

## Display classes

The base form is `ecl-u-d-{value}`:

| Base class             | CSS applied                        |
| ---------------------- | ---------------------------------- |
| `ecl-u-d-none`         | `display: none !important`         |
| `ecl-u-d-inline`       | `display: inline !important`       |
| `ecl-u-d-inline-block` | `display: inline-block !important` |
| `ecl-u-d-block`        | `display: block !important`        |
| `ecl-u-d-table`        | `display: table !important`        |
| `ecl-u-d-table-cell`   | `display: table-cell !important`   |
| `ecl-u-d-flex`         | `display: flex !important`         |
| `ecl-u-d-inline-flex`  | `display: inline-flex !important`  |
| `ecl-u-d-grid`         | `display: grid !important`         |

Every value also has `s`, `m`, `l`, and `xl` variants. Insert the breakpoint
before the value:

```text
ecl-u-d-{value}       0px and up
ecl-u-d-s-{value}     480px and up
ecl-u-d-m-{value}     768px and up
ecl-u-d-l-{value}     996px and up
ecl-u-d-xl-{value}    1140px and up
```

For example, the complete responsive family for `grid` is
`ecl-u-d-grid`, `ecl-u-d-s-grid`, `ecl-u-d-m-grid`, `ecl-u-d-l-grid`, and
`ecl-u-d-xl-grid`. The same five forms exist for every value in the table.
Breakpoint rules use `min-width`, so a responsive class continues to apply at
larger viewport widths until another class overrides it.

### Responsive visibility

```html
<!-- Hidden below 768px; displayed as a block from 768px upward. -->
<nav class="ecl-u-d-none ecl-u-d-m-block" aria-label="Section">...</nav>

<!-- Visible below 996px; hidden from 996px upward. -->
<div class="ecl-u-d-block ecl-u-d-l-none">Small-screen content</div>
```

Set both sides of a visibility change. A class such as `ecl-u-d-m-none` only
hides from that breakpoint upward; it does not express what should happen
below the breakpoint.

Do not use `display: none` for content that must remain available to screen
readers: hidden elements and their descendants are removed from the
accessibility tree. Keep the DOM reading and focus order meaningful when
changing layout across breakpoints.

### Flex and grid containers

```html
<div class="ecl-u-d-flex ecl-u-flex-wrap ecl-u-align-items-center">...</div>

<div class="ecl-u-d-grid">...</div>
```

`ecl-u-d-flex` and `ecl-u-d-inline-flex` only create a flex container; call
`guide("flex")` for direction, wrapping, alignment, ordering, growth, shrinkage,
and basis utilities. `ecl-u-d-grid` only changes `display`; ECL's layout grid
classes are documented by `guide("grid")`.

Use `table` and `table-cell` only when CSS table layout is intended. These
classes do not add semantic table roles; use native table markup for tabular
data.

## Box sizing classes

Box-sizing classes have no responsive variants:

| Class                      | CSS applied                          |
| -------------------------- | ------------------------------------ |
| `ecl-u-box-sizing-content` | `box-sizing: content-box !important` |
| `ecl-u-box-sizing-border`  | `box-sizing: border-box !important`  |

With `border-box`, the declared width and height include padding and borders.
With `content-box`, padding and borders are added outside the declared content
size.

```html
<div class="ecl-u-box-sizing-border" style="width: 12rem; padding: 1rem">
  The rendered border box remains 12rem wide.
</div>
```

## Implementation notes

- All declarations use `!important`. Avoid multiple display utilities that are
  active at the same breakpoint unless the intentional cascade is clear.
- Utilities impose no component markup, ARIA attributes, IDs, or JavaScript
  hooks.
- Display utilities do not add spacing, width, positioning, or alignment.
- The tagged v5.0.1 Sass and compiled EC bundle include `grid`, even though the
  v5.0.1 website usage list and display Storybook control omit it.
