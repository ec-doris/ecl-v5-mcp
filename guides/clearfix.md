# Clearfix Utilities

The ECL Clearfix utility provides a CSS class to clear floated elements within a container. This utility is part of the ECL (European Commission Library) design system, ensuring proper layout behavior when working with floated elements.

## Overview

The clearfix utility solves the common CSS issue where a container doesn't expand to contain its floated children. This can cause layout problems where content that should appear below the floats instead wraps around them. The ECL clearfix class provides a reliable, cross-browser solution using modern CSS techniques.

## Clearfix Class

| Class            | Description                                                                                  |
| ---------------- | -------------------------------------------------------------------------------------------- |
| `ecl-u-clearfix` | Applies clearfix behavior to clear floated child elements and ensure proper container height |

## How It Works

The `ecl-u-clearfix` class uses CSS pseudo-elements (`::before` and `::after`) to create a clearing mechanism that:

1. Adds a `::before` pseudo-element that clears any previous floats
2. Adds an `::after` pseudo-element that clears the floats within the container
3. Ensures the container expands to contain all its floated children

## Usage Examples

### Basic Clearfix Usage

```html
<!-- Without clearfix - container collapses -->
<div style="background: #f0f0f0; padding: 1rem;">
  <div style="float: left; width: 100px; height: 100px; background: #blue;">Float left</div>
  <div style="float: right; width: 100px; height: 100px; background: #yellow;">Float right</div>
</div>
<p>This text might wrap around the floats instead of appearing below.</p>

<!-- With clearfix - container properly contains floats -->
<div class="ecl-u-clearfix" style="background: #f0f0f0; padding: 1rem;">
  <div style="float: left; width: 100px; height: 100px; background: #blue;">Float left</div>
  <div style="float: right; width: 100px; height: 100px; background: #yellow;">Float right</div>
</div>
<p>This text now appears below the container as expected.</p>
```

### Common Use Cases

```html
<!-- Two-column layout -->
<div class="ecl-u-clearfix">
  <div style="float: left; width: 50%;">Left column content</div>
  <div style="float: right; width: 50%;">Right column content</div>
</div>

<!-- Media object pattern -->
<div class="ecl-u-clearfix">
  <img src="image.jpg" alt="Media" style="float: left; margin-right: 1rem;">
  <div>Text content that flows beside the image</div>
</div>

<!-- Grid-like layout -->
<div class="ecl-u-clearfix">
  <div style="float: left; width: 33.333%;">Item 1</div>
  <div style="float: left; width: 33.333%;">Item 2</div>
  <div style="float: left; width: 33.333%;">Item 3</div>
</div>
```

### Combined Example

Here's a visual demonstration of the clearfix utility in action:

```html
<h2>Without clearfix</h2>
<div style="background-color: #d9d9d9; font: normal normal 400 .875rem/1rem Arial,sans-serif; padding: 0.5rem;">
  <div style="background-color: #BFD0E4; box-sizing: border-box; border: 2px solid #000; display: inline-block; float: left; padding: 0.5rem;">
    Float left box
  </div>
  <div style="background-color: #FFF4BB; box-sizing: border-box; border: 2px solid #000; display: inline-block; float: right; padding: 0.5rem;">
    Float right box
  </div>
</div>
<p>Text after (may wrap around floats)</p>

<h2>With clearfix</h2>
<div style="background-color: #d9d9d9; font: normal normal 400 .875rem/1rem Arial,sans-serif; padding: 0.5rem;" class="ecl-u-clearfix">
  <div style="background-color: #BFD0E4; box-sizing: border-box; border: 2px solid #000; display: inline-block; float: left; padding: 0.5rem;">
    Float left box
  </div>
  <div style="background-color: #FFF4BB; box-sizing: border-box; border: 2px solid #000; display: inline-block; float: right; padding: 0.5rem;">
    Float right box
  </div>
</div>
<p>Text after (properly positioned below)</p>
```

## Notes

- Apply `ecl-u-clearfix` to the parent container of floated elements
- The utility uses modern CSS techniques and is compatible with all supported browsers
- For new layouts, consider using flexbox or CSS Grid instead of floats, which don't require clearing
- Multiple floated elements within a clearfix container will be properly contained
- The clearfix only affects the container's height calculation, not the positioning of the floats themselves
- This utility is essential when working with legacy float-based layouts in ECL

The clearfix utility ensures robust layout behavior and prevents common float-related issues in ECL-based applications.
