# Shadow Utilities

The ECL Shadow utilities provide CSS classes for adding box shadows and inner shadows to elements. These utilities are part of the ECL (European Commission Library) design system, offering consistent elevation and depth effects across your application.

## Overview

Shadow utilities help create visual hierarchy and depth in your UI by applying box-shadow effects. They support different elevation levels and can be combined with inner shadows for more complex visual effects. Note that available options may vary between ECL systems (EC vs. EU).

## Box Shadow Classes

Apply outer shadows to create elevation effects:

### EC System
| Class               | Elevation | Description                              |
| ------------------- | --------- | ---------------------------------------- |
| `ecl-u-shadow-none` | None      | No shadow                                |
| `ecl-u-shadow-1`    | 1         | Subtle shadow for slight elevation       |
| `ecl-u-shadow-2`    | 2         | Moderate shadow for cards and panels     |
| `ecl-u-shadow-3`    | 3         | Stronger shadow for floating elements    |
| `ecl-u-shadow-4`    | 4         | Prominent shadow for modals and overlays |
| `ecl-u-shadow-5`    | 5         | Maximum shadow for emphasis              |

### EU System
| Class                     | Elevation  | Description                           |
| ------------------------- | ---------- | ------------------------------------- |
| `ecl-u-shadow-none`       | None       | No shadow                             |
| `ecl-u-shadow-1`          | 1          | Subtle shadow for slight elevation    |
| `ecl-u-shadow-2`          | 2          | Moderate shadow for cards and panels  |
| `ecl-u-shadow-3`          | 3          | Stronger shadow for floating elements |
| `ecl-u-shadow-negative-1` | Negative 1 | Inset shadow for subtle depth         |
| `ecl-u-shadow-negative-2` | Negative 2 | Moderate inset shadow                 |
| `ecl-u-shadow-negative-3` | Negative 3 | Strong inset shadow                   |

## Inner Shadow Classes (EU System Only)

Apply inner shadows for inset depth effects:

| Class                           | Depth      | Description                 |
| ------------------------------- | ---------- | --------------------------- |
| `ecl-u-shadow-none`             | None       | No inner shadow             |
| `ecl-u-shadow-inner-1`          | 1          | Subtle inner shadow         |
| `ecl-u-shadow-inner-2`          | 2          | Moderate inner shadow       |
| `ecl-u-shadow-negative-inner-1` | Negative 1 | Subtle inset inner shadow   |
| `ecl-u-shadow-negative-inner-2` | Negative 2 | Moderate inset inner shadow |

## Usage Examples

### Basic Box Shadows

```html
<!-- No shadow -->
<div class="ecl-u-shadow-none">No elevation</div>

<!-- Subtle elevation -->
<div class="ecl-u-shadow-1">Slightly elevated</div>

<!-- Moderate elevation -->
<div class="ecl-u-shadow-2">Card-like elevation</div>

<!-- Strong elevation -->
<div class="ecl-u-shadow-3">Floating element</div>
```

### Advanced Shadows (EU System)

```html
<!-- Inset shadow -->
<div class="ecl-u-shadow-negative-1">Inset effect</div>

<!-- Combined outer and inner shadows -->
<div class="ecl-u-shadow-2 ecl-u-shadow-inner-1">
  <div>Complex shadow effect</div>
</div>
```

### Practical Examples

```html
<!-- Card component -->
<div class="ecl-u-shadow-2" style="padding: 1rem; background: white; border-radius: 4px;">
  <h3>Card Title</h3>
  <p>Card content with elevation.</p>
</div>

<!-- Modal overlay -->
<div class="ecl-u-shadow-4" style="position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); background: white; padding: 2rem; border-radius: 8px;">
  <h2>Modal Title</h2>
  <p>Modal content with strong shadow.</p>
</div>

<!-- Button with depth (EU System) -->
<button class="ecl-u-shadow-1 ecl-u-shadow-inner-1" style="padding: 0.5rem 1rem; border: none; border-radius: 4px; background: #007acc; color: white;">
  Pressed Button Effect
</button>
```

### Combined Example

Here's a demonstration of shadow utilities in action:

```html
<!-- EC System Example -->
<div style="display: flex; align-items: center; justify-content: center; padding: 2rem 0;">
  <div style="background-color: #ebebeb; height: 5rem; outline: 10px solid #fff; outline-offset: -10px; width: 10rem;" class="ecl-u-shadow-3">
  </div>
</div>

<!-- EU System Example -->
<div style="display: flex; align-items: center; justify-content: center; padding: 2rem 0; background-color: #808080;">
  <div style="height: 5rem; width: 10rem;" class="ecl-u-shadow-negative-2">
    <div style="background-color: #404040; height: 100%; width: 100%;" class="ecl-u-shadow-negative-inner-1"></div>
  </div>
</div>
```

## Notes

- Shadow availability depends on your ECL system (EC or EU). Check your system configuration.
- Inner shadows are only available in the EU system.
- Negative shadows create inset effects, useful for pressed buttons or recessed elements.
- Combine multiple shadow classes for complex visual effects, but use sparingly to maintain design consistency.
- For responsive designs, ECL provides breakpoint-specific shadow variants.
- Always consider performance impact when using shadows on many elements, especially on mobile devices.
- Shadows work best on elements with background colors or borders to provide contrast.

These utilities help create visual hierarchy and modern UI effects while maintaining consistency across ECL-based applications.
