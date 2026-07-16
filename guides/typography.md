# ECL Typography Utilities (EC preset, v5.0.1)

EC typography uses the Inter variable font and provides semantic heading,
paragraph, and microcopy styles plus lower-level size, weight, color,
transformation, decoration, alignment, highlight, and enhanced-text utilities.

## Required assets

Load the main EC stylesheet for theme variables and `@font-face`, then the
utilities stylesheet:

```html
<link rel="stylesheet" href="assets/ecl-ec.css" />
<link rel="stylesheet" href="assets/ecl-ec-utilities.css" />
<link rel="stylesheet" href="assets/ecl-ec-print.css" media="print" />
```

Call `guide("assets")` for the complete setup. Keep `assets/` and `fonts/` as
sibling directories: ECL tries the WebTools-hosted Inter files first and
`../fonts/InterVariable.woff2` or `InterVariable-Italic.woff2` as local
fallbacks. Typography utility selectors are not in `ecl-ec.css`. No JavaScript
is required.

When compiling Sass, use `@ecl/utility-typography`; its screen entry point is
`typography.scss` and its print entry point is `typography-print.scss`.

The screen font stack is `Inter, arial, sans-serif`. Responsive semantic type
uses these mobile-first tiers:

| Typography tier | Minimum width |
| --------------- | ------------- |
| mobile-xs       | 0px           |
| mobile          | 480px         |
| tablet          | 768px         |
| desktop         | 1140px        |

There is no typography transition at the grid's 996px `l` breakpoint.

## Semantic headings

Use semantic HTML for the document outline and add the class matching the
desired ECL presentation:

```html
<h1 class="ecl-u-type-heading-1">About the European Commission</h1>
<h2 class="ecl-u-type-heading-2">Priorities</h2>
```

The class does not change an element's semantic heading level. Do not choose an
`h3` merely because its visual size is wanted; keep heading levels logical and
apply the visual class separately when necessary.

Each table cell below is `font-size / line-height / letter-spacing`. “Normal”
means no letter-spacing declaration from the utility.

| Class                  | 0px                         | 480px                       | 768px                       | 1140px                      | Weight |
| ---------------------- | --------------------------- | --------------------------- | --------------------------- | --------------------------- | ------ |
| `ecl-u-type-display`   | 2.75rem / 2.75rem / normal  | 2.75rem / 3.25rem / -1px    | 4rem / 4rem / -1px          | 6rem / 6rem / -2px          | 400    |
| `ecl-u-type-heading-1` | 2rem / 2.25rem / normal     | 2.25rem / 2.5rem / -1px     | 3.25rem / 3.5rem / -2px     | 4rem / 4rem / -2px          | 600    |
| `ecl-u-type-heading-2` | 1.5rem / 2rem / normal      | 1.75rem / 2rem / normal     | 2.25rem / 2.5rem / -1px     | 2.75rem / 3rem / -1px       | 600    |
| `ecl-u-type-heading-3` | 1.125rem / 1.75rem / normal | 1.375rem / 1.75rem / normal | 1.75rem / 2rem / normal     | 1.75rem / 2rem / normal     | 600    |
| `ecl-u-type-heading-4` | 1.125rem / 1.75rem / normal | 1.25rem / 1.75rem / normal  | 1.375rem / 1.75rem / normal | 1.5rem / 2rem / normal      | 500    |
| `ecl-u-type-heading-5` | 1.125rem / 1.5rem / normal  | 1.125rem / 1.5rem / normal  | 1.25rem / 1.5rem / normal   | 1.375rem / 1.75rem / normal | 500    |
| `ecl-u-type-heading-6` | 1rem / 1.5rem / normal      | 1rem / 1.25rem / normal     | 1.125rem / 1.5rem / normal  | 1.125rem / 1.5rem / normal  | 650    |

`ecl-u-type-display` is a visual display style, not a seventh heading level.
Use it sparingly and retain appropriate semantic markup.

## Paragraph styles

```html
<p class="ecl-u-type-paragraph">
  Default paragraph style and readable line length.
</p>

<p class="ecl-u-type-paragraph-xl">Lead paragraph text.</p>
```

All paragraph utilities set the text color to `currentcolor` and constrain
`max-width` to `var(--max-w)`. The EC default is 80ch; call
`guide("dimension")` before changing it. Paragraph utilities do not add margin
or set a font weight, so the weight is inherited.

Each value is `font-size / line-height`:

