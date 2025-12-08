# ECL Flexbox Utilities

The ECL (European Commission Look & Feel) provides a comprehensive set of responsive flexbox utilities for managing layout, alignment, and sizing of grid columns, navigation, components, and other elements.

## Overview

ECL's flexbox utilities are based on Bootstrap 5's flexbox system, offering the same powerful functionality with ECL-specific class naming conventions.

## Class Prefix

All flexbox utility classes in ECL are prefixed with `.ecl-u-` to ensure compatibility and avoid naming conflicts. For example:
- Bootstrap: `.d-flex`
- ECL: `.ecl-u-d-flex`

## Available Utilities

The ECL flexbox utilities include all standard Bootstrap 5 flexbox classes:

- **Display**: `.ecl-u-d-flex`, `.ecl-u-d-inline-flex`
- **Direction**: `.ecl-u-flex-row`, `.ecl-u-flex-column`, etc.
- **Justify Content**: `.ecl-u-justify-content-start`, `.ecl-u-justify-content-center`, etc.
- **Align Items**: `.ecl-u-align-items-start`, `.ecl-u-align-items-center`, etc.
- **Flex Wrap**: `.ecl-u-flex-wrap`, `.ecl-u-flex-nowrap`
- **Order**: `.ecl-u-order-1`, `.ecl-u-order-2`, etc.
- **Grow/Shrink**: `.ecl-u-flex-grow-1`, `.ecl-u-flex-shrink-0`

## Responsive Variants

All utilities support responsive breakpoints:
- `.ecl-u-d-flex` (default)
- `.ecl-u-d-s-flex` (small screens and up)
- `.ecl-u-d-m-flex` (medium screens and up)
- `.ecl-u-d-l-flex` (large screens and up)
- `.ecl-u-d-xl-flex` (extra large screens and up)

## Documentation

For detailed usage examples and complete class references, see the [Bootstrap 5 Flexbox Documentation](https://getbootstrap.com/docs/5.3/utilities/flex/).