# ECL Colours (EC preset, v5.0.1)

ECL EC has two related colour systems:

1. **Fixed palette tokens** such as `--ecl-color-primary-600`. Their values do
   not change when a color mode is applied.
2. **Adaptive semantic tokens** such as `--cm-surface-0`,
   `--cm-on-surface-swap-0`, and `--cm-border`. Their values can be overridden
   by an `ecl-color-mode--*` class and inherited by its descendants.

Use fixed palette values when an exact EC colour is required. Prefer adaptive
surface, on-surface, and border tokens when a component or region must respond
to a color mode.

## Required CSS

Load the stylesheets in this order:

```html
<link rel="stylesheet" href="assets/ecl-ec.css" />
<link rel="stylesheet" href="assets/ecl-ec-color-modes.css" />
<link rel="stylesheet" href="assets/ecl-ec-utilities.css" />
```

- `ecl-ec.css` defines the fixed palette and default adaptive tokens.
- `ecl-ec-color-modes.css` defines the 15 optional mode classes.
- `ecl-ec-utilities.css` provides background, text-colour, and border-colour
  utility classes.

Keep `ecl-ec-color-modes.css` after `ecl-ec.css`, especially when a mode class
is placed on the root `html` element. Call `guide("assets")` for the complete
asset setup. No JavaScript is required for colours or color modes.

## Fixed EC palette

The public custom-property format is:

```text
--ecl-color-{family}-{shade}
```

ECL also defines short aliases such as `--c-p-600`, but the source labels those
as internal aliases. Use the public `--ecl-color-*` properties in project CSS.

All opaque families use these 13 shades:

```text
25, 50, 75, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950
```

Lower numbers are generally lighter and higher numbers darker. Choose colours
by semantic purpose and verified contrast, not by shade number alone.

### Main and neutral palette values

| Shade | Primary   | Secondary | Neutral   | Grey      | Monochrome |
| ----- | --------- | --------- | --------- | --------- | ---------- |
| 25    | `#f7f9ff` | `#fffcf7` | `#f9fafd` | `#fafafb` | `#fbfbfb`  |
| 50    | `#f2f6ff` | `#fff5e5` | `#eceff9` | `#f6f6f8` | `#f7f7f7`  |
| 75    | `#eef2ff` | `#ffebcc` | `#d1d9f1` | `#ededf0` | `#efefef`  |
| 100   | `#e6edff` | `#ffe1b4` | `#c1ccec` | `#e1e1e7` | `#e4e4e4`  |
| 200   | `#d9e3ff` | `#ffd392` | `#b0bde6` | `#d4d4dc` | `#d8d8d8`  |
| 300   | `#b0c6ff` | `#ffcb7d` | `#9eaee1` | `#b9b9c5` | `#bfbfbf`  |
| 400   | `#8cacff` | `#ffbe5c` | `#8ea1dc` | `#a0a0b1` | `#a9a9a9`  |
| 500   | `#5987ff` | `#fea439` | `#7c92d6` | `#84849b` | `#909090`  |
| 600   | `#0046ff` | `#fc8713` | `#6c85d1` | `#696984` | `#777777`  |
| 700   | `#0035bf` | `#ed6c09` | `#51649d` | `#505070` | `#606060`  |
| 800   | `#002a99` | `#c55109` | `#41507d` | `#353559` | `#474747`  |
| 900   | `#001f73` | `#9e4107` | `#313c5e` | `#1c1c45` | `#313131`  |
| 950   | `#001959` | `#763105` | `#26324b` | `#00002e` | `#171717`  |

Family names are `primary`, `secondary`, `neutral`, `grey`, and `monochrome`.
For example, Primary 600 is `var(--ecl-color-primary-600)`.

### Status palette values

