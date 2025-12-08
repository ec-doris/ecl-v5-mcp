
# ECL Utility Classes (EC System)

This document provides a comprehensive list of all ECL utility classes that start with `ecl-u-`. These utilities are designed for the Europa Component Library (ECL) EC system and help with styling, layout, and accessibility without writing custom CSS.

## Spacing Utilities

Control margins and padding with responsive breakpoints.

### Margin (all directions):

- `ecl-u-ma-{size}` (e.g., `ecl-u-ma-5xs`, `ecl-u-ma-xs`, `ecl-u-ma-m`, `ecl-u-ma-xl`, up to `ecl-u-ma-13xl`)
- `ecl-u-ma-none`, `ecl-u-ma-auto`

### Margin (horizontal/vertical):

- `ecl-u-mh-{size}`, `ecl-u-mv-{size}` (same sizes as above)
- `ecl-u-mh-none`, `ecl-u-mv-none`, `ecl-u-mh-auto`, `ecl-u-mv-auto`

### Margin (individual sides):

- `ecl-u-mt-{size}`, `ecl-u-mr-{size}`, `ecl-u-mb-{size}`, `ecl-u-ml-{size}` (same sizes)
- `ecl-u-mt-none`, `ecl-u-mr-none`, `ecl-u-mb-none`, `ecl-u-ml-none`, `ecl-u-mt-auto`, `ecl-u-mr-auto`, `ecl-u-mb-auto`, `ecl-u-ml-auto`

### Padding (all directions):

- `ecl-u-pa-{size}` (same sizes as margin)
- `ecl-u-pa-none`

### Padding (horizontal/vertical):

- `ecl-u-ph-{size}`, `ecl-u-pv-{size}` (same sizes)
- `ecl-u-ph-none`, `ecl-u-pv-none`

### Padding (individual sides):

- `ecl-u-pt-{size}`, `ecl-u-pr-{size}`, `ecl-u-pb-{size}`, `ecl-u-pl-{size}` (same sizes)
- `ecl-u-pt-none`, `ecl-u-pr-none`, `ecl-u-pb-none`, `ecl-u-pl-none`

**Responsive variants:** Add breakpoint infix before size, e.g., `ecl-u-ma-m-l` (margin all large on medium+ screens). Breakpoints: `s`, `m`, `l`, `xl`, `2xl`.

## Typography Utilities

Control text appearance, alignment, and styling.

### Headings and text sizes:

- `ecl-u-type-display`
- `ecl-u-type-heading-1` to `ecl-u-type-heading-6`
- `ecl-u-type-paragraph`
- `ecl-u-type-paragraph-lead`
- `ecl-u-type-paragraph-{size}` (sizes from theme: typically `m`, `l`, `xl`)
- `ecl-u-type-microcopy-{size}` (sizes from theme: typically `m`, `s`, `xs`, `2xs`)

### Text colors:

- `ecl-u-type-color-{color}` where {color} includes:
  - Standard colors: `primary`, `secondary`, `neutral`, `grey`, `monochrome`, `info`, `success`, `error`, `warning`
  - Specific shades: `primary-600`, `secondary-500`, etc. (from color palette)
  - Color modes: `on-surface`, `on-surface-1`, `on-surface-2`, `on-surface-3`, `on-surface-swap-0`, `on-surface-swap-1`
  - Special: `black`, `white`

### Font weights:

- `ecl-u-type-weight-{weight}` (weights from theme: typically `regular`, `bold`, `light`, etc.)

### Text styles:

- `ecl-u-type-italic`
- `ecl-u-type-capitalize`
- `ecl-u-type-lowercase`
- `ecl-u-type-uppercase`
- `ecl-u-type-overline`
- `ecl-u-type-underline`
- `ecl-u-type-strike`
- `ecl-u-type-none`

### Text alignment:

- `ecl-u-type-align-left`
- `ecl-u-type-align-center`
- `ecl-u-type-align-right`

### Text highlights and enhances:

- `ecl-u-type-highlight`
- `ecl-u-type-enhance`
- `ecl-u-type-enhance-strong`
- `ecl-u-type-enhance-light`

## Display Utilities

Control element display properties.

### Display types (responsive):

- `ecl-u-d{infix}-{type}` where {infix} is breakpoint (`s`, `m`, `l`, `xl`, `2xl`) and {type} is: `none`, `inline`, `inline-block`, `block`, `table`, `table-cell`, `flex`, `inline-flex`, `grid`

### Box sizing:

- `ecl-u-box-sizing-content`
- `ecl-u-box-sizing-border`

## Flex Utilities

Control flexbox layout (responsive).

### Flex direction:

- `ecl-u-flex{infix}-{direction}` ({direction}: `row`, `column`, `row-reverse`, `column-reverse`)

### Flex wrap:

- `ecl-u-flex{infix}-{wrap}` ({wrap}: `wrap`, `nowrap`, `wrap-reverse`)

### Justify content:

- `ecl-u-justify-content{infix}-{value}` ({value}: `start`, `end`, `center`, `between`, `around`)

### Align items:

- `ecl-u-align-items{infix}-{value}` ({value}: `start`, `end`, `center`, `baseline`, `stretch`)

### Align content:

- `ecl-u-align-content{infix}-{value}` ({value}: `start`, `end`, `center`, `between`, `around`, `stretch`)

