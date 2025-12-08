# ECL Background Utilities Guide

## Overview

The ECL (European Commission Look & Feel) framework provides a set of utility classes for applying background colors to elements. These utilities allow you to quickly style backgrounds using predefined color palettes that ensure consistency across your application.

Background utilities follow the naming convention `ecl-u-bg-{color}`, where `{color}` is replaced with the desired color name.

## Usage

To apply a background color, add the appropriate class to your HTML element:

```html
<div class="ecl-u-bg-primary">This div has a primary background</div>
```

### Color Modes

For the EC system, you can also use color mode backgrounds that adapt to different themes. Combine background classes with color mode classes:

```html
<div class="ecl-u-bg-surface-0 ecl-color-mode--dark">This div adapts to dark mode</div>
```

## Available Colors

### EC System Colors

#### Regular Background Colors
- `ecl-u-bg-white`
- `ecl-u-bg-primary`
- `ecl-u-bg-secondary`
- `ecl-u-bg-neutral`
- `ecl-u-bg-grey`
- `ecl-u-bg-success`
- `ecl-u-bg-info`
- `ecl-u-bg-warning`
- `ecl-u-bg-error`

#### Color Mode Background Colors
These backgrounds work with color modes for adaptive theming:
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

### EU System Colors

For the EU system, the available background colors are:
- `ecl-u-bg-white`
- `ecl-u-bg-primary`
- `ecl-u-bg-secondary`
- `ecl-u-bg-dark`
- `ecl-u-bg-success`
- `ecl-u-bg-info`
- `ecl-u-bg-warning`
- `ecl-u-bg-error`

## Examples

### Basic Usage
```html
<div class="ecl-u-pa-xl ecl-u-border-all ecl-u-bg-white">
  <p>White background with padding and border</p>
</div>

<div class="ecl-u-pa-xl ecl-u-border-all ecl-u-bg-primary">
  <p>Primary background</p>
</div>
```

### With Color Modes (EC System)
```html
<div class="ecl-u-pa-xl ecl-u-border-all ecl-u-bg-surface-0 ecl-color-mode--default">
  <p>Surface background in default mode</p>
</div>

<div class="ecl-u-pa-xl ecl-u-border-all ecl-u-bg-surface-low-1 ecl-color-mode--dark">
  <p>Low surface background in dark mode</p>
</div>
```

## Notes

- Background utilities can be combined with other ECL utilities like padding (`ecl-u-pa-*`), borders (`ecl-u-border-*`), and text colors.
- For color mode backgrounds, ensure the appropriate color mode class is applied to the parent element or globally.
- These utilities are part of the ECL utility classes and should be used in conjunction with the ECL CSS framework.
