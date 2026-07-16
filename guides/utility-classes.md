# ECL Utility Class Index (EC preset, v5.0.1)

This is the cross-family index for the EC utility bundle. Use the focused guide
named in each section for the complete class contract, values, examples, and
known v5.0.1 defects.

## Required CSS

Load EC theme variables before the utilities:

```html
<link rel="stylesheet" href="assets/ecl-ec.css" />
<link rel="stylesheet" href="assets/ecl-ec-color-modes.css" />
<link rel="stylesheet" href="assets/ecl-ec-utilities.css" />
<link rel="stylesheet" href="assets/ecl-ec-print.css" media="print" />
```

Call `guide("assets")` for the complete asset setup. The screen utility bundle
contains 2,456 distinct `ecl-u-*` class names across 15 Sass utility packages.
The print bundle contains 1,764 because print spacing has a smaller token set
and print screen-only/page-break classes replace the screen bundle's
print-only class.

Most utility declarations use `!important`. HTML class order does not determine
CSS precedence; avoid applying competing utilities for the same property and
active breakpoint.

## Family inventory

| Family         | Screen classes | Responsive class names | Focused guide         |
| -------------- | -------------- | ---------------------- | --------------------- |
| Background     | 167            | No                     | `guide("background")` |
| Border         | 178            | No                     | `guide("border")`     |
| Clearfix       | 1              | No                     | `guide("clearfix")`   |
| Dimension      | 8              | No                     | `guide("dimension")`  |
| Disable scroll | 1              | No                     | This guide            |
| Display        | 47             | Yes                    | `guide("display")`    |
| Flex           | 190            | Yes                    | `guide("flex")`       |
| Float          | 3              | No                     | `guide("float")`      |
| Media          | 51             | Sizes only             | `guide("media")`      |
| Print display  | 1              | No                     | This guide            |
| Screen reader  | 1              | No                     | This guide            |
| Shadow         | 6              | No                     | `guide("shadow")`     |
| Spacing        | 1,575          | Yes                    | `guide("spacing")`    |
| Typography     | 221            | Built into type styles | `guide("typography")` |
| Z-index        | 6              | No                     | `guide("z-index")`    |

“Responsive class names” means an explicit breakpoint infix is available.
Semantic typography classes change at internal responsive rules but do not add
a breakpoint to their names.

## EC breakpoints

Explicit responsive display, flex, media-size, and spacing classes use:

| Infix | Minimum width |
| ----- | ------------- |
| none  | 0px           |
| `s`   | 480px         |
| `m`   | 768px         |
| `l`   | 996px         |
| `xl`  | 1140px        |

There is no EC `2xl` breakpoint or utility infix in v5.0.1. Rules are
mobile-first `min-width` rules and continue to larger viewports until
overridden.

## Layout utilities

### Display

Every value has base, `s`, `m`, `l`, and `xl` forms:

```text
ecl-u-d-{none|inline|inline-block|block|table|table-cell|flex|inline-flex|grid}
ecl-u-d-{s|m|l|xl}-{value}
```

The two non-responsive box-sizing classes are
`ecl-u-box-sizing-content` and `ecl-u-box-sizing-border`. Call
`guide("display")`.

### Flex

Every base family below also supports an infix immediately before its final
value:

```text
ecl-u-flex-{row|column|row-reverse|column-reverse}
ecl-u-flex-{wrap|nowrap|wrap-reverse}
ecl-u-justify-content-{start|end|center|between|around}
ecl-u-align-items-{start|end|center|baseline|stretch}
ecl-u-align-content-{start|end|center|between|around|stretch}
ecl-u-align-self-{auto|start|end|center|baseline|stretch}
ecl-u-order-{first|last|0}
ecl-u-flex-grow-{0|1}
ecl-u-flex-shrink-{0|1}
ecl-u-flex-basis-{100|auto}
```

Example infixed forms are `ecl-u-flex-m-row`,
`ecl-u-justify-content-l-between`, and `ecl-u-flex-grow-xl-1`. Flex utilities
do not set `display`; also use `ecl-u-d-flex` or `ecl-u-d-inline-flex`. Call
`guide("flex")`.

### Spacing

The grammar is:

```text
ecl-u-{m|p}{a|h|v|t|r|b|l}-{token}
ecl-u-{m|p}{a|h|v|t|r|b|l}-{s|m|l|xl}-{token}
```

All 21 tokens from `5xs` through `13xl` are generated. Margin also supports
`none` and `auto`; padding supports `none` but not `auto`. Horizontal and
one-sided utilities use logical inline/block properties, not physical left and
right. Call `guide("spacing")` for the token scale and exact repeated-letter
examples.

### Dimension

```text
ecl-u-width-{auto|100}
ecl-u-height-{auto|100}
ecl-u-max-height-{none|100}
ecl-u-max-width-{none|100}
```

The max-width pair sets inherited `--max-w`, not the CSS `max-width` property.
It affects only elements or descendants that consume that custom property. Call
`guide("dimension")`.

### Float and clearfix

```text
ecl-u-f-l
ecl-u-f-r
ecl-u-f-none
ecl-u-clearfix
```

Floats are physical, non-responsive directions. Put `ecl-u-clearfix` on a
parent that must contain floated children; it creates only an `::after` clear.
Call `guide("float")` and `guide("clearfix")`.

### Media

