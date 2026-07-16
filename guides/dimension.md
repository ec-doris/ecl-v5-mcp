# ECL Dimension Utilities (EC preset, v5.0.1)

Dimension utilities provide eight classes for `width`, `height`, `max-height`,
and ECL's shared max-width token. All declarations use `!important`.

The max-width classes are an important exception: they set the custom property
`--max-w`, not the CSS `max-width` property directly.

## Required CSS

Load the EC utilities stylesheet:

```html
<link rel="stylesheet" href="assets/ecl-ec-utilities.css" />
```

Call `guide("assets")` for the complete ECL asset setup. The dimension rules
are in `ecl-ec-utilities.css`, not `ecl-ec.css`, and are also present in
`ecl-ec-print.css`. No JavaScript or color-mode stylesheet is required.

When compiling from Sass packages, load the standalone entry point:

```scss
@use "@ecl/utility-dimension/dimension";
```

ECL v5.0.1 provides no responsive or breakpoint variants of these classes.

## Exact class contract

| Class                   | Exact declaration             |
| ----------------------- | ----------------------------- |
| `ecl-u-width-auto`      | `width: auto !important`      |
| `ecl-u-width-100`       | `width: 100% !important`      |
| `ecl-u-height-auto`     | `height: auto !important`     |
| `ecl-u-height-100`      | `height: 100% !important`     |
| `ecl-u-max-width-none`  | `--max-w: none !important`    |
| `ecl-u-max-width-100`   | `--max-w: 100% !important`    |
| `ecl-u-max-height-none` | `max-height: none !important` |
| `ecl-u-max-height-100`  | `max-height: 100% !important` |

Use at most one class from each pair. Class order in the HTML attribute does
not control precedence; avoid conflicting utilities.

## Width

### Full available width

```html
<div class="ecl-u-width-100">Full containing-block width</div>
```

`width: 100%` is calculated from the containing block. With the default
`content-box` sizing, the element's padding and border are added outside that
width and can cause overflow. Use ECL's border-box utility when they must fit
inside the declared width:

```html
<div class="ecl-u-width-100 ecl-u-box-sizing-border ecl-u-border-all">
  Border and padding fit inside the 100% width.
</div>
```

In flex and grid layouts, `width` also interacts with flex basis, shrinking,
minimum size, tracks, and alignment. `ecl-u-width-100` does not override those
other layout rules.

### Automatic width

```html
<div class="ecl-u-width-auto">Automatic width</div>
```

`width: auto` restores the normal sizing behavior for the element's formatting
context. A block element commonly fills its available inline space, while an
image or other replaced element commonly uses its intrinsic dimensions. It
does not mean “width equal to content” in every layout mode.

## Height

### Full containing-block height

```html
<div style="height: 20rem;">
  <div class="ecl-u-height-100 ecl-u-box-sizing-border ecl-u-border-all">
    This can resolve to the parent's 20rem height.
  </div>
</div>
```

Percentage height needs a definite containing-block height. If the parent's
height is content-driven or otherwise indefinite, `height: 100%` may behave
like `auto` instead of filling the visual space. In nested percentage-height
layouts, each relevant ancestor needs a resolvable height.

As with width, padding and border can make a content-box element exceed 100%.
Use `ecl-u-box-sizing-border` when appropriate.

### Automatic height and intrinsic media ratio

```html
<img
  class="ecl-u-width-100 ecl-u-height-auto"
  src="image.jpg"
  alt="Description of the image"
  width="800"
  height="450"
/>
```

`height: auto` allows content to determine the height. On an image with useful
intrinsic `width` and `height` attributes, combining full width with automatic
height preserves its aspect ratio. This example can upscale a small image;
use a max-width constraint when upscaling is not wanted.

## Max height

The max-height utilities set the real CSS property:

```html
<div style="height: 20rem; overflow: auto;">
  <div class="ecl-u-max-height-100">
    Content constrained to at most the parent's definite height.
  </div>
</div>
```

- `ecl-u-max-height-100` limits height to `100%` of a resolvable containing
  block; it does not force the element to become that tall.
- `ecl-u-max-height-none` removes a max-height constraint.
- Max height does not choose overflow behavior. Content remains visible by
  default and may overflow; add a suitable project or ECL overflow rule when
  clipping or scrolling is intentionally required.

## Max width uses `--max-w`

ECL EC defines this default in `ecl-ec.css`:

```css
:root {
  --ecl-max-width: 80ch;
  --max-w: var(--ecl-max-width);
}
```

Many ECL components and paragraph typography utilities consume it with:

```css
max-width: var(--max-w);
```

The two dimension classes change that shared token:

- `ecl-u-max-width-none` changes `--max-w` to `none`.
- `ecl-u-max-width-100` changes `--max-w` to `100%`.

They do **not** emit `max-width: none` or `max-width: 100%`. Therefore:

- They work directly on an ECL element whose CSS already uses
  `max-width: var(--max-w)`.
- They have no direct sizing effect on an arbitrary element that does not
  consume `--max-w`.
- They do not override an unrelated explicit `max-width` declaration.
- Because custom properties inherit, applying one to a parent can change every
  descendant component that consumes `--max-w`. Scope the class narrowly.

### Remove ECL's default 80ch paragraph cap

```html
<p class="ecl-u-type-paragraph ecl-u-max-width-none">
  This paragraph utility consumes --max-w, so its usual 80ch cap is removed.
</p>
```

### Cap an ECL paragraph at its container width

```html
<p class="ecl-u-type-paragraph ecl-u-max-width-100">
  This paragraph cannot exceed the width of its containing block.
</p>
```

### Use the token with arbitrary media

For an arbitrary image, explicitly connect `max-width` to the token:

```html
<img
  class="ecl-u-max-width-100 ecl-u-height-auto"
  style="max-width: var(--max-w); width: 40rem;"
  src="image.jpg"
  alt="Description of the image"
  width="800"
  height="450"
/>
```

The upstream v5.0.1 Storybook demonstration uses this same
`max-width: var(--max-w)` connection. Without it, the max-width utility class
alone would only define an otherwise unused custom property on the image.

For reusable project markup, prefer a project class over an inline style:

```css
.app-responsive-media {
  height: auto;
  max-width: var(--max-w);
}
```

```html
<img
  class="app-responsive-media ecl-u-max-width-100"
  src="image.jpg"
  alt="Description of the image"
  width="800"
  height="450"
/>
```

## Combining dimensions

Width/height and maximum constraints solve different problems and may be
combined when their containing blocks are well defined:

```html
<div style="height: 20rem; width: 20rem;">
  <div
    class="ecl-u-width-100 ecl-u-height-100 ecl-u-max-height-100 ecl-u-box-sizing-border"
  >
    Full-size child constrained by the parent's dimensions.
  </div>
</div>
```

Do not add `ecl-u-max-width-100` to this arbitrary child unless it or a
descendant actually consumes `--max-w`.

## Accessibility and implementation notes

- Avoid fixed-height containers that clip text when users zoom, enlarge fonts,
  translate content, or use longer labels. Prefer content-driven height where
  possible.
- If constrained content can overflow, provide an intentional and keyboard-
  accessible way to reach it. Do not hide essential content.
- Preserve intrinsic image dimensions and aspect ratios to reduce layout shift
  and distortion.
- Percentage dimensions are relative to a containing block, not necessarily
  the viewport.
- These utilities set no minimum dimensions. Existing `min-width`,
  `min-height`, intrinsic sizing, or flex/grid constraints can still win in the
  final used size.
- They impose no ARIA attributes, IDs, DOM structure, or JavaScript hooks.
