# ECL Grid (EC preset, v5.0.1)

ECL uses an abridged, mobile-first 12-column Bootstrap-style grid. The public
layout consists of a container, flex rows, responsive columns, optional logical
start offsets, physical push/pull modifiers, and a no-gutters modifier.

## Required CSS

Load the EC component stylesheet:

```html
<link rel="stylesheet" href="assets/ecl-ec.css" />
```

Call `guide("assets")` for the complete asset setup. Grid rules are in
`ecl-ec.css`, not `ecl-ec-utilities.css`, and are also included in
`ecl-ec-print.css`. No JavaScript is required.

When compiling from Sass, use the `@ecl/grid` package and its `grid.scss` entry
point.

## Standard structure

```html
<div class="ecl-container">
  <div class="ecl-row">
    <main class="ecl-col-12 ecl-col-m-8">Main content</main>
    <aside class="ecl-col-12 ecl-col-m-4">Related content</aside>
  </div>
</div>
```

- `ecl-container` centers and constrains the page content.
- `ecl-row` is a wrapping flex container and compensates for column gutters.
- `ecl-col-{span}` and responsive variants set a column's width as a fraction
  of 12.
- Place page content inside columns. A nested row belongs inside a column; it
  does not need another container.

## Breakpoints, columns, and container

| Tier | Minimum width | Column form          | Container behavior         |
| ---- | ------------- | -------------------- | -------------------------- |
| xs   | 0px           | `ecl-col-{1..12}`    | Fluid, 100%                |
| s    | 480px         | `ecl-col-s-{1..12}`  | Fluid, 100%                |
| m    | 768px         | `ecl-col-m-{1..12}`  | Fluid, 100%                |
| l    | 996px         | `ecl-col-l-{1..12}`  | Fluid, 100%                |
| xl   | 1140px        | `ecl-col-xl-{1..12}` | Fluid up to a 1368px width |

All responsive rules use `min-width`: a tier applies at its minimum and above
until a later tier overrides it. Each column has `width: 100%` before its own
tier becomes active, so a class such as `ecl-col-m-6` is full width below 768px
and half width from 768px upward.

```html
<!-- 100% by default, 50% from 768px, 33.333% from 996px. -->
<div class="ecl-col-12 ecl-col-m-6 ecl-col-l-4">...</div>
```

Span values are `1` through `12`; there are no zero, auto-width, or bare
`ecl-col` column rules. Common proportions include:

| Span | Width      |
| ---- | ---------- |
| 1    | 8.333333%  |
| 2    | 16.666667% |
| 3    | 25%        |
| 4    | 33.333333% |
| 6    | 50%        |
| 8    | 66.666667% |
| 9    | 75%        |
| 12   | 100%       |

If active spans total more than 12, `ecl-row` wraps later columns to another
line.

The EC theme's internal container widths are 768px, 996px, 1140px, and 1368px
at the `s`, `m`, `l`, and `xl` tiers. Each also has `max-width: 100%`, so the
container remains fluid until the viewport can accommodate 1368px.

## Gutters

| Tier | Space between adjacent column content | Container padding per side |
| ---- | ------------------------------------- | -------------------------- |
| xs/s | 1rem                                  | 1rem                       |
| m/l  | 1.5rem                                | 1.5rem                     |
| xl   | 2rem                                  | 2rem                       |

Columns receive half a gutter on each inline side. Rows receive matching
negative half-gutter inline margins, while the container receives a full gutter
of inline padding.

To remove row and direct-child column gutters, put `ecl-no-gutters` on the row:

```html
<div class="ecl-row ecl-no-gutters">
  <div class="ecl-col-6">First</div>
  <div class="ecl-col-6">Second</div>
</div>
```

The modifier removes the row's inline margins and the inline padding of direct
children matching `.ecl-col` or `[class*="ecl-col-"]`. It does not recursively
remove gutters from nested grids.

## Offsets

Offsets add `margin-inline-start` equal to a number of grid columns:

```html
<div class="ecl-row">
  <div class="ecl-col-4 ecl-offset-4">Centered four-column region</div>
</div>
```

Available forms are:

- Base: `ecl-offset-{1..11}`.
- Responsive: `ecl-offset-s-{0..11}`, `ecl-offset-m-{0..11}`,
  `ecl-offset-l-{0..11}`, and `ecl-offset-xl-{0..11}`.

There is intentionally no `ecl-offset-0` base class and no offset value `12`.
Responsive zero resets an earlier offset:

```html
<div class="ecl-col-10 ecl-offset-1 ecl-col-m-8 ecl-offset-m-0">...</div>
```

Offsets follow the document's inline-start direction, so they work logically
in left-to-right and right-to-left layouts.

## Push and pull

ECL v5.0.1 also emits `push` and `pull` forms for values `0` through `12` at
every tier:

```text
ecl-push-{0..12}       ecl-pull-{0..12}
ecl-push-s-{0..12}     ecl-pull-s-{0..12}
ecl-push-m-{0..12}     ecl-pull-m-{0..12}
ecl-push-l-{0..12}     ecl-pull-l-{0..12}
ecl-push-xl-{0..12}    ecl-pull-xl-{0..12}
```

Positive push sets physical `left`; positive pull sets physical `right`. Zero
resets the relevant property to `auto`. These modifiers visually move a
relatively positioned column without changing its allocated grid space, DOM
order, focus order, or screen-reader order. They are not direction-logical and
can overlap content. Prefer correct source order and normal responsive column
layouts; use push/pull only when that legacy behavior is deliberately required.

## Nested grid example

```html
<div class="ecl-container">
  <div class="ecl-row">
    <div class="ecl-col-12 ecl-col-l-8">
      <div class="ecl-row">
        <div class="ecl-col-12 ecl-col-m-6">Nested first</div>
        <div class="ecl-col-12 ecl-col-m-6">Nested second</div>
      </div>
    </div>
    <aside class="ecl-col-12 ecl-col-l-4">Related</aside>
  </div>
</div>
```

## Implementation notes

- The compiled EC bundle contains 252 distinct public grid class names: 60
  columns, 65 pushes, 65 pulls, 59 offsets, and the three structural classes.
- Grid layout is flex-based; the row does not clear floats despite legacy source
  comments that refer to floats.
- Container, row, column, and no-gutter inline spacing uses logical properties.
  Push and pull still use physical directions.
- Grid classes do not add vertical spacing, semantic landmarks, or accessibility
  attributes.
