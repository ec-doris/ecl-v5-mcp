# ECL Background Utilities (EC preset, v5.0.1)

Background utilities set an element's `background-color`. They do not add text
colour, padding, borders, dimensions, or layout, and they do not remove a
`background-image`.

Every background declaration uses `!important`. Apply one background utility
per element and avoid competing `!important` rules.

## Required CSS

Load the EC theme variables, optional color modes, and utilities:

```html
<link rel="stylesheet" href="assets/ecl-ec.css" />
<link rel="stylesheet" href="assets/ecl-ec-color-modes.css" />
<link rel="stylesheet" href="assets/ecl-ec-utilities.css" />
```

Call `guide("assets")` for the complete asset setup. The background utility
rules are in `ecl-ec-utilities.css`, not `ecl-ec.css`; `ecl-ec.css` supplies
their default colour variables, and `ecl-ec-color-modes.css` supplies the 15
optional color-mode overrides. The rules are also present in
`ecl-ec-print.css`. No JavaScript is required.

When compiling ECL from Sass packages instead, pass the EC theme to the
background utility:

```scss
@use "@ecl/theme-ec/theme" as theme;
@use "@ecl/utility-background/background" with (
  $theme: theme.$theme
);
```

Without the theme parameter, the Sass source emits only the transparent,
white, and black utilities.

## Choosing a background

Use one of these approaches:

1. Use a semantic alias such as `ecl-u-bg-primary` when the semantic role is
   more important than a particular shade.
2. Use a numbered palette class such as `ecl-u-bg-primary-600` when the exact
   EC palette shade is required.
3. Use an adaptive surface class such as `ecl-u-bg-surface-0` when the
   background must respond to an ECL color mode.
4. Use `ecl-u-bg-white`, `ecl-u-bg-black`, or `ecl-u-bg-transparent` for those
   fixed values.

The utilities are not responsive; ECL v5.0.1 provides no breakpoint variants.

## Semantic background classes

Semantic aliases resolve through EC custom properties. Their v5.0.1 default
palette equivalents are shown here:

| Class                 | Default equivalent |
| --------------------- | ------------------ |
| `ecl-u-bg-primary`    | `primary-600`      |
| `ecl-u-bg-secondary`  | `secondary-400`    |
| `ecl-u-bg-neutral`    | `neutral-600`      |
| `ecl-u-bg-grey`       | `grey-950`         |
| `ecl-u-bg-alpha`      | `grey-alpha-950`   |
| `ecl-u-bg-monochrome` | `monochrome-500`   |
| `ecl-u-bg-info`       | `info-600`         |
| `ecl-u-bg-success`    | `success-700`      |
| `ecl-u-bg-error`      | `error-600`        |
| `ecl-u-bg-warning`    | `warning-500`      |

These semantic palette aliases do not change when an
`ecl-color-mode--*` class is applied. Use the surface utilities described below
for color-mode-aware backgrounds.

## Numbered palette classes

The class format is:

```text
ecl-u-bg-{family}-{shade}
```

Supported opaque families are:

- `primary`
- `secondary`
- `neutral`
- `grey`
- `monochrome`
- `info`
- `success`
- `error`
- `warning`

Every family above supports exactly these 13 shades:

```text
25, 50, 75, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950
```

Examples of valid classes include:

```html
<div class="ecl-u-bg-primary-50">Light primary background</div>
<div class="ecl-u-bg-primary-600 ecl-u-type-color-white">
  Primary background with a contrasting text utility
</div>
<div class="ecl-u-bg-error-100">Light error-palette background</div>
<div class="ecl-u-bg-monochrome-950 ecl-u-type-color-white">
  Dark monochrome background
</div>
```

The numbered shade classes are fixed palette colours. They do not adapt to
color modes.

### Alpha-shade defect in v5.0.1

The compiled v5.0.1 CSS contains all 13 shade selectors for both
`ecl-u-bg-grey-alpha-{shade}` and `ecl-u-bg-white-alpha-{shade}`, but their
declarations reference the undefined variables `--c-g-alpha` and
`--c-w-alpha`. Browsers therefore cannot use those declarations as intended.
Do not use these alpha-shade utility classes in v5.0.1.