### Align self:

- `ecl-u-align-self{infix}-{value}` ({value}: `auto`, `start`, `end`, `center`, `baseline`, `stretch`)

### Order:

- `ecl-u-order{infix}-{value}` ({value}: `first`, `last`, `0`)

### Flex grow/shrink:

- `ecl-u-flex-grow{infix}-{value}` ({value}: `0`, `1`)
- `ecl-u-flex-shrink{infix}-{value}` ({value}: `0`, `1`)

### Flex basis:

- `ecl-u-flex-basis{infix}-{value}` ({value}: `100`, `auto`)

## Dimension Utilities

Control width and height.

- `ecl-u-width-100`
- `ecl-u-width-auto`
- `ecl-u-height-100`
- `ecl-u-height-auto`
- `ecl-u-max-width-100`
- `ecl-u-max-width-none`
- `ecl-u-max-height-100`
- `ecl-u-max-height-none`

## Border Utilities

Control borders, colors, widths, styles, and radius.

### Border sides:

- `ecl-u-border-all`
- `ecl-u-border-top`
- `ecl-u-border-bottom`
- `ecl-u-border-left`
- `ecl-u-border-right`

### Border colors:

- `ecl-u-border-color-{color}` (same color options as typography colors, plus `transparent`, `black`, `white`, and color mode borders like `border-low`, `border-medium`, `border`, `border-high`)

### Border widths:

- `ecl-u-border-width-0`
- `ecl-u-border-width-1`
- `ecl-u-border-width-2`
- `ecl-u-border-width-4`
- `ecl-u-border-width-8`

### Border styles:

- `ecl-u-border-style-solid`
- `ecl-u-border-style-dashed`
- `ecl-u-border-style-dotted`

### Border radius:

- `ecl-u-border-radius-0`
- `ecl-u-border-radius-2`
- `ecl-u-border-radius-4`
- `ecl-u-border-radius-8`
- `ecl-u-border-radius-12`

## Background Utilities

Control background colors.

- `ecl-u-bg-{color}` (same color options as border colors, plus surface variants like `surface-lowest`, `surface-0`, etc.)

## Shadow Utilities

Control box shadows.

- `ecl-u-shadow-none`
- `ecl-u-shadow-{key}` (keys from shadow map: typically `s`, `m`, `l`, etc.)
- `ecl-u-shadow-inner-{key}` (inner shadows)
- `ecl-u-shadow-negative-{key}` (negative shadows)
- `ecl-u-shadow-negative-inner-{key}` (negative inner shadows)

## Z-Index Utilities

Control stacking order.

- `ecl-u-z-{key}` (keys from z-index map: typically `auto`, `dropdown`, `sticky`, `fixed`, `modal`, `popover`, `tooltip`)

## Media Utilities

Control media sizing, ratios, and background properties.

### Media sizing (responsive):

- `ecl-u-media-a{infix}-{size}` (square dimensions)
- `ecl-u-media-h{infix}-{size}` (width only)
- `ecl-u-media-v{infix}-{size}` (height only)
- `ecl-u-media-content` (content positioning)

### Aspect ratios:

- `ecl-u-media-ratio-16-9`
- `ecl-u-media-ratio-4-3`
- `ecl-u-media-ratio-3-2`
- `ecl-u-media-ratio-1-1`

### Background properties:

- `ecl-u-media-bg-origin-border`
- `ecl-u-media-bg-origin-padding`
- `ecl-u-media-bg-origin-content`
- `ecl-u-media-bg-position-initial`
- `ecl-u-media-bg-position-top`
- `ecl-u-media-bg-position-bottom`
- `ecl-u-media-bg-position-left`
- `ecl-u-media-bg-position-right`
- `ecl-u-media-bg-position-center`
- `ecl-u-media-bg-repeat-all`
- `ecl-u-media-bg-repeat-x`
- `ecl-u-media-bg-repeat-y`
- `ecl-u-media-bg-repeat-none`
- `ecl-u-media-bg-size-auto`
- `ecl-u-media-bg-size-contain`
- `ecl-u-media-bg-size-cover`

## Float Utilities

Control element floating.

- `ecl-u-f-l` (float left)
- `ecl-u-f-r` (float right)
- `ecl-u-f-none` (no float)

## Screen Reader Utilities

Control screen reader visibility.

- `ecl-u-sr-only`

## Clearfix Utilities

Clear floats.

- `ecl-u-clearfix::after`

## Disable Scroll Utilities

Prevent scrolling.

- `ecl-u-disablescroll`

## Print Utilities

Control print-specific display and page breaks.

- `ecl-u-print-only`
- `ecl-u-screen-only`
- `ecl-u-break-before-auto`
- `ecl-u-break-before-avoid`
- `ecl-u-break-before-page`
- `ecl-u-break-after-auto`
- `ecl-u-break-after-avoid`
- `ecl-u-break-after-page`
- `ecl-u-break-inside-auto`
- `ecl-u-break-inside-avoid`

## Notes

- Many utilities are generated dynamically based on EC theme configurations.
- Responsive utilities use breakpoint infixes (e.g., `s`, `m`, `l`, `xl`, `2xl`) to apply styles only on screens larger than the specified breakpoint.
- All utilities use `!important` to ensure they override component styles when needed.
- For the most up-to-date list, refer to the ECL documentation or source code.
