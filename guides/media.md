# ECL Media Utilities (EC preset, v5.0.1)

Media utilities provide fixed width/height tokens, four aspect-ratio wrappers,
and background-image controls. They can be used with images, embeds, or ordinary
elements, but careless fixed sizing can distort or crop media.

## Required CSS

Load the EC utilities stylesheet:

```html
<link rel="stylesheet" href="assets/ecl-ec-utilities.css" />
```

Call `guide("assets")` for the complete asset setup. The supplied EC build also
contains these rules in `ecl-ec.css` and `ecl-ec-print.css`. No JavaScript is
required.

When compiling from Sass, use `@ecl/utility-media`; its entry point is
`media.scss` and it depends on `@ecl/grid` for breakpoints.

## Fixed media sizes

The EC theme has two media tokens:

| Token | Value |
| ----- | ----- |
| `s`   | 77px  |
| `m`   | 100px |

Combine a dimension code and token:

| Base class pattern      | CSS applied                                      |
| ----------------------- | ------------------------------------------------ |
| `ecl-u-media-a-{token}` | Both `height` and `width` set to the token value |
| `ecl-u-media-h-{token}` | `width` set to the token value                   |
| `ecl-u-media-v-{token}` | `height` set to the token value                  |

`a` means all dimensions, `h` means horizontal/width, and `v` means
vertical/height. Contrary to some informal descriptions, the one-axis forms do
not set the other axis to `auto`; they leave it unchanged.

```html
<img class="ecl-u-media-h-m" src="portrait.jpg" alt="Commissioner Jane Doe" />
```

For intrinsic media, a one-axis class usually preserves the aspect ratio. An
`a` class forces a square and can distort an `<img>` unless another rule such as
`object-fit` handles the content.

### Responsive size forms

All six size combinations exist at every EC breakpoint:

```text
ecl-u-media-{a|h|v}-{s|m}       0px and up
ecl-u-media-{a|h|v}-s-{s|m}     480px and up
ecl-u-media-{a|h|v}-m-{s|m}     768px and up
ecl-u-media-{a|h|v}-l-{s|m}     996px and up
ecl-u-media-{a|h|v}-xl-{s|m}    1140px and up
```

The breakpoint infix comes before the size token. For example:

```html
<!-- Width 77px by default, then 100px from 768px upward. -->
<img
  class="ecl-u-media-h-s ecl-u-media-h-m-m"
  src="portrait.jpg"
  alt="Commissioner Jane Doe"
/>
```

Use ECL breakpoint names `s`, `m`, `l`, and `xl`; `md` and `lg` forms do not
exist in the v5.0.1 CSS.

## Aspect-ratio wrappers

| Wrapper class            | Ratio | Generated top padding |
| ------------------------ | ----- | --------------------- |
| `ecl-u-media-ratio-16-9` | 16:9  | 56.25%                |
| `ecl-u-media-ratio-4-3`  | 4:3   | 75%                   |
| `ecl-u-media-ratio-3-2`  | 3:2   | 66.6667%              |
| `ecl-u-media-ratio-1-1`  | 1:1   | 100%                  |

Put sizing and external spacing on the wrapper, then add
`ecl-u-media-content` to its descendant media:

```html
<div class="ecl-u-media-ratio-16-9 ecl-u-media-h-m">
  <img
    class="ecl-u-media-content"
    src="thumbnail.jpg"
    alt="Video: press conference highlights"
  />
</div>
```

The ratio wrapper becomes a positioned block and uses an `::before`
pseudo-element for its height. A descendant `.ecl-u-media-content` is
absolutely positioned at the top-right with `height: 100%` and `width: 100%`.
ECL's Storybook example uses horizontal sizing on the wrapper; setting a fixed
height with an `a` or `v` size can defeat the ratio technique.

A direct-child `<iframe>` is also absolutely positioned to fill the wrapper:

```html
<div class="ecl-u-media-ratio-16-9" style="max-width: 40rem">
  <iframe
    src="https://example.test/embed/video"
    title="Press conference highlights"
    allowfullscreen
  ></iframe>
</div>
```

For responsive content, prefer a fluid or constrained width rather than the
77px/100px fixed-size utilities. ECL supplies the ratio behavior, but the
application may set a suitable wrapper width or max-width.

## Background-image utilities

These classes alter only the named background property. Set the actual
`background-image` and an element size separately.

### Origin

| Class                           | CSS value     |
| ------------------------------- | ------------- |
| `ecl-u-media-bg-origin-border`  | `border-box`  |
| `ecl-u-media-bg-origin-padding` | `padding-box` |
| `ecl-u-media-bg-origin-content` | `content-box` |

### Position

| Class                             | CSS value |
| --------------------------------- | --------- |
| `ecl-u-media-bg-position-initial` | `0 0`     |
| `ecl-u-media-bg-position-top`     | `top`     |
| `ecl-u-media-bg-position-bottom`  | `bottom`  |
| `ecl-u-media-bg-position-left`    | `left`    |
| `ecl-u-media-bg-position-right`   | `right`   |
| `ecl-u-media-bg-position-center`  | `center`  |

Despite its name, `ecl-u-media-bg-position-initial` explicitly sets `0 0`, not
the CSS-wide `initial` keyword. Left and right are physical directions.

### Repeat

| Class                        | CSS value   |
| ---------------------------- | ----------- |
| `ecl-u-media-bg-repeat-all`  | `repeat`    |
| `ecl-u-media-bg-repeat-x`    | `repeat-x`  |
| `ecl-u-media-bg-repeat-y`    | `repeat-y`  |
| `ecl-u-media-bg-repeat-none` | `no-repeat` |

### Size

| Class                         | CSS value |
| ----------------------------- | --------- |
| `ecl-u-media-bg-size-auto`    | `auto`    |
| `ecl-u-media-bg-size-contain` | `contain` |
| `ecl-u-media-bg-size-cover`   | `cover`   |

```html
<div
  class="ecl-u-media-bg-position-center ecl-u-media-bg-repeat-none ecl-u-media-bg-size-cover"
  style="background-image: url('hero.jpg'); min-height: 18rem"
  role="img"
  aria-label="Berlaymont building at sunrise"
></div>
```

Use a normal `<img>` with useful `alt` text when the image conveys content.
CSS background images have no native alternative-text mechanism; decorative
backgrounds should remain unannounced, while meaningful ones need an equivalent
accessible description or content elsewhere.

## Implementation notes

- Size, ratio-content, and background declarations use `!important` except the
  ratio wrapper's `display`, direct-iframe rules, and a few positioning rules.
- Ratios and background controls have no responsive variants; only fixed media
  sizes are generated per breakpoint.
- The compiled bundle contains 30 size classes, four ratio wrapper classes,
  `ecl-u-media-content`, and 16 background classes.
- These utilities do not set `object-fit`, `object-position`, an image source,
  loading behavior, captions, or accessible names.
