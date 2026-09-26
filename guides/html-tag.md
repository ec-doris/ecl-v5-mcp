# ECL EC HTML-tag styling (v5.3.1)

HTML-tag styling is an optional edge-case preset feature, not the default MCP
asset set. The pinned source is `src/utilities/html-tag/` together with
`src/presets/ec/src/ec-default.scss` and `ec-default-print.scss` at commit
`0b3ca5a9190e1c32ff00fc092380e3a8f3571a05`.

## Contract

Obtain both optional files from the v5.3.1 EC distribution:

```text
ecl-ec-default.css
ecl-ec-default-print.css
```

Put the markup inside an `.ecl` container. The target preset automatically
styles these bare tags:

- links and buttons;
- headings `h1` through `h6`;
- paragraphs;
- unordered and ordered lists, including nested list cases;
- description lists;
- tables;
- blockquotes and citations; and
- horizontal rules.

The print partner is required for equivalent printed output. Load the optional
screen file before the main EC screen stylesheet, and the optional print file
before the main EC print stylesheet, with the appropriate `media` attributes:

```html
<link rel="stylesheet" href="assets/ecl-ec-default.css" media="screen">
<link rel="stylesheet" href="assets/ecl-ec.css" media="screen">
<link rel="stylesheet" href="assets/ecl-ec-default-print.css" media="print">
<link rel="stylesheet" href="assets/ecl-ec-print.css" media="print">
```

The files are not bundled by this MCP because its examples use explicit ECL
classes and no bare-tag page requires them. Do not copy only one half of the
pair or load these files globally without checking their `.ecl` scope.

## Limits

Bare-tag styling cannot express every component variant and only covers the
listed tags. Prefer the component's explicit ECL classes for new markup,
variants, accessibility hooks and predictable composition. Use
`guide("assets")` for the complete bundled load order and the optional-file
decision.

Reference: [official EC HTML-tag guidance](https://ec.europa.eu/component-library/ec/utilities/html-tag/).