| Shade | Info      | Success   | Error     | Warning   |
| ----- | --------- | --------- | --------- | --------- |
| 25    | `#f9fbfd` | `#f9fefc` | `#fefafa` | `#fffaf5` |
| 50    | `#f5f7fb` | `#edfbf6` | `#fdefef` | `#fff3e8` |
| 75    | `#ebeff7` | `#e3f9f0` | `#fce9ea` | `#ffeddc` |
| 100   | `#dee4f2` | `#daf6eb` | `#f5bbbe` | `#ffdbba` |
| 200   | `#bfcce6` | `#b2edd6` | `#f09a9e` | `#ffc998` |
| 300   | `#a3b6da` | `#8fe5c4` | `#ea6c72` | `#ffb16a` |
| 400   | `#859dce` | `#5ddaa9` | `#e54f57` | `#ffa14d` |
| 500   | `#6685c2` | `#05c67b` | `#df232d` | `#ff8a20` |
| 600   | `#3b62b0` | `#05b26f` | `#cb2029` | `#e87e1d` |
| 700   | `#1c49a4` | `#049e62` | `#9e1920` | `#ba6517` |
| 800   | `#003399` | `#037e4e` | `#7b1319` | `#8b4c11` |
| 900   | `#00297a` | `#025f3b` | `#5a0e12` | `#68390d` |
| 950   | `#001f5c` | `#02472c` | `#1f0506` | `#512c0a` |

Family names are `info`, `success`, `error`, and `warning`.

### Alpha palettes

Grey-alpha mixes `#00002e` with transparency. White-alpha mixes `#fff` with
transparency. The result blends with whatever is behind it.

| Shade | Grey-alpha                                      | White-alpha                                  |
| ----- | ----------------------------------------------- | -------------------------------------------- |
| 25    | `color-mix(in srgb, #00002e 2.5%, transparent)` | `color-mix(in srgb, #fff 2.5%, transparent)` |
| 50    | `color-mix(in srgb, #00002e 5%, transparent)`   | `color-mix(in srgb, #fff 5%, transparent)`   |
| 75    | `color-mix(in srgb, #00002e 7.5%, transparent)` | `color-mix(in srgb, #fff 7.5%, transparent)` |
| 100   | `color-mix(in srgb, #00002e 10%, transparent)`  | `color-mix(in srgb, #fff 10%, transparent)`  |
| 200   | `color-mix(in srgb, #00002e 20%, transparent)`  | `color-mix(in srgb, #fff 15%, transparent)`  |
| 300   | `color-mix(in srgb, #00002e 30%, transparent)`  | `color-mix(in srgb, #fff 30%, transparent)`  |
| 400   | `color-mix(in srgb, #00002e 40%, transparent)`  | `color-mix(in srgb, #fff 40%, transparent)`  |
| 500   | `color-mix(in srgb, #00002e 50%, transparent)`  | `color-mix(in srgb, #fff 50%, transparent)`  |
| 600   | `color-mix(in srgb, #00002e 60%, transparent)`  | `color-mix(in srgb, #fff 60%, transparent)`  |
| 700   | `color-mix(in srgb, #00002e 72%, transparent)`  | `color-mix(in srgb, #fff 72%, transparent)`  |
| 800   | `color-mix(in srgb, #00002e 80%, transparent)`  | `color-mix(in srgb, #fff 80%, transparent)`  |
| 900   | `color-mix(in srgb, #00002e 90%, transparent)`  | `color-mix(in srgb, #fff 90%, transparent)`  |
| 950   | `color-mix(in srgb, #00002e 95%, transparent)`  | `color-mix(in srgb, #fff 95%, transparent)`  |

Use `--ecl-color-grey-alpha-{shade}` and
`--ecl-color-white-alpha-{shade}` in project CSS. The short internal aliases
are `--c-a-{shade}` and `--c-w-{shade}`.

### Unnumbered semantic aliases

