# Dimension Utilities

The ECL Dimension utilities provide CSS classes to control the width, height, maximum width, and maximum height of HTML elements. These utilities are part of the ECL (European Commission Library) design system, offering a utility-first approach to sizing elements consistently across your application.

## Overview

Dimension utilities allow you to set specific dimensions or constraints on elements without writing custom CSS. They help maintain design consistency and responsiveness in ECL-based projects.

## Width and Height Classes

Control the width and height properties directly:

| Class               | Property | Value  | Description                                            |
| ------------------- | -------- | ------ | ------------------------------------------------------ |
| `ecl-u-width-auto`  | `width`  | `auto` | Element width is determined by its content or parent.  |
| `ecl-u-width-100`   | `width`  | `100%` | Element takes full width of its parent container.      |
| `ecl-u-height-auto` | `height` | `auto` | Element height is determined by its content or parent. |
| `ecl-u-height-100`  | `height` | `100%` | Element takes full height of its parent container.     |

## Max Width and Max Height Classes

Set maximum constraints on dimensions:

| Class                   | Property     | Value  | Description                                        |
| ----------------------- | ------------ | ------ | -------------------------------------------------- |
| `ecl-u-max-width-none`  | `max-width`  | `none` | No maximum width constraint.                       |
| `ecl-u-max-width-100`   | `max-width`  | `100%` | Element cannot exceed 100% of its parent's width.  |
| `ecl-u-max-height-none` | `max-height` | `none` | No maximum height constraint.                      |
| `ecl-u-max-height-100`  | `max-height` | `100%` | Element cannot exceed 100% of its parent's height. |

## Usage Examples

### Basic Width and Height Control

```html
<!-- Auto width and height -->
<div class="ecl-u-width-auto ecl-u-height-auto">
  This div sizes based on its content.
</div>

<!-- Full width, auto height -->
<div class="ecl-u-width-100 ecl-u-height-auto">
  This div spans the full width of its container.
</div>

<!-- Auto width, full height -->
<div class="ecl-u-width-auto ecl-u-height-100">
  This div takes the full height of its parent.
</div>

<!-- Full width and height -->
<div class="ecl-u-width-100 ecl-u-height-100">
  This div fills its entire parent container.
</div>
```

### Maximum Dimension Constraints

```html
<!-- Image with max-width constraint -->
<img src="example.jpg" alt="Example" class="ecl-u-max-width-100 ecl-u-max-height-none">

<!-- Container with height constraint -->
<div class="ecl-u-max-width-none ecl-u-max-height-100" style="overflow: auto;">
  Scrollable content that won't exceed parent height.
</div>
```

### Combined Example

Here's a practical example demonstrating both width/height and max-width/max-height utilities:

```html
<div style="background-color: #d9d9d9; border: 2px dashed #404040; height: 10rem; width: 10rem; font: normal normal 400 .875rem/1rem Arial,sans-serif;">
  <div style="background-color: #ebebeb; box-sizing: border-box; border: 2px solid #000; display: inline-block;" class="ecl-u-width-100 ecl-u-height-100">
    Content box (full width and height)
  </div>
</div>

<div style="background-color: #d9d9d9; border: 2px dashed #404040; height: 10rem; width: 10rem; font: normal normal 400 .875rem/1rem Arial,sans-serif; margin-top: 1rem;">
  <img
    src="https://inno-ecl.s3.amazonaws.com/media/examples/example-image-square.jpg"
    alt="example"
    style="width: 12rem; height: 12rem;"
    class="ecl-u-max-width-100 ecl-u-max-height-100"
  />
</div>
```

## Notes

- These utilities work best when combined with ECL's responsive breakpoint variants for different screen sizes.
- For more granular control, consider using custom CSS or additional ECL utilities.
- When using `ecl-u-max-width-100` or `ecl-u-max-height-100`, ensure the parent container has defined dimensions.
- The `auto` values allow elements to size naturally based on content, which is useful for flexible layouts.
- Always test dimension utilities across different devices and screen sizes to ensure proper responsiveness.

For advanced sizing needs, combine these utilities with ECL's spacing, display, and flexbox utilities to create complex, responsive layouts.
