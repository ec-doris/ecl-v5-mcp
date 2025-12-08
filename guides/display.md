# Display Utilities

The ECL Display utilities provide a set of CSS classes to control the `display` property of HTML elements, allowing for flexible layout and visibility management. These utilities are part of the ECL (European Commission Library) design system and follow consistent naming conventions.

## Overview

Display utilities help you change how elements are rendered on the page. Whether you need to hide elements, create flexible layouts, or control inline/block behavior, these classes offer a utility-first approach.

## Display Classes

The following classes control the display property:

| Class                  | Display Value  | Description                                       |
| ---------------------- | -------------- | ------------------------------------------------- |
| `ecl-u-d-block`        | `block`        | Elements are displayed as block-level elements.   |
| `ecl-u-d-inline`       | `inline`       | Elements are displayed as inline elements.        |
| `ecl-u-d-inline-block` | `inline-block` | Elements are displayed as inline-block elements.  |
| `ecl-u-d-flex`         | `flex`         | Elements are displayed as flex containers.        |
| `ecl-u-d-inline-flex`  | `inline-flex`  | Elements are displayed as inline flex containers. |
| `ecl-u-d-table`        | `table`        | Elements are displayed as table elements.         |
| `ecl-u-d-table-cell`   | `table-cell`   | Elements are displayed as table cells.            |
| `ecl-u-d-none`         | `none`         | Elements are not displayed (hidden).              |

## Box Sizing Classes

Control the box-sizing model:

| Class                      | Box Sizing Value | Description                                                       |
| -------------------------- | ---------------- | ----------------------------------------------------------------- |
| `ecl-u-box-sizing-content` | `content-box`    | Width and height include only the content, not padding or border. |
| `ecl-u-box-sizing-border`  | `border-box`     | Width and height include content, padding, and border.            |

## Usage Examples

### Basic Display Control

```html
<!-- Block display -->
<div class="ecl-u-d-block">This is a block element</div>

<!-- Inline display -->
<span class="ecl-u-d-inline">This is inline</span>

<!-- Hide an element -->
<div class="ecl-u-d-none">This content is hidden</div>
```

### Flexbox Layout

```html
<div class="ecl-u-d-flex">
  <div>Item 1</div>
  <div>Item 2</div>
  <div>Item 3</div>
</div>
```

### Box Sizing Example

```html
<div class="ecl-u-d-block ecl-u-box-sizing-border" style="width: 200px; padding: 20px; border: 5px solid black;">
  This div uses border-box sizing, so the total width is 200px including padding and border.
</div>
```

### Combined Example

Here's a practical example combining display and box-sizing classes:

```html
<div class="ecl-u-d-flex" style="background-color: #d9d9d9; padding: 0.5rem;">
  <div class="ecl-u-d-block ecl-u-box-sizing-border" style="background-color: #ebebeb; border: 2px solid #000; height: 5rem; margin: 0.5rem; padding: 0.5rem; width: 5rem;">
    Box 1
  </div>
  <div class="ecl-u-d-block ecl-u-box-sizing-border" style="background-color: #ebebeb; border: 2px solid #000; height: 5rem; margin: 0.5rem; padding: 0.5rem; width: 5rem;">
    Box 2
  </div>
  <div class="ecl-u-d-block ecl-u-box-sizing-border" style="background-color: #ebebeb; border: 2px solid #000; height: 5rem; margin: 0.5rem; padding: 0.5rem; width: 5rem;">
    Box 3
  </div>
</div>
```

## Notes

- These utilities are designed to be used with the ECL CSS framework.
- For responsive design, ECL provides breakpoint-specific variants (not shown in this basic example).
- Always consider accessibility when hiding elements; use `ecl-u-d-none` judiciously.
- The `ecl-u-d-flex` and `ecl-u-d-inline-flex` classes enable flexbox layouts, which can be further customized with additional flex utilities.

For more advanced layout techniques, combine these display utilities with other ECL utilities like spacing, positioning, and flexbox helpers.