| Public property           | Internal alias | v5.0.1 value              |
| ------------------------- | -------------- | ------------------------- |
| `--ecl-color-primary`     | `--c-p`        | Primary 600, `#0046ff`    |
| `--ecl-color-secondary`   | `--c-s`        | Secondary 400, `#ffbe5c`  |
| `--ecl-color-neutral`     | `--c-n`        | Neutral 600, `#6c85d1`    |
| `--ecl-color-grey`        | `--c-g`        | Grey 950, `#00002e`       |
| `--ecl-color-grey-alpha`  | `--c-a`        | Grey-alpha 950            |
| `--ecl-color-white-alpha` | `--c-w`        | White-alpha 600           |
| `--ecl-color-monochrome`  | `--c-m`        | Monochrome 500, `#909090` |
| `--ecl-color-info`        | `--c-in`       | Info 600, `#3b62b0`       |
| `--ecl-color-success`     | `--c-su`       | Success 700, `#049e62`    |
| `--ecl-color-error`       | `--c-er`       | Error 600, `#cb2029`      |
| `--ecl-color-warning`     | `--c-wa`       | Warning 500, `#ff8a20`    |

The theme also exposes:

```css
--ecl-color-corporate-gradient: linear-gradient(
  90deg,
  #155dfc 0%,
  #1447e6 50%,
  #010492 100%
);
```

The supplementary families used to build color modes—such as `blue-ocean`,
`green-lemon`, and `red-tomato`—are Sass palette entries, not public fixed
custom properties or utility families. Do not invent classes such as
`ecl-u-bg-blue-ocean-500`.

## Using fixed palette values

In custom CSS, use the public properties:

```css
.app-panel {
  background-color: var(--ecl-color-primary-50);
  border-color: var(--ecl-color-primary-300);
  color: var(--ecl-color-primary-800);
}
```

ECL also generates fixed palette utilities for backgrounds, borders, and text.
For their exact contracts and special values, call:

- `guide("background")`
- `guide("border")`
- `guide("typography")`

## Alpha utility defect in v5.0.1

The public alpha custom properties listed above are valid. However, the
v5.0.1 Sass utility generator incorrectly points numbered
`grey-alpha-{shade}` and `white-alpha-{shade}` background, border, and text
utilities to undefined variables such as `--c-g-alpha` and `--c-w-alpha`.

Do not use these numbered alpha utility classes in v5.0.1:

```text
ecl-u-bg-grey-alpha-{shade}
ecl-u-bg-white-alpha-{shade}
ecl-u-border-color-grey-alpha-{shade}
ecl-u-border-color-white-alpha-{shade}
ecl-u-type-color-grey-alpha-{shade}
ecl-u-type-color-white-alpha-{shade}
```

Use the public custom properties in a project class instead. The unnumbered
`ecl-u-bg-alpha`, `ecl-u-border-color-alpha`, and `ecl-u-type-color-alpha`
classes are valid.

## Adaptive color-mode tokens

Adaptive tokens are CSS custom properties beginning with `--cm-`. Their names
describe roles rather than fixed hues:

- **surface** tokens are for backgrounds;
- **on-surface** tokens are for text and content placed on surfaces;
- **border** tokens are for outlines, separators, and boundaries.

The default values are defined on `:root` in `ecl-ec.css`. A color-mode class
overrides a subset of them, and those overrides inherit through that class's
descendants.

### Core default surface tokens

| Token                         | Default value                   |
| ----------------------------- | ------------------------------- |
| `--cm-surface-lowest`         | Primary 50, `#f2f6ff`           |
| `--cm-surface-lowest-variant` | 50% `#f6f4f3` over transparency |
| `--cm-surface-low-0`          | Primary 50, `#f2f6ff`           |
| `--cm-surface-low-1`          | Primary 100, `#e6edff`          |
| `--cm-surface-low-2`          | Primary 200, `#d9e3ff`          |
| `--cm-surface-medium-0`       | Primary 200, `#d9e3ff`          |
| `--cm-surface-medium-1`       | Primary 300, `#b0c6ff`          |
| `--cm-surface-0`              | Grey 950, `#00002e`             |
| `--cm-surface-variant-1`      | `#e2dcda`                       |
| `--cm-surface-variant-2`      | Grey 950, `#00002e`             |

