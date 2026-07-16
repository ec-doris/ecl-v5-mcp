# ECL Float Utilities (EC preset, v5.0.1)

Float utilities apply a physical `left`, `right`, or `none` value to an
element. Use them mainly when content such as text must wrap around another
element. For ordinary page and component layouts, prefer ECL flex or grid
utilities.

## Required CSS

Load the EC utilities stylesheet before using these classes:

```html
<link rel="stylesheet" href="assets/ecl-ec-utilities.css" />
```

Call `guide("assets")` for the complete ECL asset setup. The float rules are in
`ecl-ec-utilities.css`, not `ecl-ec.css`. They are also included in the supplied
`ecl-ec-print.css` for print output. No JavaScript is required.

If ECL is compiled from Sass packages instead of using the bundled assets, the
source package is `@ecl/utility-float` and its Sass entry point is `float.scss`.

## Classes

| Class          | CSS applied               | Use                                                                                     |
| -------------- | ------------------------- | --------------------------------------------------------------------------------------- |
| `ecl-u-f-l`    | `float: left !important`  | Float the element to the physical left; following inline content can wrap on its right. |
| `ecl-u-f-r`    | `float: right !important` | Float the element to the physical right; following inline content can wrap on its left. |
| `ecl-u-f-none` | `float: none !important`  | Cancel a float applied by another rule or state.                                        |

Use only one float utility on an element at a time. These classes are not
responsive: ECL v5.0.1 provides no breakpoint variants of them.

`left` and `right` are physical directions. They do not switch automatically
in right-to-left documents. Choose the class deliberately when directionality
matters.

## Examples

### Float left so text wraps

```html
<div class="ecl-u-clearfix">
  <img
    class="ecl-u-f-l"
    src="image.jpg"
    alt="Description of the image"
    width="160"
    height="120"
  />
  <p>
    This text wraps around the right-hand side of the image. Add suitable
    spacing with ECL spacing utilities when the design requires it.
  </p>
</div>
```

### Float right

```html
<div class="ecl-u-clearfix">
  <aside class="ecl-u-f-r">Supplementary content</aside>
  <p>Main content wraps on the left of the floated aside.</p>
</div>
```

### Cancel an existing float

```html
<aside class="ecl-u-f-none">
  This element participates in normal flow because its float is cancelled.
</aside>
```

When changing state dynamically, remove the old directional class and apply
the new class or `ecl-u-f-none`; do not leave conflicting float utilities on
the same element.

### Contain left- and right-floated children

```html
<section class="ecl-u-clearfix">
  <div class="ecl-u-f-l">Left content</div>
  <div class="ecl-u-f-r">Right content</div>
</section>
<p>This paragraph starts after the containing section.</p>
```

## Float versus clearfix

A floated element is shifted to one side and surrounding inline content may
wrap around it. Floated children may not contribute normally to their parent's
height, so later content can overlap or wrap unexpectedly.

Apply `ecl-u-clearfix` to the **parent** when it must contain its floated
children. In ECL v5.0.1 the clearfix creates an `::after` pseudo-element with
`clear: both`, `content: ""`, and `display: block`, all marked `!important`.

- Use `ecl-u-f-none` on an element to cancel that element's float.
- Use `ecl-u-clearfix` on a parent to contain floated children.
- Clearfix does not cancel the float on those children.

Call `guide("clearfix")` for more clearfix examples.

## Implementation notes

- The utilities can be applied to any suitable HTML element and impose no
  component-specific markup, ARIA attributes, IDs, or JavaScript hooks.
- All three declarations use `!important`, so they override non-important
  float declarations. Avoid competing `!important` rules and multiple float
  utilities on the same element.
- Floating changes visual layout, not document order. Keep the DOM in a logical
  reading and focus order, and provide meaningful alternative text for floated
  images.
- A float alone does not add width, margin, padding, or gap. Add those separately
  when needed.
- Use flexbox or grid for rows, columns, alignment, and responsive reordering;
  use float when wrapping content around an element is the intended behavior.
