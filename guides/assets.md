# ECL EC assets — v5.3.1

The bundled EC CSS and JavaScript come from the official v5.3.1 release at
commit `0b3ca5a9190e1c32ff00fc092380e3a8f3571a05`. Copy both directories from
this MCP package into your application, keeping them as siblings:

```text
__DIR__/assets/*
__DIR__/fonts/*
```

## Included files and pinned source

- Main component styles: `assets/ecl-ec.css` and its `.css.map`.
- Print styles: `assets/ecl-ec-print.css` and its `.css.map`.
- Optional helpers: `assets/ecl-reset.css`, `assets/ecl-ec-utilities.css`, and
  `assets/ecl-ec-color-modes.css`. Utilities and color modes have `.css.map` files;
  the official reset build does not.
- JavaScript: `assets/ecl-ec.js` (classic browser bundle) or
  `assets/ecl-esm-ec.js` (ES module). Choose one.
- EC branding: `assets/favicon.ico`, `assets/favicon.svg`,
  `assets/logo-ec-positive-en.svg`, and `assets/logo-ec-negative-en.svg`.
- Inter fonts: `fonts/InterVariable.woff2`, `fonts/InterVariable-Italic.woff2`,
  and `fonts/version.txt`. Inter **4.1** is the font version, independent of ECL.

The release's `styles/`, `styles/optional/`, and `scripts/` files are flattened
into `assets/`; CSS and JavaScript bytes are unchanged. Source maps retain the
original mappings but embed the pinned SCSS and replace build-machine paths
with pinned source URLs, so debugging does not require the upstream checkout.
The source archive and commit are recorded above; the provenance manifest is
not shipped because it is not needed by the MCP runtime.

## Page setup

Use this order in the document head: reset, utilities, main EC styles, then
color modes. Apply screen styles only to screen; the print bundle includes its
own component and utility styles.

The official setup puts all optional styles before the main stylesheet. Keep
color modes **after** the main stylesheet here: `.ecl-color-mode--*` and `:root`
have equal specificity, so the main defaults would otherwise override a mode
applied to `<html>`. This exception was checked against the v5.3.1 CSS; a mode
on a descendant container also works with this order.

```html
<html lang="en" class="no-js">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Your page title</title>
  <script>
    document.documentElement.classList.remove('no-js');
    document.documentElement.classList.add('has-js');
  </script>
  <link rel="icon" href="assets/favicon.ico" type="image/x-icon">
  <link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="assets/ecl-reset.css" media="screen">
  <link rel="stylesheet" href="assets/ecl-ec-utilities.css" media="screen">
  <link rel="stylesheet" href="assets/ecl-ec.css" media="screen">
  <link rel="stylesheet" href="assets/ecl-ec-color-modes.css" media="screen">
  <link rel="stylesheet" href="assets/ecl-ec-print.css" media="print">
  <script defer src="https://webtools.europa.eu/load.js"></script>
</head>
```

Color modes are optional: use an `ecl-color-mode--*` class on the intended
container. Utilities are also optional, but the supplied examples use them.
The reset is recommended for new pages; check its effect when integrating an
existing application. Do not add the EC logo as an `apple-touch-icon`; that
requires an appropriate touch-icon asset supplied by your application.

Place the classic bundle and initialization after the page content, immediately
before `</body>`. The synchronous script finishes before the following call:

```html
<script src="assets/ecl-ec.js"></script>
<script>
  ECL.autoInit();
</script>
```

Alternatively, replace those two scripts with a single module script. Import
and initialize in the same module so initialization waits for the dependency:

```html
<script type="module">
  import { ECL } from './assets/ecl-esm-ec.js';
  ECL.autoInit();
</script>
```

Do not follow a separate `type="module" src="..."` tag with an immediate
classic-script `ECL.autoInit()` call: modules are deferred and ECL may not yet
exist. Serve the page over HTTP(S) when using modules. In either setup,
`ECL.version` reports `5.3.1` once the bundle is loaded. See `guide("start")`
for initializing components added after the initial page render.

## Fonts, branding and icons

The main and print styles try WebTools-hosted Inter first, then
`../fonts/InterVariable.woff2` or `../fonts/InterVariable-Italic.woff2` as local
fallbacks. Preserve the `assets/` and `fonts/` sibling layout. Copying the fonts
does not disable the initial remote request; a local-only deployment needs a
deliberate font-source override and its own loading checks.

The English positive and negative EC logos and both favicons match the pinned
upstream resources. For another language, obtain the matching logo from the
same release's `images/logo/positive/` or `images/logo/negative/` directory;
do not substitute an EU logo. See `guide("logos")` for the variant and language
contract. The older `resources-ec-favicons` package is marked deprecated
upstream and is not copied into this package.

Use `guide("images")` for content, alternative-text and media-selection
guidance. It is distinct from the `guide("media")` utility contract.

Icons are delivered by WebTools, separately from the ECL bundles. Load its
script once and use the `span` classes and accessible labels from
`component("icon")` and `guide("icons")`. For example, hide a decorative icon
beside visible text with `aria-hidden="true"`. An icon-only control still
needs an accessible name. See the
[official WebTools icon instructions](https://webtools.europa.eu/showcase/demo?comp=icons&section=about&demo=how_to_use&lang=en#about).

## Datepicker dependency (only on pages using it)

ECL's datepicker integrates **Duet Date Picker 1.4.0**, which is not bundled.
For self-hosting, install `@duetds/date-picker@1.4.0` in the consuming application,
copy the **contents** of its `dist/` directory into `assets/duet/`, and load:

```html
<script type="module" src="assets/duet/duet.esm.js"></script>
```

Keep the entire distribution, including its lazy-loaded files. If external
CDNs are permitted for the application, the official setup also supports:

```html
<script type="module"
  src="https://cdn.jsdelivr.net/npm/@duetds/date-picker@1.4.0/dist/duet/duet.esm.js"></script>
```

Use one approach. Retain the ECL datepicker markup and `Datepicker` auto-init
hook from its component example. No Duet script or global dialog z-index
override is required by the starter, which contains no datepicker.

## Other optional styles

The upstream distribution also provides `ecl-ec-default.css` and
`ecl-ec-default-print.css` for automatically styling supported bare HTML tags
inside `.ecl`. These files are not bundled here: the supplied examples use
explicit ECL classes. If your application needs this mode, obtain both files
from the v5.3.1 release and follow the
[HTML-tag guidance](https://ec.europa.eu/component-library/ec/utilities/html-tag/).
Keep the screen file before the main screen stylesheet and the print partner
before the main print stylesheet, with the respective media attributes.

`ecl-ec-easy-to-read.css` is also not bundled or required by the current
examples. It targets `.ecl-easy-to-read`; adopt it deliberately for an
application's easy-to-read content rather than loading it on every page.

Reference: [official EC getting started](https://ec.europa.eu/component-library/ec/getting-started/)
and the [v5.3.1 release](https://github.com/ec-europa/europa-component-library/releases/tag/v5.3.1).
The asset version does not certify every existing component example: the
incremental content audit is recorded in `__DIR__/update-status.md`.