Media sizes support every breakpoint:

```text
ecl-u-media-{a|h|v}-{s|m}
ecl-u-media-{a|h|v}-{s|m|l|xl}-{s|m}
```

The four non-responsive ratio wrappers are `ecl-u-media-ratio-16-9`, `4-3`,
`3-2`, and `1-1`; descendants may use `ecl-u-media-content`. Sixteen additional
classes control background origin, position, repeat, and size. Call
`guide("media")` for exact names and ratio markup.

## Visual utilities

### Background and border

Fixed palette utility families are `primary`, `secondary`, `neutral`, `grey`,
`monochrome`, `info`, `success`, `error`, and `warning`. Each supports base and
13 numbered shades. Adaptive background `surface*` and border `border*`
utilities follow the current `ecl-color-mode--*` variables.

```text
ecl-u-bg-{family}[-{shade}]
ecl-u-border-color-{family}[-{shade}]
```

The numbered `grey-alpha` and `white-alpha` selectors exist but are broken in
v5.0.1 because they refer to undefined short custom properties. Do not use
them. Unnumbered `*-alpha` works. Call `guide("background")`, `guide("border")`,
and `guide("colours")` before choosing a foreground/background combination.

Border composition starts with one of:

```text
ecl-u-border-{all|top|right|bottom|left}
```

Then optionally use width `0|1|2|4|8`, style `solid|dashed|dotted`, radius
`0|2|4|8|12`, and a color. Border direction properties are logical despite the
class names. Color, width, and style modifiers apply globally to all sides.

### Shadow

The EC classes are exactly:

```text
ecl-u-shadow-none
ecl-u-shadow-{1|2|3|4|5}
```

EC has no inner or negative shadow utilities and no responsive forms. Call
`guide("shadow")`.

### Z-index

```text
ecl-u-z-highlight     1
ecl-u-z-navigation    10
ecl-u-z-dropdown      15
ecl-u-z-modal         50
ecl-u-z-overlay       100
ecl-u-z-max           9999
```

There are no `auto` or `zero` EC classes. A high value cannot escape an
ancestor stacking context. Call `guide("z-index")`.

## Typography utilities

Semantic families are:

```text
ecl-u-type-display
ecl-u-type-heading-{1..6}
ecl-u-type-paragraph
ecl-u-type-paragraph-{xs|s|m|l|xl|2xl}
ecl-u-type-paragraph-lead
ecl-u-type-microcopy-{2xs|xs|s|m}
```

The bundle also includes 15 lower-level `ecl-u-type-{size}` classes, 11 weight
classes, 161 colors, italic/case/decoration classes, three physical alignment
classes, one highlight, and three enhanced-block styles. Call
`guide("typography")`; call `guide("colours")` before using numbered alpha colors
or color modes.

## Accessibility and document utilities

### Screen-reader-only content

`ecl-u-sr-only` visually clips an element while keeping its text available to
assistive technologies:

```html
<span class="ecl-u-sr-only">Additional context for screen-reader users</span>
```

It applies zero border and padding, two clipping declarations, a 1px box,
-1px margin, hidden overflow, absolute positioning, nowrap, and a 1px width,
all with `!important`.

Do not use it as a substitute for `aria-hidden`, and do not put it on focusable
content: ECL v5.0.1 supplies no focus-reveal companion class. Hidden text should
clarify the same operation or content rather than give screen-reader users a
different experience.

### Disable scroll

`ecl-u-disablescroll` applies `overflow: hidden !important` to the element:

```html
<html class="ecl-u-disablescroll">
  ...
</html>
```

For page locking, apply it to the actual scrolling element used by the
application and remove it when the modal/overlay closes. The utility does not
manage focus, preserve scrollbar width, remember scroll position, or initialize
a component.

## Print utilities

The screen utility bundle contains:

```css
.ecl-u-print-only {
  display: none !important;
}
```

The dedicated print bundle instead contains:

```text
ecl-u-screen-only              display: none !important
ecl-u-break-before-{auto|avoid|page}
ecl-u-break-after-{auto|avoid|page}
ecl-u-break-inside-{auto|avoid}
```

The eight break declarations are not marked `!important`, and paged-media
support is best-effort; browsers may be unable to honor an avoid rule.

Important v5.0.1 integration detail: `ecl-ec-print.css` does not reset
`ecl-u-print-only`. If `ecl-ec-utilities.css` remains active during printing,
`ecl-u-print-only` remains hidden. When the screen/print visibility pair is
needed, scope the bundles to their intended media:

```html
<link rel="stylesheet" href="assets/ecl-ec-utilities.css" media="screen" />
<link rel="stylesheet" href="assets/ecl-ec-print.css" media="print" />
```

That also means screen utility declarations are replaced by the dedicated
print implementations during printing. Test the application's print output;
the print spacing scale is intentionally smaller than the screen scale.

## General rules

- Utilities never add semantic HTML, ARIA, IDs, component hooks, or JavaScript.
- Prefer a component's existing styles before overriding its internals.
- Responsive utilities use only `s`, `m`, `l`, and `xl`; do not invent Bootstrap
  `sm`, `md`, `lg`, `xxl`, or ECL `2xl` breakpoint infixes.
- Test logical-direction utilities in RTL and physical float, text-align, and
  media-position utilities deliberately.
- Test final color contrast and do not communicate state through color alone.