### Core default on-surface tokens

| Token                       | Default value            |
| --------------------------- | ------------------------ |
| `--cm-on-surface`           | Primary 600, `#0046ff`   |
| `--cm-on-surface-1`         | Secondary 400, `#ffbe5c` |
| `--cm-on-surface-2`         | Primary 300, `#b0c6ff`   |
| `--cm-on-surface-3`         | `#fff`                   |
| `--cm-on-surface-highlight` | Secondary 75, `#ffebcc`  |
| `--cm-on-surface-swap-0`    | `#fff`                   |
| `--cm-on-surface-swap-1`    | Grey 950, `#00002e`      |

### Core default border tokens

| Token                | Default value          |
| -------------------- | ---------------------- |
| `--cm-border-low`    | Primary 300, `#b0c6ff` |
| `--cm-border-medium` | Primary 500, `#5987ff` |
| `--cm-border`        | Primary 600, `#0046ff` |
| `--cm-border-high`   | Primary 700, `#0035bf` |

## Available color modes

Apply one mode class to the region that should inherit it:

- `ecl-color-mode--blue`
- `ecl-color-mode--green-dark`
- `ecl-color-mode--orange`
- `ecl-color-mode--green`
- `ecl-color-mode--purple`
- `ecl-color-mode--blue-navy`
- `ecl-color-mode--blue-electric`
- `ecl-color-mode--blue-ocean`
- `ecl-color-mode--green-lemon`
- `ecl-color-mode--green-pine`
- `ecl-color-mode--warm-grey`
- `ecl-color-mode--red-crayola`
- `ecl-color-mode--yellow-gold`
- `ecl-color-mode--purple-violet`
- `ecl-color-mode--red-tomato`

There is no `ecl-color-mode--default` or `ecl-color-mode--dark` class in the
v5.0.1 stylesheet. Omit the class to use the default tokens.

### Mode summary

This table shows five defining values from each compiled mode. It is a compact
preview, not a list of every override.

| Mode            | Surface 0 | Surface variant 1 | On-surface | On-surface swap 0 | Border    |
| --------------- | --------- | ----------------- | ---------- | ----------------- | --------- |
| `blue`          | `#0046ff` | `#000083`         | `#0038cc`  | `#fff`            | `#0046ff` |
| `green-dark`    | `#003d3d` | `#e8f2b0`         | `#005c5c`  | `#fff`            | `#006666` |
| `orange`        | `#ffb16a` | `#0a3f4d`         | `#8c4c12`  | `#00002e`         | `#ff8a20` |
| `green`         | `#05c67b` | `#003d3d`         | `#03774a`  | `#00002e`         | `#05c67b` |
| `purple`        | `#905fd9` | `#000083`         | `#66439a`  | `#fff`            | `#905fd9` |
| `blue-navy`     | `#000069` | `#69d2c6`         | `#000069`  | `#fff`            | `#000069` |
| `blue-electric` | `#03bbe6` | `#0a3f4d`         | `#02708a`  | `#00002e`         | `#03bbe6` |
| `blue-ocean`    | `#69d2c6` | `#08323e`         | `#0e7065`  | `#00002e`         | `#69d2c6` |
| `green-lemon`   | `#ddec8d` | `#313c5e`         | `#626d26`  | `#00002e`         | `#cbe250` |
| `green-pine`    | `#445c63` | `#cabfff`         | `#445c63`  | `#fff`            | `#445c63` |
| `warm-grey`     | `#bfb4af` | `#0a3f4d`         | `#726660`  | `#00002e`         | `#b3a59f` |
| `red-crayola`   | `#e33755` | `#00002e`         | `#a1273c`  | `#fff`            | `#e95f77` |
| `yellow-gold`   | `#ffe05e` | `#0a3f4d`         | `#735d00`  | `#00002e`         | `#ffd72e` |
| `purple-violet` | `#b1a1ff` | `#000069`         | `#6352b5`  | `#00002e`         | `#b1a1ff` |
| `red-tomato`    | `#ff684a` | `#0a3f4d`         | `#b54a35`  | `#00002e`         | `#ff684a` |

