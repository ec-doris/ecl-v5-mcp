# ECL Border Utilities (EC preset, v5.0.1)

Border utilities can create a border and independently control its colour,
width, style, and corner radius. All declarations use `!important`, so apply
them deliberately and avoid competing `!important` rules.

## Required CSS

Load the EC theme variables, optional color modes, and utilities:

```html
<link rel="stylesheet" href="assets/ecl-ec.css" />
<link rel="stylesheet" href="assets/ecl-ec-color-modes.css" />
<link rel="stylesheet" href="assets/ecl-ec-utilities.css" />
```

Call `guide("assets")` for the complete asset setup. The border utility rules
are in `ecl-ec-utilities.css`, not `ecl-ec.css`; `ecl-ec.css` supplies their
default colour variables, and `ecl-ec-color-modes.css` supplies the 15 optional
color-mode overrides. The rules are also present in `ecl-ec-print.css`. No
JavaScript is required.

When compiling ECL from Sass packages instead, pass the EC theme to the border
utility:

```scss
@use "@ecl/theme-ec/theme" as theme;
@use "@ecl/utility-border/border" with (
  $theme: theme.$theme
);
```

Without the theme parameter, the Sass source still emits the direction, fixed
transparent/white/black colour, width, style, and radius utilities, but not the
EC palette or adaptive color-mode colours.

The utilities are not responsive; ECL v5.0.1 provides no breakpoint variants.

## Create the border first

Start with one or more direction utilities. Each creates a `1px solid #000`
border; colour and width classes then override that base.

| Class                 | Property created           |
| --------------------- | -------------------------- |
| `ecl-u-border-all`    | `border` on all four sides |
| `ecl-u-border-top`    | `border-block-start`       |
| `ecl-u-border-right`  | `border-inline-end`        |
| `ecl-u-border-bottom` | `border-block-end`         |
| `ecl-u-border-left`   | `border-inline-start`      |

The directional names are implemented with CSS logical properties:

- In the usual horizontal writing mode, top/bottom are block-start/block-end.
- In a left-to-right document, left/right are inline-start/inline-end.
- In a right-to-left document, `ecl-u-border-left` appears on the physical
  right and `ecl-u-border-right` appears on the physical left.

Combine directional classes when only selected sides are needed:

```html
<div
  class="ecl-u-border-top ecl-u-border-bottom ecl-u-border-color-primary ecl-u-border-width-2"
>
  Logical top and bottom borders
</div>
```

Do not combine `ecl-u-border-all` with the individual direction classes.

Colour or width utilities alone do not make a border visible when the element's
border style is still `none`. Starting with a direction class gives a
predictable base.

## Border widths

Width utilities set `border-width` on all four sides:

| Class                  | CSS value   | Approximate pixels at a 16px root |
| ---------------------- | ----------- | --------------------------------- |
| `ecl-u-border-width-0` | `0`         | 0px                               |
| `ecl-u-border-width-1` | `0.0625rem` | 1px                               |
| `ecl-u-border-width-2` | `0.125rem`  | 2px                               |
| `ecl-u-border-width-4` | `0.25rem`   | 4px                               |
| `ecl-u-border-width-8` | `0.5rem`    | 8px                               |

The non-zero utilities use `rem`, so their physical size follows the document
root font size. `ecl-u-border-width-0` is useful for cancelling an existing
border without changing its stored colour or style.

## Border styles

| Class                       | CSS value              |
| --------------------------- | ---------------------- |
| `ecl-u-border-style-solid`  | `border-style: solid`  |
| `ecl-u-border-style-dashed` | `border-style: dashed` |
| `ecl-u-border-style-dotted` | `border-style: dotted` |

These utilities set the style on **all four sides**. Use them safely with
`ecl-u-border-all`:

```html
<div
  class="ecl-u-border-all ecl-u-border-style-dashed ecl-u-border-color-secondary ecl-u-border-width-2"
>
  Dashed border on all sides
</div>
```

Do not combine a one-side direction utility with a global style utility when
only one visible side is intended. For example,
`ecl-u-border-bottom ecl-u-border-style-dashed` gives every side a non-`none`
style, which can make all four sides visible. ECL v5.0.1 has no side-specific
border-style utility; use a project rule such as
`border-block-end-style: dashed !important` when that shape is required.

## Border radius

Radius utilities are independent of border direction and apply to all corners:

| Class                    | CSS value  | Approximate pixels at a 16px root |
| ------------------------ | ---------- | --------------------------------- |
| `ecl-u-border-radius-0`  | `0`        | 0px                               |
| `ecl-u-border-radius-2`  | `0.125rem` | 2px                               |
| `ecl-u-border-radius-4`  | `0.25rem`  | 4px                               |
| `ecl-u-border-radius-8`  | `0.5rem`   | 8px                               |
| `ecl-u-border-radius-12` | `0.75rem`  | 12px                              |

`ecl-u-border-radius-0` cancels existing rounding. Border radius also affects
how the element's own background is painted, even when no visible border is
present. It does not by itself clip overflowing child content.

## Semantic border colours

Semantic aliases resolve through EC custom properties. Their v5.0.1 default
palette equivalents are:

