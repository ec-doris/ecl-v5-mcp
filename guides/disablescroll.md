# ECL EC disable-scroll utility (v5.3.1)

The target package is `@ecl/utility-disablescroll` v5.3.1. Its complete
implementation is one class:

```css
.ecl-u-disablescroll {
  overflow: hidden !important;
}
```

Apply it to the element that actually scrolls in the application, commonly the
document scrolling element while a modal or overlay is open:

```html
<html class="ecl-u-disablescroll">
  ...
</html>
```

Remove the class when the overlay closes. The utility only changes overflow;
it does not manage focus, dialog semantics, scroll-position restoration,
scrollbar compensation, Escape handling or background inertness. Pair it with
the relevant ECL interactive component and application-owned lifecycle logic.

The utility has no responsive variant, color-mode dependency or JavaScript
auto-init hook. It is delivered through the EC utility bundle. The official
page describes it as a helper to prevent unwanted scroll.

References: `src/website/src/pages/ec/utilities/disablescroll/`,
`src/utilities/disablescroll/disablescroll.scss` and
[official EC disable-scroll guidance](https://ec.europa.eu/component-library/ec/utilities/disablescroll/).
