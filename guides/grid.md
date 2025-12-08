# ECL Grid System

The Europa Component Library (ECL) uses a responsive, mobile-first grid system based on Bootstrap v4's 12-column layout. This grid provides a flexible foundation for structuring web page layouts across different screen sizes.

## Overview

The ECL grid system consists of:
- **Containers** (`.ecl-container`): Center and constrain content width
- **Rows** (`.ecl-row`): Horizontal groups of columns that clear floats
- **Columns** (`.ecl-col-*`): Flexible content containers that span 1-12 columns

The grid is built with flexbox and uses percentage-based widths, making it fluid and responsive.

## Breakpoints

ECL defines 5 breakpoints with minimum width media queries:

| Breakpoint       | Minimum Width | Container Max Width | Class Prefix   |
| ---------------- | ------------- | ------------------- | -------------- |
| Extra Small (xs) | 0px           | 100%                | `.ecl-col-`    |
| Small (s)        | 480px         | 100%                | `.ecl-col-s-`  |
| Medium (m)       | 768px         | 100%                | `.ecl-col-m-`  |
| Large (l)        | 996px         | 100%                | `.ecl-col-l-`  |
| Extra Large (xl) | 1140px        | 1368px              | `.ecl-col-xl-` |

## Grid Columns

Columns are specified by the number of 12-column units they span. For example:
- `.ecl-col-6` spans 6 columns (50% width)
- `.ecl-col-4` spans 4 columns (33.33% width)
- `.ecl-col-12` spans all 12 columns (100% width)

### Responsive Classes

Apply different column spans at different breakpoints:

```html
<div class="ecl-col-12 ecl-col-m-6 ecl-col-l-4">
  <!-- Full width on mobile, half on medium, third on large -->
</div>
```

## Container

The `.ecl-container` class centers content and applies maximum widths:

```html
<div class="ecl-container">
  <!-- Content goes here -->
</div>
```

## Row

The `.ecl-row` class creates a horizontal group of columns:

```html
<div class="ecl-row">
  <div class="ecl-col-6">Column 1</div>
  <div class="ecl-col-6">Column 2</div>
</div>
```

## Gutters

Columns have horizontal padding (gutters) for spacing:

| Breakpoint | Gutter Size |
| ---------- | ----------- |
| xs, s      | 1rem        |
| m, l       | 1.5rem      |
| xl         | 2rem        |

### No Gutters

Remove gutters with `.ecl-no-gutters`:

```html
<div class="ecl-row ecl-no-gutters">
  <div class="ecl-col-6">No gutter column</div>
  <div class="ecl-col-6">No gutter column</div>
</div>
```

## Offsets

Offset columns to create space before them:

```html
<div class="ecl-row">
  <div class="ecl-col-4">Column 1</div>
  <div class="ecl-col-4 ecl-offset-4">Column 2 (offset by 4)</div>
</div>
```

Responsive offsets: `.ecl-offset-s-2`, `.ecl-offset-m-3`, etc.

## Push and Pull

Reorder columns visually (less common, use with caution):

```html
<div class="ecl-row">
  <div class="ecl-col-8 ecl-push-4">Content A</div>
  <div class="ecl-col-4 ecl-pull-8">Content B</div>
</div>
```

## Basic Example

```html
<div class="ecl-container">
  <div class="ecl-row">
    <div class="ecl-col-12 ecl-col-m-6">
      <p>Left column - full width on mobile, half on medium+</p>
    </div>
    <div class="ecl-col-12 ecl-col-m-6">
      <p>Right column - full width on mobile, half on medium+</p>
    </div>
  </div>
</div>
```

## Responsive Example

```html
<div class="ecl-container">
  <div class="ecl-row">
    <div class="ecl-col-12 ecl-col-s-6 ecl-col-l-3">
      <p>Column 1</p>
    </div>
    <div class="ecl-col-12 ecl-col-s-6 ecl-col-l-3">
      <p>Column 2</p>
    </div>
    <div class="ecl-col-12 ecl-col-s-6 ecl-col-l-3">
      <p>Column 3</p>
    </div>
    <div class="ecl-col-12 ecl-col-s-6 ecl-col-l-3">
      <p>Column 4</p>
    </div>
  </div>
</div>
```

## Best Practices

### Do's
- Always wrap columns in `.ecl-row`
- Always wrap rows in `.ecl-container`
- Use responsive classes to adapt layouts to different screen sizes
- Specify column spans explicitly (don't rely on auto-width)
- Use `.ecl-offset-*` classes for spacing instead of margins

### Don'ts
- Don't use margins for horizontal spacing between columns
- Don't nest containers unnecessarily
- Don't mix EC and EU grid classes on the same page
- Don't use push/pull for content that should be reordered in source

## Technical Details

- **Flexbox-based**: Uses CSS flexbox for layout
- **Percentage widths**: Column widths are calculated as percentages
- **Mobile-first**: Base classes apply to all sizes, responsive classes override
- **12-column system**: Maximum of 12 columns per row
- **Namespace**: All classes prefixed with `.ecl-` to avoid conflicts
- **Theme-aware**: Gutter sizes defined in theme variables

## Integration

The grid is included in ECL presets:
- `@ecl/preset-ec` - European Commission theme
- `@ecl/preset-eu` - European Union theme

Import the grid styles:

```scss
@use '@ecl/grid/grid';
```

Or include via preset CSS.</content>
<parameter name="filePath">/Users/brownrl/Herd/europa-component-library/docs/grid.md