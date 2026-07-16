# ECL Spacing Utilities (EC preset, v5.0.1)

Spacing utilities apply EC tokens to margin or padding. The values themselves
are fixed, but the classes are responsive: every form is generated at the base,
`s`, `m`, `l`, and `xl` tiers.

## Required CSS

Load the main stylesheet for EC spacing custom properties and the utilities
stylesheet for the classes:

```html
<link rel="stylesheet" href="assets/ecl-ec.css" />
<link rel="stylesheet" href="assets/ecl-ec-utilities.css" />
```

Call `guide("assets")` for the complete asset setup. Spacing utility rules are
not in `ecl-ec.css`; print variants are in `ecl-ec-print.css`. No JavaScript is
required.

When compiling from Sass, use `@ecl/utility-spacing`; its screen entry point is
`spacing.scss`, its print entry point is `spacing-print.scss`, and it depends on
`@ecl/grid` for breakpoints.

## EC spacing tokens

| Token | Value     | Token | Value    | Token  | Value   |
| ----- | --------- | ----- | -------- | ------ | ------- |
| `5xs` | 0.0625rem | `2xs` | 0.375rem | `xl`   | 1.5rem  |
| `4xs` | 0.125rem  | `xs`  | 0.5rem   | `2xl`  | 1.75rem |
| `3xs` | 0.25rem   | `s`   | 0.75rem  | `3xl`  | 2rem    |
|       |           | `m`   | 1rem     | `4xl`  | 2.25rem |
|       |           | `l`   | 1.25rem  | `5xl`  | 2.5rem  |
|       |           |       |          | `6xl`  | 2.75rem |
|       |           |       |          | `7xl`  | 3rem    |
|       |           |       |          | `8xl`  | 3.25rem |
|       |           |       |          | `9xl`  | 3.5rem  |
|       |           |       |          | `10xl` | 3.75rem |
|       |           |       |          | `11xl` | 4rem    |
|       |           |       |          | `12xl` | 4.25rem |
|       |           |       |          | `13xl` | 4.5rem  |

Use the nearest token instead of introducing an arbitrary value. Avoid
unintentional doubled space, such as a child's top margin combined with its
parent's padding for the same visual separation.

## Class grammar

```text
ecl-u-{property}{direction}-{token}
ecl-u-{property}{direction}-{breakpoint}-{token}
```

### Property

| Code | Property |
| ---- | -------- |
| `m`  | margin   |
| `p`  | padding  |

### Direction

| Code | Sides affected    | CSS form                            |
| ---- | ----------------- | ----------------------------------- |
| `a`  | All sides         | `margin` or `padding` shorthand     |
| `h`  | Both inline sides | `*-inline-start` and `*-inline-end` |
| `v`  | Both block sides  | `*-block-start` and `*-block-end`   |
| `t`  | Block start       | `*-block-start`                     |
| `r`  | Inline end        | `*-inline-end`                      |
| `b`  | Block end         | `*-block-end`                       |
| `l`  | Inline start      | `*-inline-start`                    |

Although the one-letter names derive from top/right/bottom/left, v5.0.1 uses
logical properties. Thus `l` means inline-start and `r` means inline-end, so
they reverse appropriately in RTL. Similarly, `t` and `b` use block direction.

Examples:

```html
<section class="ecl-u-pa-l">Padding on every side</section>
<div class="ecl-u-mb-xl">Block-end margin</div>
<nav class="ecl-u-ph-m">Inline padding on both sides</nav>
<span class="ecl-u-ml-s">Inline-start margin</span>
```

Every one of the 21 tokens is available for all seven directions and both
properties.

## None and auto

Every margin and padding direction supports the suffix `none`, which applies
zero:

```html
<div class="ecl-u-ma-none">No margin on any side</div>
<div class="ecl-u-pv-none">No block-axis padding</div>
```

Every **margin** direction also supports `auto`:

```html
<!-- Auto margins on both inline sides, commonly used to center a sized block. -->
<div class="ecl-u-mh-auto" style="max-width: 40rem">...</div>

<!-- Consume available inline space before this flex item. -->
<div class="ecl-u-ml-auto">...</div>
```

There are no `ecl-u-p*-auto` classes and no negative-spacing utilities.

## Responsive spacing

Insert the breakpoint before the final token, `none`, or `auto`:

```text
base:  ecl-u-ma-l             0px and up
s:     ecl-u-ma-s-l           480px and up
m:     ecl-u-ma-m-l           768px and up
l:     ecl-u-ma-l-l           996px and up
xl:    ecl-u-ma-xl-l          1140px and up
```

The repeated letters can be easy to misread: in `ecl-u-ma-m-l`, `ma` means
margin on all sides, `m` is the medium breakpoint, and `l` is the spacing token.

```html
<!-- Padding: 1rem by default, 1.5rem from 768px, 2rem from 996px. -->
<section class="ecl-u-pa-m ecl-u-pa-m-xl ecl-u-pa-l-3xl">...</section>

<!-- End margin removed from 480px upward. -->
<div class="ecl-u-mr-l ecl-u-mr-s-none">...</div>
```

Breakpoint rules are mobile-first `min-width` rules and remain active above
their threshold until a later utility overrides them. The exact class counts
per breakpoint are 161 margin classes (21 tokens + `none` + `auto`, in seven
directions) and 154 padding classes (21 tokens + `none`, in seven directions),
for 315 per tier and 1,575 screen classes total.

## Print behavior

The dedicated print source defines a smaller centimetre-based token set:

| Token | Print value | Token | Print value |
| ----- | ----------- | ----- | ----------- |
| `2xs` | 0.1cm       | `xl`  | 0.63cm      |
| `xs`  | 0.21cm      | `2xl` | 0.84cm      |
| `s`   | 0.31cm      | `3xl` | 1.05cm      |
| `m`   | 0.42cm      | `4xl` | 1.26cm      |
| `l`   | 0.52cm      | `5xl` | 1.47cm      |
|       |             | `6xl` | 1.68cm      |

Print CSS generates these 11 tokens plus margin `none`/`auto` and padding
`none`, again at all five breakpoints, for 875 print rules. When the standard
utilities stylesheet remains loaded during printing, screen-only tokens
(`5xs`–`3xs` and `7xl`–`13xl`) retain their rem-based declarations because the
print stylesheet has no replacement rule for them.

## Implementation notes

- All declarations use `!important`. Remove conflicting utilities rather than
  depending on their order in an HTML `class` attribute.
- These utilities control margin and padding only. ECL v5.0.1 does not generate
  a `gap` family from the spacing utility source.
- Margin does not become part of an element's clickable background; padding
  does. Choose based on whether the space is outside or inside the box.
- Prefer component-provided spacing when using an existing ECL component; add
  utilities for deliberate layout adjustments or custom compositions.
