# Border Utilities in ECL

The ECL (European Commission Look) design system provides a comprehensive set of utility classes for styling borders on elements. These utilities allow you to control border color, width, direction, and radius in a consistent and accessible way.

## Border Colors

ECL offers semantic border color utilities that adapt to different design systems and color modes:

### EC System Colors
- `ecl-u-border-color-primary` - Primary color border
- `ecl-u-border-color-secondary` - Secondary color border
- `ecl-u-border-color-neutral` - Neutral color border
- `ecl-u-border-color-grey` - Grey color border
- `ecl-u-border-color-success` - Success color border (green)
- `ecl-u-border-color-error` - Error color border (red)

### EU System Colors
- `ecl-u-border-color-primary` - Primary color border
- `ecl-u-border-color-secondary` - Secondary color border
- `ecl-u-border-color-dark` - Dark color border
- `ecl-u-border-color-success` - Success color border (green)
- `ecl-u-border-color-error` - Error color border (red)

## Border Widths

Control the thickness of borders with these width utilities:

- `ecl-u-border-width-1` - 1px border
- `ecl-u-border-width-2` - 2px border
- `ecl-u-border-width-4` - 4px border
- `ecl-u-border-width-8` - 8px border

## Border Directions

Apply borders to specific sides or all sides:

- `ecl-u-border-all` - Border on all sides
- `ecl-u-border-top` - Top border only
- `ecl-u-border-right` - Right border only
- `ecl-u-border-bottom` - Bottom border only
- `ecl-u-border-left` - Left border only

## Border Radius

Round the corners of elements with these radius utilities:

- `ecl-u-border-radius-2` - 2px border radius
- `ecl-u-border-radius-4` - 4px border radius
- `ecl-u-border-radius-8` - 8px border radius
- `ecl-u-border-radius-12` - 12px border radius

## Color Modes (EC System)

For the EC system, additional color mode borders are available when using color modes:

- `ecl-u-border-color-border-low` - Low contrast border
- `ecl-u-border-color-border-medium` - Medium contrast border
- `ecl-u-border-color-border` - Default border
- `ecl-u-border-color-border-high` - High contrast border

These are used in conjunction with color mode classes like `ecl-color-mode--border-low`.

## Usage Examples

### Basic Border
```html
<div class="ecl-u-border-all ecl-u-border-color-primary ecl-u-border-width-1">
  Content with a primary colored border
</div>
```

### Rounded Corners with Specific Sides
```html
<div class="ecl-u-border-bottom ecl-u-border-color-secondary ecl-u-border-width-2 ecl-u-border-radius-4">
  Content with bottom border and rounded corners
</div>
```

### Color Mode Border (EC System)
```html
<div class="ecl-color-mode--border-high ecl-u-border-color-border-high ecl-u-border-all ecl-u-border-width-1">
  High contrast border content
</div>
```

### Complete Example
```html
<div class="ecl-u-border-all ecl-u-border-color-success ecl-u-border-width-2 ecl-u-border-radius-8"
     style="height: 5rem; margin: 2rem auto; width: 10rem;">
  Success border with 2px width and 8px radius
</div>
```

These utilities provide a flexible and consistent way to style borders across ECL components, ensuring visual harmony and accessibility compliance.
