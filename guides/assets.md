ECL EC Assets

To start using ECL EC, you need to bring in the following assets into your project:

Copy the following folder from your node_modules into your project's assets folder:

```
__DIR__/assets/*
```

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

Then include the following code in the head of your HTML document:

```html            
<link rel="icon" href="assets/favicon.ico" type="image/x-icon">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="assets/logo-ec-positive-en.svg">
<link rel="stylesheet" href="assets/ecl-reset.css">
<link rel="stylesheet" href="assets/ecl-ec.css">
<link rel="stylesheet" href="assets/ecl-ec-utilities.css">
<link rel="stylesheet" href="assets/ecl-ec-print.css" media="print">
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

The above code includes the necessary CSS and JavaScript files for the ECL EC theme. The reset and the utilties are important.

Datepickers are now made using the duet.js library. You need to load the duet.js script from unpkg.com as shown above.

Icons are now made by WebTools, you make a span with the correct classes to get the icon you want. No longer are the icons in a .svg file. See examples: in the Icon Component 

call: get_component_examples('icon')

The official documentation.
https://webtools.europa.eu/showcase/demo?comp=icons&section=about&demo=how_to_use&lang=en#about