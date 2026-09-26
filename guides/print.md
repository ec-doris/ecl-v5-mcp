# ECL EC print utilities (v5.3.1)

The target package is `@ecl/utility-print` v5.3.1. Print utilities are split
between the screen utility bundle and the EC print bundle.

## Visibility

The screen utility bundle defines:

```css
.ecl-u-print-only {
  display: none !important;
}
```

The print bundle defines `ecl-u-screen-only` as hidden for print. Load the
bundles with their intended media types so the visibility pair works:

```html
<link rel="stylesheet" href="assets/ecl-ec-utilities.css" media="screen">
<link rel="stylesheet" href="assets/ecl-ec-print.css" media="print">
```

The v5.3.1 print bundle does not reset `ecl-u-print-only`; leaving the screen
utility bundle active during print can therefore keep print-only content
hidden. Follow `guide("assets")` for the full screen/main/color-mode order.

## Page breaks

The print bundle supplies these classes:

```text
ecl-u-break-before-{auto|avoid|page}
ecl-u-break-after-{auto|avoid|page}
ecl-u-break-inside-{auto|avoid}
```

They map to the corresponding paged-media `break-*` properties and are not
marked `!important`. Browser support is best effort, particularly for avoiding
breaks in complex or long content. Test print preview and generated output for
the consuming application; the print spacing scale is intentionally separate
from the screen scale.

Print utilities add no semantics, ARIA, IDs, component hooks or JavaScript.

References: `src/website/src/pages/ec/utilities/print/`,
`src/utilities/print/` and
[official EC print guidance](https://ec.europa.eu/component-library/ec/utilities/print/).