| Class                           | Default equivalent |
| ------------------------------- | ------------------ |
| `ecl-u-border-color-primary`    | `primary-600`      |
| `ecl-u-border-color-secondary`  | `secondary-400`    |
| `ecl-u-border-color-neutral`    | `neutral-600`      |
| `ecl-u-border-color-grey`       | `grey-950`         |
| `ecl-u-border-color-alpha`      | `grey-alpha-950`   |
| `ecl-u-border-color-monochrome` | `monochrome-500`   |
| `ecl-u-border-color-info`       | `info-600`         |
| `ecl-u-border-color-success`    | `success-700`      |
| `ecl-u-border-color-error`      | `error-600`        |
| `ecl-u-border-color-warning`    | `warning-500`      |

These semantic palette aliases do not change when an
`ecl-color-mode--*` class is applied. Use the adaptive border colours described
below when the border must respond to a color mode.

## Numbered palette colours

The class format is:

```text
ecl-u-border-color-{family}-{shade}
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

Example:

```html
<div
  class="ecl-u-border-all ecl-u-border-color-primary-600 ecl-u-border-width-2 ecl-u-border-radius-4"
>
  Exact primary-600 border
</div>
```

Numbered shade classes are fixed palette colours and do not adapt to color
modes.

### Alpha-shade defect in v5.0.1

The compiled v5.0.1 CSS contains all 13 shade selectors for both
`ecl-u-border-color-grey-alpha-{shade}` and
`ecl-u-border-color-white-alpha-{shade}`, but their declarations reference the
undefined variables `--c-g-alpha` and `--c-w-alpha`. Browsers therefore cannot
use those declarations as intended. Do not use these alpha-shade utility
classes in v5.0.1.

The unnumbered `ecl-u-border-color-alpha` class is valid. If a specific alpha
shade is needed, define a project class using the public EC variable instead:

```css
.app-border-grey-alpha-300 {
  border-color: var(--ecl-color-grey-alpha-300) !important;
}

.app-border-white-alpha-300 {
  border-color: var(--ecl-color-white-alpha-300) !important;
}
```

## Adaptive color-mode border colours

These four utilities read `--cm-border*` variables and adapt to the active
color mode:

| Class                              | Default equivalent |
| ---------------------------------- | ------------------ |
| `ecl-u-border-color-border-low`    | `primary-300`      |
| `ecl-u-border-color-border-medium` | `primary-500`      |
| `ecl-u-border-color-border`        | `primary-600`      |
| `ecl-u-border-color-border-high`   | `primary-700`      |

Default values come from `ecl-ec.css`, so no color-mode class is required for
the default appearance.

To select another mode, apply one of the following classes to the bordered
element or an ancestor:

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

There is no `ecl-color-mode--default`, `ecl-color-mode--dark`, or
`ecl-color-mode--border-high` class in the v5.0.1 EC color-mode stylesheet.
Omit the color-mode class to use the default.

```html
<section class="ecl-color-mode--blue">
  <div
    class="ecl-u-border-all ecl-u-border-color-border-high ecl-u-border-width-2 ecl-u-border-radius-8"
  >
    Border-high from the blue color mode
  </div>
</section>
```

Color modes affect other ECL components and utilities inside their scope, not
only borders. Place the mode class at the narrowest container that should
inherit it. Call `guide("colours")` for the complete EC color-mode palette.

## Fixed special colours

| Class                            | Result                    |
| -------------------------------- | ------------------------- |
| `ecl-u-border-color-transparent` | Transparent border colour |
| `ecl-u-border-color-white`       | `#fff`                    |
| `ecl-u-border-color-black`       | `#000`                    |

A transparent border still occupies space when its width and style create a
border; only its colour is transparent.

## Practical combinations

### Default one-pixel black border

```html
<div class="ecl-u-border-all">Content</div>
```

### Customised complete border

```html
<div
  class="ecl-u-border-all ecl-u-border-color-primary ecl-u-border-width-4 ecl-u-border-radius-12"
>
  Primary semantic border
</div>
```

### Adaptive bottom border

```html
<div
  class="ecl-u-border-bottom ecl-u-border-color-border-medium ecl-u-border-width-2"
>
  A solid logical block-end border that adapts to the active color mode
</div>
```

## Accessibility and implementation notes

- Borders used to identify controls, focus, selection, errors, or other
  meaningful UI states should have at least 3:1 contrast against adjacent
  colours.
- Do not communicate `success`, `warning`, `error`, or `info` using border
  colour alone. Include visible text and, when useful, an icon.
- Do not remove or reduce a component's focus indicator unless an equally
  visible accessible replacement is provided.
- Border utilities can be placed on any suitable HTML element and require no
  special DOM structure, ARIA attributes, IDs, or JavaScript hooks.
- Colour, width, and style modifiers apply to all sides. ECL v5.0.1 has no
  side-specific modifier variants.
- Class order in the HTML attribute does not control precedence; the compiled
  stylesheet order does. Avoid conflicting utilities from the same group.
- `ecl-u-border-color-neutral-dark` appears in the tagged EC showcase but is
  not present in the v5.0.1 source or compiled CSS. Use a valid semantic,
  numbered, adaptive, or fixed colour class from this guide.