Every mode overrides 28 variables. All 15 override the 10 core surface tokens,
the 7 core on-surface tokens, three core border tokens (`low`, `medium`, and
the base border), and seven component/color-mode tokens. Blue, green-dark, and
orange also override `--cm-border-high`; the other 12 instead override
`--cm-on-surface-grey-low`. Tokens not overridden by a mode keep their default
`:root` value.

## Applying and nesting modes

Color-mode variables inherit, so the class may be on the same element or an
ancestor:

```html
<section class="ecl-color-mode--orange">
  <div
    class="ecl-u-bg-surface-0 ecl-u-type-color-on-surface-swap-0 ecl-u-border-all ecl-u-border-color-border"
  >
    Orange-mode surface, foreground, and border
  </div>
</section>
```

A nested mode replaces the inherited values only within its own subtree:

```html
<main class="ecl-color-mode--blue">
  <section class="ecl-u-bg-surface-low-0 ecl-u-type-color-on-surface">
    Blue-mode region
  </section>

  <section class="ecl-color-mode--green-dark">
    <div class="ecl-u-bg-surface-low-0 ecl-u-type-color-on-surface">
      Nested green-dark region
    </div>
  </section>
</main>
```

Color modes affect every ECL component and utility using the overridden
variables inside their scope. Place the class at the narrowest container that
should change. Removing the class restores inherited/default values.

## Color-mode utility classes

Only these adaptive tokens have general-purpose utilities in v5.0.1.

### Background

```text
ecl-u-bg-surface-lowest
ecl-u-bg-surface-lowest-variant
ecl-u-bg-surface-low-0
ecl-u-bg-surface-low-1
ecl-u-bg-surface-low-2
ecl-u-bg-surface-medium-0
ecl-u-bg-surface-medium-1
ecl-u-bg-surface-0
ecl-u-bg-surface-variant-1
ecl-u-bg-surface-variant-2
ecl-u-bg-on-surface-highlight
```

### Text colour

```text
ecl-u-type-color-on-surface
ecl-u-type-color-on-surface-1
ecl-u-type-color-on-surface-2
ecl-u-type-color-on-surface-3
ecl-u-type-color-on-surface-swap-0
ecl-u-type-color-on-surface-swap-1
```

### Border colour

```text
ecl-u-border-color-border-low
ecl-u-border-color-border-medium
ecl-u-border-color-border
ecl-u-border-color-border-high
```

Other `--cm-*` tokens are available to ECL components or custom CSS but do not
automatically imply a utility class with the same suffix.

## Extended adaptive token inventory

Besides the 21 core tokens above, `ecl-ec.css` defines these 80 tokens. Use
their exact custom properties in custom CSS; do not invent utility classes.

### Extended surface tokens