| Style and class                                      | 0px               | 480px              | 768px              | 1140px             |
| ---------------------------------------------------- | ----------------- | ------------------ | ------------------ | ------------------ |
| XS — `ecl-u-type-paragraph-xs`                       | .875rem / 1.25rem | .875rem / 1.25rem  | .875rem / 1.25rem  | .875rem / 1.25rem  |
| S — `ecl-u-type-paragraph-s`                         | .875rem / 1.25rem | 1rem / 1.5rem      | 1rem / 1.5rem      | 1rem / 1.5rem      |
| M — `ecl-u-type-paragraph`, `...-paragraph-m`        | 1rem / 1.5rem     | 1.125rem / 1.75rem | 1.125rem / 1.75rem | 1.125rem / 1.75rem |
| L — `ecl-u-type-paragraph-l`                         | 1rem / 1.5rem     | 1.125rem / 1.75rem | 1.125rem / 1.75rem | 1.25rem / 1.75rem  |
| XL — `ecl-u-type-paragraph-xl`, `...-paragraph-lead` | 1.375rem / 2rem   | 1.125rem / 1.75rem | 1.25rem / 1.75rem  | 1.375rem / 2rem    |
| 2XL — `ecl-u-type-paragraph-2xl`                     | 1.25rem / 1.75rem | 1.25rem / 1.75rem  | 1.375rem / 2rem    | 1.5rem / 2.25rem   |

The XL style becoming smaller at 480px before growing again at later tiers is
the actual EC v5.0.1 theme behavior, not a transcription error.

`ecl-u-type-paragraph-lead` resolves to the XL paragraph style in the EC theme.
Prefer `ecl-u-type-paragraph-xl` when the named size is clearer.

## Microcopy

Microcopy styles set Inter, font size, line height, and `currentcolor`, but do
not set font weight:

| Class                      | 0px                | 480px and above    |
| -------------------------- | ------------------ | ------------------ |
| `ecl-u-type-microcopy-2xs` | .75rem / .875rem   | .75rem / .875rem   |
| `ecl-u-type-microcopy-xs`  | .875rem / 1rem     | .875rem / 1rem     |
| `ecl-u-type-microcopy-s`   | .875rem / 1rem     | 1rem / 1.5rem      |
| `ecl-u-type-microcopy-m`   | 1.125rem / 1.75rem | 1.125rem / 1.75rem |

Use microcopy for short supporting labels or metadata, not to make essential
information visually insignificant.

## Lower-level type-size classes

The EC bundle contains `ecl-u-type-2xs`, `ecl-u-type-xs`, `ecl-u-type-s`,
`ecl-u-type-m`, `ecl-u-type-l`, `ecl-u-type-xl`, and
`ecl-u-type-2xl` through `ecl-u-type-10xl`.

- `xs` through `2xl` use the responsive body rows in the paragraph table, but
  without paragraph color or max-width.
- `2xs` is a fixed `.75rem/.875rem` font.
- `3xl` through `10xl` are deprecated raw font shorthands:

| Class             | Size / line height |
| ----------------- | ------------------ |
| `ecl-u-type-3xl`  | 1.75rem / 2.25rem  |
| `ecl-u-type-4xl`  | 2rem / 2.75rem     |
| `ecl-u-type-5xl`  | 2.25rem / 3rem     |
| `ecl-u-type-6xl`  | 2.75rem / 3rem     |
| `ecl-u-type-7xl`  | 3.25rem / 4rem     |
| `ecl-u-type-8xl`  | 4rem / 4.25rem     |
| `ecl-u-type-9xl`  | 4.5rem / 4.875rem  |
| `ecl-u-type-10xl` | 6rem / 6rem        |

Prefer semantic heading, paragraph, or microcopy utilities. Use a lower-level
class only when a design explicitly calls for a size independent of semantics.

## Font weights

| Class                            | Value |
| -------------------------------- | ----- |
| `ecl-u-type-weight-thin`         | 100   |
| `ecl-u-type-weight-extra-light`  | 200   |
| `ecl-u-type-weight-light`        | 300   |
| `ecl-u-type-weight-semi-regular` | 350   |
| `ecl-u-type-weight-regular`      | 400   |
| `ecl-u-type-weight-medium`       | 500   |
| `ecl-u-type-weight-semi-bold`    | 600   |
| `ecl-u-type-weight-near-bold`    | 650   |
| `ecl-u-type-weight-bold`         | 700   |
| `ecl-u-type-weight-extra-bold`   | 800   |
| `ecl-u-type-weight-black`        | 900   |

Inter is loaded as a variable font from weight 100 through 900. Avoid using
weight alone to convey meaning.

## Text colors

The EC bundle emits 161 `ecl-u-type-color-*` classes:

- `primary`, `secondary`, `neutral`, `grey`, `monochrome`, `info`, `success`,
  `error`, and `warning`, each with a base class and shades `25`, `50`, `75`,
  `100` through `900`, and `950`;
- `ecl-u-type-color-alpha`;
- 13 numbered `grey-alpha` and 13 numbered `white-alpha` names;
- `ecl-u-type-color-white` and `ecl-u-type-color-black`;
- adaptive `on-surface`, `on-surface-1`, `on-surface-2`, `on-surface-3`,
  `on-surface-swap-0`, and `on-surface-swap-1`.

```html
<p class="ecl-u-type-paragraph ecl-u-type-color-primary">Primary text</p>

<section class="ecl-color-mode--blue ecl-u-bg-surface-0">
  <p class="ecl-u-type-color-on-surface-swap-0">Mode-aware text</p>
</section>
```

