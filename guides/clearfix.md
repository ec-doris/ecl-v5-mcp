# ECL Clearfix Utility (EC preset, v5.0.1)

Use `ecl-u-clearfix` on a normal container when floated content must contribute
to that container's height. This prevents later content from unexpectedly
wrapping around or overlapping the container's floats.

## Required CSS

Load the EC utilities stylesheet:

```html
<link rel="stylesheet" href="assets/ecl-ec-utilities.css" />
```

Call `guide("assets")` for the complete ECL asset setup. The clearfix rule is
in `ecl-ec-utilities.css`, not `ecl-ec.css`, and is also included in
`ecl-ec-print.css`. It has no theme, color-mode, font, or JavaScript dependency.

When compiling from Sass packages, load its standalone entry point:

```scss
@use "@ecl/utility-clearfix/clearfix";
```

## Class and exact behavior

Apply the class to the **parent** of the floated content:

```text
ecl-u-clearfix
```

ECL v5.0.1 implements it as:

```css
.ecl-u-clearfix::after {
  clear: both !important;
  content: "" !important;
  display: block !important;
}
```

The empty block pseudo-element is generated after the parent's content.
`clear: both` moves it below preceding left- and right-floated content. Because
that pseudo-element remains in normal flow, the parent expands far enough to
contain it and therefore the floats.

There is no `::before` rule in v5.0.1.

## Basic usage with ECL float utilities

```html
<section class="ecl-u-clearfix">
  <div class="ecl-u-f-l">Left-floated content</div>
  <div class="ecl-u-f-r">Right-floated content</div>
</section>
<p>This paragraph starts after the containing section.</p>
```

Load `ecl-ec-utilities.css` for both the clearfix and float classes. Call
`guide("float")` for the complete float utility contract.

## Text wrapping around a floated image

```html
<article class="ecl-u-clearfix">
  <img
    class="ecl-u-f-l"
    src="image.jpg"
    alt="Description of the image"
    width="160"
    height="120"
  />
  <p>
    This text can wrap beside the image, while the article still contains the
    floated image when the text is shorter than it.
  </p>
</article>
```

Add appropriate ECL spacing utilities when visual separation is needed;
clearfix itself adds no margin, padding, width, or gap.

## Clearfix versus removing a float

Clearfix and `float: none` solve different problems:

- Put `ecl-u-clearfix` on a parent to contain its floated children.
- Put `ecl-u-f-none` on an element to cancel that element's float.
- Clearfix does not cancel, reposition, or resize the floated content.
- `ecl-u-f-none` on a child does not clear any other floated siblings.

```html
<div class="ecl-u-clearfix">
  <aside class="ecl-u-f-r">This remains floated right.</aside>
</div>

<aside class="ecl-u-f-none">This element is not floated.</aside>
```

## When to use it

Use clearfix when all of the following are true:

- one or more descendants are floated;
- the containing box would otherwise collapse or end above those floats; and
- content following the container must begin below it.

For new rows, columns, alignment, or responsive layouts, prefer ECL flex or
grid utilities. Those layout models contain their children without clearfix.
Float remains appropriate when inline content is intentionally meant to wrap
around another element.

## Boundaries and interactions

- The utility creates only an `::after`; it does not create an `::before` or
  insert a real DOM element.
- It clears preceding left and right floats that affect the container's
  formatting context, regardless of whether ECL classes or project CSS created
  them.
- It does not establish a new block formatting context. If the container must
  also be isolated from floats outside it, use an appropriate layout method or
  a project rule such as `display: flow-root`.
- It does not prevent margin collapsing. A two-pseudo-element clearfix recipe
  found elsewhere on the web may behave differently from this ECL rule.
- Apply it to a normal container that can generate an `::after` pseudo-element,
  such as a `div`, `section`, or `article`; do not put it on the floated child,
  an `img`, or another void/replaced element.
- `ecl-u-clearfix` owns the element's `::after` content, display, and clear
  properties with `!important`. Do not use it on an element whose `::after`
  already provides decoration or meaningful generated content.
- Existing `overflow`, `display: flow-root`, flex, or grid containment may make
  clearfix redundant.
- The class has no responsive variants and imposes no ARIA attributes, IDs, or
  JavaScript hooks. Its empty pseudo-element carries no content for assistive
  technologies.
