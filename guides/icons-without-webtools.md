# Icons without WebTools (unsupported workaround)

## Important disclaimer

This is an **unsupported workaround**, not an official ECL or WebTools
integration. It may be useful when the site is hosted on a non-`europa.eu`
origin and WebTools does not load, but it is not a production-valid solution
by itself. The icon source, CSS variables, class names, markup contract,
licensing/provenance and accessibility behavior can change without this MCP
being able to detect the change.

Use the official WebTools loader on an approved origin whenever possible. If a
local workaround is unavoidable, obtain the required approvals, pin the exact
source files and version, record their origin and hash, test every release,
and keep a replacement plan. Review the applicable EC/WebTools terms before
redistributing any downloaded asset. Do not imply that a locally copied file
is an official ECL distribution.

## When this guide applies

Call `guide("icons")` first. That guide describes the supported markup and the
official WebTools dependency. Use this guide only when that dependency cannot
render on the deployment origin, for example a public site that is neither a
WebTools-approved `europa.eu` origin nor `localhost`.

The patterns below are generic application patterns. They are not dependencies
of this MCP and should be adapted to the framework, asset pipeline and
deployment policy of the consuming application.

## 1. Capture and pin the local source

Start from a working WebTools page, such as the official icon showcase, and
inspect the requests made by `https://webtools.europa.eu/load.js` in browser
developer tools. Identify the icon CSS and SVG sources that the loader
actually requests for the required families. Save only the required files to
your application and record:

- the source URL and the date retrieved;
- the WebTools/ECL release or response metadata, when available;
- a SHA-256 hash of every CSS, SVG and wrapper input file;
- which standard, network and flag names are included; and
- the owner and process responsible for checking for upstream changes.

Do not blindly copy the loader itself or assume that one sprite contains every
family. A captured standard sprite may have `<symbol>` entries such as
`id="audio"` and `id="search"`, while the CSS source contains additional
families and names. Verify each name used by the application against the
captured source.

## 2. Option A: reference a local SVG sprite

If the captured source is a symbol sprite, serve it from the same origin and
reference the symbol with an SVG `<use>`. For example, a locally captured
standard `audio` symbol can be used as follows:

```html
<svg
  class="wt-icon--audio ecl-icon ecl-icon--m ecl-icon--audio"
  viewBox="0 0 48 48"
  aria-hidden="true"
  focusable="false"
>
  <use href="/assets/icons/icons.svg#audio"></use>
</svg>
```

Keep the accessible text on the surrounding control or label. If the icon is
meaningful by itself, do not use `aria-hidden="true"`; give the SVG an
accessible name with the normal SVG accessibility pattern and test it with a
screen reader.

The sprite path, symbol IDs and `<use>` behavior are local application
contracts in this approach. Test them with the browsers and CSP headers used
by the deployment. A restrictive `Content-Security-Policy`, an incorrect
MIME type, a cross-origin sprite or a changed symbol ID can make the icon
silently disappear. Inline the required symbol paths instead if the chosen
browser/support matrix does not reliably resolve an external `<use>`.

## 3. Option B: keep WebTools CSS variables and hydrate inline SVG

This pattern serves the captured WebTools icon CSS locally so the document root
exposes variables such as
`--wt-icon--audio` and family variables such as `--wt-icon-networks--facebook`.
Then let a small wrapper read the variable, parse its SVG value, clone the SVG
children and insert them into a local `<svg>` element.

A marker-based hydrator can use a marker inside the target SVG:

```html
<svg
  class="wt-icon--audio ecl-icon ecl-icon--m ecl-icon--audio"
  viewBox="0 0 48 48"
  aria-hidden="true"
  focusable="false"
>
  <g data-wt-icon="audio"></g>
</svg>
```

The local wrapper reads `--wt-icon--audio`, parses the SVG value with
`DOMParser`, copies the `viewBox`, clones the child nodes and removes the
marker. It exposes a small `hydrate(root)` function and runs it after
`DOMContentLoaded`. If the application inserts icons later, call the same
function on the inserted subtree.

The essential shape is:

```js
function hydrateIcon(marker) {
  const name = marker.getAttribute('data-wt-icon');
  const value = getComputedStyle(document.documentElement)
    .getPropertyValue(`--wt-icon--${name}`)
    .trim();
  if (!value) return;

  const svg = new DOMParser().parseFromString(value, 'image/svg+xml')
    .documentElement;
  const parent = marker.closest('svg');
  if (!parent || svg.localName !== 'svg') return;

  if (svg.getAttribute('viewBox')) {
    parent.setAttribute('viewBox', svg.getAttribute('viewBox'));
  }
  Array.from(svg.childNodes).forEach((node) => {
    parent.insertBefore(document.importNode(node, true), marker);
  });
  marker.remove();
}
```

Treat this as a design sketch, not a drop-in library. A production-minded
wrapper must also handle malformed CSS values, SVG namespaces, text/comment
nodes, repeated hydration, dynamically inserted nodes, CSP, error reporting
and an explicit fallback. Keep the wrapper in the consuming application and
test it as application code; it is not supplied by this MCP.

## 4. Option C: render the inline SVG from a component helper

A component-helper implementation uses the same local CSS-variable source but
does the conversion in a reusable utility. The helper can:

1. build a variable name such as `--wt-icon--edit` or
   `--wt-icon-networks--facebook`;
2. read it with `getComputedStyle(document.documentElement)`;
3. parse the SVG with `DOMParser`;
4. copy the source attributes and child markup into a new SVG element; and
5. apply the ECL/WebTools classes, `viewBox`, dimensions and accessibility
   attributes in the component.

A simplified call site looks like this:

```js
const svg = parseIconSvg('--wt-icon--edit', 'ecl-icon ecl-icon--m');
if (svg) {
  svg.setAttribute('viewBox', '0 0 48 48');
  svg.setAttribute('aria-hidden', 'true');
  iconContainer.appendChild(svg);
}
```

This approach is useful for Vue or other component systems that need icons
after a render/update cycle. Hydrate again after a framework update only when
the component has not already produced an SVG. Preserve the official class
contract where it is useful, but do not assume that local CSS has the same
runtime behavior as WebTools for every family, color, transform or size.

## Local asset loading order

Load the local icon CSS after the main ECL CSS if its selectors are intended to
override the defaults, and load the wrapper after the DOM or call it from the
framework lifecycle. A local-asset page can use an order similar to:

```html
<link rel="stylesheet" href="/assets/ecl/ecl-ec.css">
<link rel="stylesheet" href="/assets/icons/webtools.icons.default.css">
<link rel="stylesheet" href="/assets/icons/icons-local.css">
<script src="/assets/icons/icons-local.js"></script>
```

A small local rule may be needed to make `.ecl-icon` `display: inline-block`;
that is an application workaround, not a replacement for the full
ECL/WebTools contract. Network, flag and other families may need additional
locally captured CSS sources and their own verification.

## Accessibility and failure checks

Before accepting this workaround, test at minimum:

- decorative icons remain hidden from the accessibility tree and meaningful
  icons have a usable name;
- icons render with JavaScript disabled or have an intentional fallback when
  the wrapper fails;
- every local name used by the app exists in the pinned CSS or sprite;
- sizes, colors, transforms, network icons and flags work in every supported
  color mode and at the required responsive breakpoints;
- CSP, caching, MIME type, compression and same-origin rules allow the assets;
- duplicate hydration does not append duplicate paths; and
- the source hash and local asset version are checked during upgrades.

If any of these checks fail, return to the supported WebTools integration or
choose a separately licensed icon set with its own documented API. This guide
does not make the local workaround supported or production-valid.
