ECL EC Assets

To start using ECL EC, copy the bundled assets and local font fallbacks into your project:

Copy these folders from the installed MCP package to the same paths in your project:

```
__DIR__/assets/*
__DIR__/fonts/*
```

- assets/ecl-ec-color-modes.css
- assets/ecl-ec-color-modes.css.map
- assets/ecl-ec-print.css
- assets/ecl-ec-print.css.map
- assets/ecl-ec-utilities.css
- assets/ecl-ec-utilities.css.map
- assets/ecl-ec.css
- assets/ecl-ec.css.map
- assets/ecl-ec.js
- assets/ecl-esm-ec.js
- assets/ecl-reset.css
- assets/favicon.ico
- assets/favicon.svg
- assets/logo-ec-negative-en.svg
- assets/logo-ec-positive-en.svg
- fonts/InterVariable.woff2
- fonts/InterVariable-Italic.woff2
- fonts/version.txt

Then include the following code in the head of your HTML document:

```html
<link rel="icon" href="assets/favicon.ico" type="image/x-icon" />
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml" />
<link rel="apple-touch-icon" href="assets/logo-ec-positive-en.svg" />
<link rel="stylesheet" href="assets/ecl-reset.css" />
<link rel="stylesheet" href="assets/ecl-ec.css" />
<link rel="stylesheet" href="assets/ecl-ec-color-modes.css" />
<link rel="stylesheet" href="assets/ecl-ec-utilities.css" />
<link rel="stylesheet" href="assets/ecl-ec-print.css" media="print" />
<style>
  .duet-date__dialog {
    z-index: 1000;
  }
</style>
<script src="https://unpkg.com/@duetds/date-picker@1.4.0/dist/duet/duet.js"></script>
<script src="assets/ecl-ec.js"></script>
<script src="https://webtools.europa.eu/load.js"></script>
```

Ofcourse you can compile some of these files into your application's main CSS and JS files, but make sure to include all the necessary parts.

The above code includes the necessary CSS and JavaScript files for the ECL EC theme. The reset and utilities are important. The color modes stylesheet enables the optional `ecl-color-mode--*` themes and has no effect until one of those classes is used.

The main stylesheets try the WebTools-hosted Inter font first and then `../fonts/` as a local fallback. Keep `assets/` and `fonts/` as sibling folders so those fallback URLs resolve correctly.

Datepickers are now made using the duet.js library. You need to load the duet.js script from unpkg.com as shown above.

Icons are provided by WebTools: use a `span` with the appropriate icon classes
instead of referencing an SVG file. To retrieve the reusable icon examples,
call `component("icon")`:

```json
{
  "tool": "component",
  "parameters": {
    "id": "icon"
  }
}
```

The official documentation.
https://webtools.europa.eu/showcase/demo?comp=icons&section=about&demo=how_to_use&lang=en#about