- `--cm-surface-0-add-to-calendar`
- `--cm-surface-0-text-media`
- `--cm-surface-brand`
- `--cm-surface-color-mode-high`
- `--cm-surface-color-mode-low`
- `--cm-surface-color-mode-lowest`
- `--cm-surface-grey-highest-0`
- `--cm-surface-grey-highest-1-transparent`
- `--cm-surface-grey-highest-2-transparent`
- `--cm-surface-grey-low-0`
- `--cm-surface-grey-low-0-transparent`
- `--cm-surface-grey-low-1`
- `--cm-surface-grey-medium`
- `--cm-surface-inverted`
- `--cm-surface-neutral`
- `--cm-surface-neutral-low`
- `--cm-surface-neutral-lowest`
- `--cm-surface-neutral-medium`
- `--cm-surface-primary`
- `--cm-surface-primary-high`
- `--cm-surface-primary-highest`
- `--cm-surface-primary-low-0`
- `--cm-surface-primary-low-1`
- `--cm-surface-primary-lowest`
- `--cm-surface-primary-medium`
- `--cm-surface-secondary`
- `--cm-surface-secondary-high`
- `--cm-surface-secondary-highest`
- `--cm-surface-secondary-low`
- `--cm-surface-secondary-medium-0`
- `--cm-surface-secondary-medium-1`
- `--cm-surface-status-error`
- `--cm-surface-status-error-lowest`
- `--cm-surface-status-info`
- `--cm-surface-status-info-lowest`
- `--cm-surface-status-success`
- `--cm-surface-status-success-lowest`
- `--cm-surface-status-warning`
- `--cm-surface-status-warning-lowest`
- `--cm-surface-transparent-01`
- `--cm-surface-transparent-70`

### Extended on-surface tokens

- `--cm-on-surface-add-to-calendar`
- `--cm-on-surface-brand`
- `--cm-on-surface-grey`
- `--cm-on-surface-grey-low`
- `--cm-on-surface-grey-low-transparent`
- `--cm-on-surface-grey-medium`
- `--cm-on-surface-inverted`
- `--cm-on-surface-neutral-highest`
- `--cm-on-surface-neutral-low`
- `--cm-on-surface-neutral-medium`
- `--cm-on-surface-primary`
- `--cm-on-surface-primary-highest`
- `--cm-on-surface-secondary-highest`
- `--cm-on-surface-secondary-medium`
- `--cm-on-surface-status-error`
- `--cm-on-surface-status-info`
- `--cm-on-surface-status-success`
- `--cm-on-surface-status-warning`
- `--cm-on-surface-text-media`

### Extended border tokens

- `--cm-border-brand`
- `--cm-border-grey`
- `--cm-border-grey-low`
- `--cm-border-grey-low-300`
- `--cm-border-grey-lowest`
- `--cm-border-grey-medium`
- `--cm-border-inverted`
- `--cm-border-inverted-low-transparent`
- `--cm-border-neutral`
- `--cm-border-neutral-high`
- `--cm-border-neutral-highest`
- `--cm-border-neutral-low`
- `--cm-border-on-brand`
- `--cm-border-primary`
- `--cm-border-primary-highest`
- `--cm-border-primary-medium`
- `--cm-border-status-error`
- `--cm-border-status-info`
- `--cm-border-status-success`
- `--cm-border-status-warning`

Example using extended tokens directly:

```css
.app-status-panel {
  background-color: var(--cm-surface-status-info-lowest);
  border: 1px solid var(--cm-border-status-info);
  color: var(--cm-on-surface-status-info);
}
```

## Accessibility and usage rules

- Maintain at least 4.5:1 contrast for normal text and 3:1 for large text.
- Meaningful control boundaries, focus indicators, and graphical objects
  should have at least 3:1 contrast against adjacent colours.
- Test adaptive foreground/background pairs in the default and every color mode
  used. A fixed text colour that works in one mode may fail in another.
- Alpha colours blend with their actual backdrop; calculate contrast after
  compositing, not from the alpha token alone.
- Never communicate success, warning, error, information, selection, or focus
  with colour alone. Include text, shape, position, or an icon as appropriate.
- Preserve visible keyboard focus. Do not replace a component's focus colour
  without providing an equally visible indicator.
- ECL utility colour declarations use `!important`; custom properties do not.
  Avoid stacking conflicting utilities and do not rely on class order in the
  HTML attribute.
- Use `currentColor` when an icon or border should intentionally follow the
  surrounding text colour.
