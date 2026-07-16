# ECL Shadow Utilities (EC preset, v5.0.1)

The EC preset provides five drop-shadow elevations and one reset class. It does
not provide responsive, inset, inner, or negative shadow utilities.

## Required CSS

Load the main EC stylesheet for the shadow custom properties and the utilities
stylesheet for the classes:

```html
<link rel="stylesheet" href="assets/ecl-ec.css" />
<link rel="stylesheet" href="assets/ecl-ec-utilities.css" />
```

Call `guide("assets")` for the complete asset setup. The six utility rules are
not in `ecl-ec.css`; they are also included in `ecl-ec-print.css`. No JavaScript
is required.

When compiling from Sass, use `@ecl/utility-shadow` and its `shadow.scss` entry
point.

## Classes and EC values

| Class               | CSS applied                          | EC shadow value                                        |
| ------------------- | ------------------------------------ | ------------------------------------------------------ |
| `ecl-u-shadow-none` | `box-shadow: none !important`        | No shadow                                              |
| `ecl-u-shadow-1`    | `box-shadow: var(--sh-1) !important` | 0 0 0.5px 0.5px at 8% opacity, plus 0 6px 12px at 8%   |
| `ecl-u-shadow-2`    | `box-shadow: var(--sh-2) !important` | 0 0 0.5px 0.5px at 8% opacity, plus 0 10px 22px at 10% |
| `ecl-u-shadow-3`    | `box-shadow: var(--sh-3) !important` | 0 0 0.5px 0.5px at 8% opacity, plus 0 12px 32px at 12% |
| `ecl-u-shadow-4`    | `box-shadow: var(--sh-4) !important` | 0 0 0.5px 0.5px at 8% opacity, plus 0 14px 42px at 12% |
| `ecl-u-shadow-5`    | `box-shadow: var(--sh-5) !important` | 0 0 0.5px 0.5px at 8% opacity, plus 0 18px 52px at 14% |

All shadow layers use RGB `24, 39, 75` (`#18274b`) with the opacity shown. The
public aliases `--sh-1` through `--sh-5` point to `--ecl-shadow-1` through
`--ecl-shadow-5` in the EC theme.

```html
<article class="ecl-u-shadow-2 ecl-u-pa-l">
  <h2 class="ecl-u-type-heading-2">Card title</h2>
  <p>Card content</p>
</article>
```

Use a higher number only when the design calls for stronger visual elevation.
Shadows should reinforce an actual layer relationship rather than serve as
decoration.

## Removing or changing a shadow

```html
<div class="ecl-u-shadow-none">...</div>
```

`ecl-u-shadow-none` clears the entire `box-shadow` property. To change state,
remove the old elevation class and add the new one or the reset; do not retain
multiple shadow utilities.

The classes cannot be combined to build a multi-part effect. Each sets the
whole `box-shadow` property with `!important`, so competing classes depend on
CSS source order rather than HTML class order.

## Scope and limitations

- EC v5.0.1 emits exactly these six non-responsive classes. Names such as
  `ecl-u-shadow-inner-1`, `ecl-u-shadow-negative-1`, or
  `ecl-u-shadow-m-2` are not present in the EC assets.
- The shared Sass utility can generate additional families when a theme defines
  `shadow-inner`, `shadow-negative`, or `shadow-negative-inner`; the EC theme
  defines none of them. Do not copy EU-only class advice into an EC page.
- Shadows do not change layout dimensions or stacking order. Call
  `guide("z-index")` for stacking utilities.
- Avoid relying on a shadow alone to convey state or boundaries; ensure adequate
  contrast and another understandable cue where meaning is involved.