Call `guide("colours")` for exact values, valid color modes, contrast guidance,
and the complete v5.0.1 alpha warning. In particular, do not use numbered
`ecl-u-type-color-grey-alpha-{shade}` or
`ecl-u-type-color-white-alpha-{shade}`: an upstream short-name defect makes
those declarations refer to undefined custom properties. The unnumbered
`ecl-u-type-color-alpha` works.

There is no `ecl-u-type-color-on-surface-highlight` selector in the compiled
v5.0.1 EC assets, even though the Storybook control offers that name. Use
`ecl-u-type-highlight` for highlighted text or a valid color custom property in
project CSS.

Normal text needs at least 4.5:1 contrast and large text at least 3:1. Verify the
actual foreground/background combination, including the active color mode.

## Style, decoration, and alignment

| Class                     | CSS applied                     |
| ------------------------- | ------------------------------- |
| `ecl-u-type-italic`       | `font-style: italic`            |
| `ecl-u-type-capitalize`   | `text-transform: capitalize`    |
| `ecl-u-type-lowercase`    | `text-transform: lowercase`     |
| `ecl-u-type-uppercase`    | `text-transform: uppercase`     |
| `ecl-u-type-overline`     | `text-decoration: overline`     |
| `ecl-u-type-underline`    | `text-decoration: underline`    |
| `ecl-u-type-strike`       | `text-decoration: line-through` |
| `ecl-u-type-none`         | `text-decoration: none`         |
| `ecl-u-type-align-left`   | `text-align: left`              |
| `ecl-u-type-align-right`  | `text-align: right`             |
| `ecl-u-type-align-center` | `text-align: center`            |

Left and right alignment are physical, not direction-logical. Centered
multi-line text is harder to scan; reserve centered alignment for short text.

CSS case transformation does not change the source text. Avoid long uppercase
text, and do not rely on case alone for meaning. Screen readers may not announce
strikethrough, so include an explicit accessible indication of deletion or an
old value when it matters. `ecl-u-type-none` resets decoration only; it does not
reset italic, case transformation, alignment, weight, or color.

## Highlight and enhanced blocks

### Inline highlight

```html
<p class="ecl-u-type-paragraph">
  This is <span class="ecl-u-type-highlight">important context</span>.
</p>
```

`ecl-u-type-highlight` sets a color-mode-aware highlight background. It does
not add padding, weight, or semantic emphasis; use `<em>` or `<strong>` when
emphasis is semantic.

### Enhanced blocks

All enhanced variants use the responsive 2XL body style at weight 300 and
`display: block`:

| Class                       | Background           | Border                         | Text color               | Spacing behavior          |
| --------------------------- | -------------------- | ------------------------------ | ------------------------ | ------------------------- |
| `ecl-u-type-enhance`        | `--cm-surface-low-1` | 4px inline-start `--cm-border` | `--cm-on-surface-brand`  | Padding on every side     |
| `ecl-u-type-enhance-strong` | `--cm-surface-0`     | None                           | `--cm-on-surface-swap-0` | Padding on every side     |
| `ecl-u-type-enhance-light`  | Transparent          | 4px inline-start `--cm-border` | `--cm-on-surface-brand`  | Inline-start padding only |

Padding changes from `m` (1rem) at the base to `xl` (1.5rem) at 768px and
`3xl` (2rem) at 1140px. The border and padding use logical inline-start and
adapt in RTL.

```html
<aside class="ecl-u-type-enhance">
  A prominent piece of supporting information.
</aside>
```

## Print behavior

The print stylesheet keeps the same 221 public class names and replaces the
main semantic type styles with print fonts. Heading print values are:

| Class     | Print size / line height | Weight |
| --------- | ------------------------ | ------ |
| Display   | 54pt / 58.5pt            | 400    |
| Heading 1 | 39pt / 45pt              | 600    |
| Heading 2 | 27pt / 33pt              | 600    |
| Heading 3 | 18pt / 24pt              | 600    |
| Heading 4 | 16.5pt / 24pt            | 500    |
| Heading 5 | 15pt / 21pt              | 500    |
| Heading 6 | 13.5pt / 18pt            | 650    |

Paragraph print sizes are XS 9/12pt, S 10.5/15pt, M 12/18pt, L 13.5/18pt, XL
15/21pt, and 2XL 16.5/24pt. The print heading font stack is
`Inter, arial, sans-serif`; the general print font tokens use
`Inter, verdana, sans-serif`.

## Implementation notes

- The compiled EC utility and print bundles each contain 221 distinct
  `ecl-u-type-*` class names: 161 colors and 60 other typography classes.
- Most size, line-height, color, transformation, decoration, alignment, and
  utility box declarations use `!important`; avoid conflicting utilities.
- Semantic utilities style presentation but never supply HTML semantics,
  accessible names, language metadata, or content.
