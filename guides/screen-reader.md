# ECL EC screen-reader utility (v5.3.1)

The target package is `@ecl/utility-screen-reader` v5.3.1. Use
`ecl-u-sr-only` for text that should remain available to assistive technology
while being visually clipped:

```html
<span class="ecl-u-sr-only">Additional context</span>
```

The pinned Sass applies `!important` declarations for zero border and padding,
two clipping rules, a 1px box, negative margin, hidden overflow, absolute
positioning, no wrapping and a 1px width. It is a visual technique, not a
replacement for `aria-hidden`, accessible names, labels or live-region design.

Do not place the class on content that must be keyboard-focusable. ECL v5.3.1
does not ship a companion focus-reveal utility. Keep visually hidden text
short, accurate and equivalent to the visible operation or content; do not
create a different experience for screen-reader users.

The utility has no responsive variant, color-mode dependency or JavaScript
auto-init hook and is delivered through the EC utility bundle.

References: `src/website/src/pages/ec/utilities/screen-reader/`,
`src/utilities/screen-reader/screen-reader.scss` and
[official EC screen-reader guidance](https://ec.europa.eu/component-library/ec/utilities/screen-reader/).