The unnumbered `ecl-u-bg-alpha` class is valid. If a specific alpha shade is
needed, define a project class using the public EC variable instead:

```css
.app-bg-grey-alpha-300 {
  background-color: var(--ecl-color-grey-alpha-300) !important;
}

.app-bg-white-alpha-300 {
  background-color: var(--ecl-color-white-alpha-300) !important;
}
```

## Adaptive color-mode backgrounds

These 11 utilities read `--cm-*` variables and adapt to the active color mode:

- `ecl-u-bg-surface-lowest`
- `ecl-u-bg-surface-lowest-variant`
- `ecl-u-bg-surface-low-0`
- `ecl-u-bg-surface-low-1`
- `ecl-u-bg-surface-low-2`
- `ecl-u-bg-surface-medium-0`
- `ecl-u-bg-surface-medium-1`
- `ecl-u-bg-surface-0`
- `ecl-u-bg-surface-variant-1`
- `ecl-u-bg-surface-variant-2`
- `ecl-u-bg-on-surface-highlight`

Default values come from `ecl-ec.css`, so no color-mode class is required for
the default appearance.

To select another mode, apply one of the following classes to the element or
an ancestor:

- `ecl-color-mode--blue`
- `ecl-color-mode--green-dark`
- `ecl-color-mode--orange`
- `ecl-color-mode--green`
- `ecl-color-mode--purple`
- `ecl-color-mode--blue-navy`
- `ecl-color-mode--blue-electric`
- `ecl-color-mode--blue-ocean`
- `ecl-color-mode--green-lemon`
- `ecl-color-mode--green-pine`
- `ecl-color-mode--warm-grey`
- `ecl-color-mode--red-crayola`
- `ecl-color-mode--yellow-gold`
- `ecl-color-mode--purple-violet`
- `ecl-color-mode--red-tomato`

There is no `ecl-color-mode--default` or `ecl-color-mode--dark` class in the
v5.0.1 EC color-mode stylesheet. Omit the color-mode class to use the default.

### Color mode on the same element

```html
<section
  class="ecl-color-mode--blue ecl-u-bg-surface-0 ecl-u-type-color-on-surface-swap-0 ecl-u-pa-xl"
>
  This surface uses the blue mode and its corresponding on-surface text colour.
</section>
```

### Color mode inherited from an ancestor

```html
<div class="ecl-color-mode--green-dark">
  <section
    class="ecl-u-bg-surface-low-0 ecl-u-type-color-on-surface ecl-u-pa-xl"
  >
    The background and text variables are inherited from the green-dark mode.
  </section>
</div>
```

Color modes affect other ECL components and utilities inside their scope, not
only the element's background. Place the mode class at the narrowest container
that should inherit it. Call `guide("colours")` for the complete EC color-mode
palette.

## Fixed special values

| Class                  | Result                         |
| ---------------------- | ------------------------------ |
| `ecl-u-bg-transparent` | Transparent `background-color` |
| `ecl-u-bg-white`       | `#fff`                         |
| `ecl-u-bg-black`       | `#000`                         |

`ecl-u-bg-transparent` affects only `background-color`; an existing
`background-image` remains visible.

## Accessibility and content

- A background utility does not select a matching foreground colour. Add an
  appropriate ECL typography colour utility and test the final combination in
  every color mode used.
- Maintain a contrast ratio of at least 4.5:1 for normal text and 3:1 for large
  text.
- Do not communicate status using `success`, `warning`, `error`, or `info`
  colour alone. Include visible text and, when useful, an icon.
- Color modes can change both surface and on-surface variables. Prefer the
  corresponding `ecl-u-type-color-on-surface*` utilities for adaptive content
  instead of assuming a fixed foreground remains legible.
- Background colours may be suppressed by browser or user print settings; do
  not make printed content depend on a background colour alone.

## Implementation notes

- Background utilities can be placed on any suitable HTML element and require
  no special DOM structure, ARIA attributes, IDs, or JavaScript hooks.
- All rules set only `background-color` and use `!important`.
- Do not combine multiple `ecl-u-bg-*` classes on one element. Their equal
  specificity makes the compiled source order decide which one wins.
- `ecl-u-bg-surface` is not a v5.0.1 class; use one of the 11 exact adaptive
  surface names listed above.
