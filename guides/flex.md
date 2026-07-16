# ECL Flex Utilities (EC preset, v5.0.1)

Flex utilities control the direction, wrapping, alignment, ordering, growth,
shrinkage, and basis of flex containers and items. The EC preset provides 38
utilities at each of five breakpoints, for 190 classes in total.

## Required CSS and container setup

Load the EC utilities stylesheet:

```html
<link rel="stylesheet" href="assets/ecl-ec-utilities.css" />
```

Call `guide("assets")` for the complete asset setup. The flex rules are in
`ecl-ec-utilities.css`, not `ecl-ec.css`; they are also included in
`ecl-ec-print.css`. No JavaScript is required.

When compiling ECL from Sass packages, use `@ecl/utility-flex`; its Sass entry
point is `flex.scss` and it depends on `@ecl/grid` for breakpoints.

Flex utilities do **not** create a flex formatting context. First add
`ecl-u-d-flex` or `ecl-u-d-inline-flex` to the parent:

```html
<div class="ecl-u-d-flex ecl-u-flex-wrap ecl-u-align-items-center">
  <div>First item</div>
  <div>Second item</div>
</div>
```

Call `guide("display")` for responsive flex display classes.

## Class naming and breakpoints

Use the base class with no breakpoint infix, or insert `s`, `m`, `l`, or `xl`
immediately before the final value:

```text
ecl-u-flex-row        0px and up
ecl-u-flex-s-row      480px and up
ecl-u-flex-m-row      768px and up
ecl-u-flex-l-row      996px and up
ecl-u-flex-xl-row     1140px and up
```

This pattern applies to every class family below. Breakpoint variants use
`min-width` and continue to affect larger viewports. The family prefix remains
intact: for example, use `ecl-u-justify-content-m-between` and
`ecl-u-flex-grow-l-1`.

## Container utilities

### Direction

| Base class                  | CSS value                        |
| --------------------------- | -------------------------------- |
| `ecl-u-flex-row`            | `flex-direction: row`            |
| `ecl-u-flex-column`         | `flex-direction: column`         |
| `ecl-u-flex-row-reverse`    | `flex-direction: row-reverse`    |
| `ecl-u-flex-column-reverse` | `flex-direction: column-reverse` |

### Wrapping

| Base class                | CSS value                 |
| ------------------------- | ------------------------- |
| `ecl-u-flex-wrap`         | `flex-wrap: wrap`         |
| `ecl-u-flex-nowrap`       | `flex-wrap: nowrap`       |
| `ecl-u-flex-wrap-reverse` | `flex-wrap: wrap-reverse` |

### Main-axis distribution

| Base class                      | CSS value                        |
| ------------------------------- | -------------------------------- |
| `ecl-u-justify-content-start`   | `justify-content: flex-start`    |
| `ecl-u-justify-content-end`     | `justify-content: flex-end`      |
| `ecl-u-justify-content-center`  | `justify-content: center`        |
| `ecl-u-justify-content-between` | `justify-content: space-between` |
| `ecl-u-justify-content-around`  | `justify-content: space-around`  |

There is no `space-evenly` utility in v5.0.1.

### Cross-axis item alignment

| Base class                   | CSS value                 |
| ---------------------------- | ------------------------- |
| `ecl-u-align-items-start`    | `align-items: flex-start` |
| `ecl-u-align-items-end`      | `align-items: flex-end`   |
| `ecl-u-align-items-center`   | `align-items: center`     |
| `ecl-u-align-items-baseline` | `align-items: baseline`   |
| `ecl-u-align-items-stretch`  | `align-items: stretch`    |

### Wrapped-line alignment

| Base class                    | CSS value                      |
| ----------------------------- | ------------------------------ |
| `ecl-u-align-content-start`   | `align-content: flex-start`    |
| `ecl-u-align-content-end`     | `align-content: flex-end`      |
| `ecl-u-align-content-center`  | `align-content: center`        |
| `ecl-u-align-content-between` | `align-content: space-between` |
| `ecl-u-align-content-around`  | `align-content: space-around`  |
| `ecl-u-align-content-stretch` | `align-content: stretch`       |

`align-content` is useful only when the container has multiple flex lines and
there is spare cross-axis space. It commonly needs `ecl-u-flex-wrap` plus a
defined container height.

## Item utilities

Apply these classes to flex items, not the container.

### Self alignment

| Base class                  | CSS value                |
| --------------------------- | ------------------------ |
| `ecl-u-align-self-auto`     | `align-self: auto`       |
| `ecl-u-align-self-start`    | `align-self: flex-start` |
| `ecl-u-align-self-end`      | `align-self: flex-end`   |
| `ecl-u-align-self-center`   | `align-self: center`     |
| `ecl-u-align-self-baseline` | `align-self: baseline`   |
| `ecl-u-align-self-stretch`  | `align-self: stretch`    |

### Order

| Base class          | CSS value   |
| ------------------- | ----------- |
| `ecl-u-order-first` | `order: -1` |
| `ecl-u-order-last`  | `order: 1`  |
| `ecl-u-order-0`     | `order: 0`  |

ECL v5.0.1 does not provide numbered order utilities such as
`ecl-u-order-1` or `ecl-u-order-2`. Visual reordering does not change DOM,
screen-reader, or keyboard focus order, so keep the source order logical.

### Grow, shrink, and basis

| Base class              | CSS value          |
| ----------------------- | ------------------ |
| `ecl-u-flex-grow-0`     | `flex-grow: 0`     |
| `ecl-u-flex-grow-1`     | `flex-grow: 1`     |
| `ecl-u-flex-shrink-0`   | `flex-shrink: 0`   |
| `ecl-u-flex-shrink-1`   | `flex-shrink: 1`   |
| `ecl-u-flex-basis-100`  | `flex-basis: 100%` |
| `ecl-u-flex-basis-auto` | `flex-basis: auto` |

These utilities set only one longhand property; they do not set the full
`flex` shorthand.

## Responsive example

```html
<section
  class="ecl-u-d-flex ecl-u-flex-column ecl-u-flex-m-row ecl-u-flex-wrap ecl-u-align-items-m-center"
>
  <div class="ecl-u-flex-grow-m-1">Main content</div>
  <aside class="ecl-u-flex-basis-100 ecl-u-flex-basis-m-auto">
    Related content
  </aside>
</section>
```

This stacks items by default, switches to a row at 768px, lets the main item
grow at that breakpoint, and changes the aside from a full-line basis to an
automatic basis.

## Implementation notes

- Every declaration uses `!important`; avoid conflicting utilities active at
  the same breakpoint.
- `row-reverse`, `column-reverse`, `wrap-reverse`, and `order` affect visual
  presentation without changing accessible source order.
- Flex utilities add no gap or margin. Use ECL spacing utilities when separation
  is needed.
- The exact v5.0.1 inventory is narrower than Bootstrap: use only the classes
  documented here, with an optional supported breakpoint infix.
