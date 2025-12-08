# Typography

## Typeface

Inter is the standard typeface for the websites under the European Commission domain. The sans serif typeface family is versatile and offers an easy to read display.

```css
font-family: Inter, Arial, sans-serif;
```

## Modular type scale

A modular type scale is a set of type sizes that are proportionally multiplied by the ratio working its way up or down.

The purpose of using the modular type scale is to create a design that is visually pleasing, consistent, and balanced.

We set 1.125rem  as the base font size for body text to ensure readability.

## Weight

Font weight is the thickness of a font's stroke, with various weights used to differentiate content hierarchy. The bold style emphasises the importance in comparison with the regular font style in the font family. We use a scale from 100 to 900 depending on the context. Regular text is used for body text.

## Line height

Line-height, relevant to the size of the typeface itself. Different set of font size / line height are used, based on the context (body text, headings, ...).

## Line length

Line-length is the number of characters displayed in a single line. Lines that are too long or too short can distract readers. For readability, limit to no more than 80 characters including spaces for desktop. Line length for mobile is recommended to use 40 to 60 characters including space per line.

## Headings

### Display

```html
<div className="ecl-u-ph-m ecl-u-pv-xl">
  <div className="ecl-u-type-display">Display - Lorem ipsum dolor sit amet</div>
</div>
```

|           | Font size     | Line height    | Font weight |
| --------- | ------------- | -------------- | ----------- |
| mobile-xs | 6XL - 2.5rem  | 3XL - 2.75rem  | 300 (light) |
| mobile    | 7XL - 3.25rem | 7XL - 3.75rem  | 300 (light) |
| tablet    | 9XL - 4.5rem  | 9XL - 4.875rem | 300 (light) |
| desktop   | 10XL - 6rem   | 10XL - 6rem    | 300 (light) |

### Heading 1

```html
<div className="ecl-u-ph-m ecl-u-pv-xl">
  <div className="ecl-u-type-heading-1">Heading 1 - Lorem ipsum dolor sit amet</div>
</div>
```

|           | Font size     | Line height   | Font weight |
| --------- | ------------- | ------------- | ----------- |
| mobile-xs | 4XL - 2rem    | XL - 2.5rem   | 300 (light) |
| mobile    | 6XL - 2.5rem  | 3XL - 2.75rem | 300 (light) |
| tablet    | 7XL - 3.25rem | 6XL - 3.5rem  | 300 (light) |
| desktop   | 8XL - 3.75rem | 7XL - 3.75rem | 300 (light) |

### Heading 2

```html
<div className="ecl-u-ph-m ecl-u-pv-xl">
  <div className="ecl-u-type-heading-2">Heading 2 - Lorem ipsum dolor sit amet</div>
</div>
```

|           | Font size     | Line height   | Font weight |
| --------- | ------------- | ------------- | ----------- |
| mobile-xs | 2XL - 1.5rem  | L - 2rem      | 300 (light) |
| mobile    | 3XL - 1.75rem | L - 2rem      | 300 (light) |
| tablet    | 5XL - 2.25rem | 3XL - 2.75rem | 300 (light) |
| desktop   | 6XL - 2.5rem  | 4XL - 3rem    | 300 (light) |

### Heading 3

```html
<div className="ecl-u-ph-m ecl-u-pv-xl">
  <div className="ecl-u-type-heading-3">Heading 3 - Lorem ipsum dolor sit amet</div>
</div>
```

|           | Font size     | Line height  | Font weight |
| --------- | ------------- | ------------ | ----------- |
| mobile-xs | M - 1.125rem  | M - 1.75rem  | 300 (light) |
| mobile    | 2XL - 1.5rem  | L - 2rem     | 300 (light) |
| tablet    | 3XL - 1.75rem | XL - 2.25rem | 300 (light) |
| desktop   | 3XL - 1.75rem | XL - 2.25rem | 300 (light) |

### Heading 4

```html
<div className="ecl-u-ph-m ecl-u-pv-xl">
  <div className="ecl-u-type-heading-4">Heading 4 - Lorem ipsum dolor sit amet</div>
</div>
```

|           | Font size    | Line height  | Font weight |
| --------- | ------------ | ------------ | ----------- |
| mobile-xs | M - 1.125rem | M - 1.75rem  | 300 (light) |
| mobile    | M - 1.125rem | M - 1.75rem  | 300 (light) |
| tablet    | 2XL - 1.5rem | XL - 2.25rem | 300 (light) |
| desktop   | 2XL - 1.5rem | XL - 2.25rem | 300 (light) |

### Heading 5

```html
<div className="ecl-u-ph-m ecl-u-pv-xl">
  <div className="ecl-u-type-heading-5">Heading 5 - Lorem ipsum dolor sit amet</div>
</div>
```

|           | Font size     | Line height | Font weight |
| --------- | ------------- | ----------- | ----------- |
| mobile-xs | M - 1.125rem  | S - 1.5rem  | 300 (light) |
| mobile    | M - 1.125rem  | S - 1.5rem  | 300 (light) |
| tablet    | XL - 1.375rem | M - 1.75rem | 300 (light) |
| desktop   | XL - 1.375rem | M - 1.75rem | 300 (light) |

### Heading 6

```html
<div className="ecl-u-ph-m ecl-u-pv-xl">
  <div className="ecl-u-type-heading-6">Heading 6 - Lorem ipsum dolor sit amet</div>
</div>
```

|           | Font size    | Line height | Font weight |
| --------- | ------------ | ----------- | ----------- |
| mobile-xs | M - 1.125rem | S - 1.5rem  | 300 (light) |
| mobile    | M - 1.125rem | S - 1.5rem  | 300 (light) |
| tablet    | L - 1.25rem  | M - 1.75rem | 300 (light) |
| desktop   | L - 1.25rem  | M - 1.75rem | 300 (light) |

## Paragraphs

### 2XL paragraph

```html
<div className="ecl-u-ph-m ecl-u-pv-xl">
  <div className="ecl-u-type-paragraph-2xl">2XL paragraph - The quick brown fox jumps over the lazy dog</div>
</div>
```

|           | Font size     | Line height  | Font weight   |
| --------- | ------------- | ------------ | ------------- |
| mobile-xs | L - 1.25rem   | M - 1.75rem  | 400 (regular) |
| mobile    | XL - 1.375rem | L - 2rem     | 400 (regular) |
| tablet    | XL - 1.375rem | L - 2rem     | 400 (regular) |
| desktop   | 2XL - 1.5rem  | XL - 2.25rem | 400 (regular) |

### XL paragraph (lead)

```html
<div className="ecl-u-ph-m ecl-u-pv-xl">
  <div className="ecl-u-type-paragraph-xl">XL paragraph - The quick brown fox jumps over the lazy dog</div>
</div>
```

|           | Font size     | Line height | Font weight   |
| --------- | ------------- | ----------- | ------------- |
| mobile-xs | XL - 1.375rem | L - 2rem    | 400 (regular) |
| mobile    | XL - 1.375rem | L - 2rem    | 400 (regular) |
| tablet    | XL - 1.375rem | L - 2rem    | 400 (regular) |
| desktop   | XL - 1.375rem | L - 2rem    | 400 (regular) |

### L paragraph

```html
<div className="ecl-u-ph-m ecl-u-pv-xl">
  <div className="ecl-u-type-paragraph-l">L paragraph - The quick brown fox jumps over the lazy dog</div>
</div>
```

|           | Font size   | Line height | Font weight   |
| --------- | ----------- | ----------- | ------------- |
| mobile-xs | L - 1.25rem | M - 1.75rem | 400 (regular) |
| mobile    | L - 1.25rem | M - 1.75rem | 400 (regular) |
| tablet    | L - 1.25rem | M - 1.75rem | 400 (regular) |
| desktop   | L - 1.25rem | M - 1.75rem | 400 (regular) |

### M paragraph (default)

```html
<div className="ecl-u-ph-m ecl-u-pv-xl">
  <div className="ecl-u-type-paragraph-m">M paragraph - The quick brown fox jumps over the lazy dog</div>
</div>
```

|           | Font size    | Line height | Font weight   |
| --------- | ------------ | ----------- | ------------- |
| mobile-xs | S - 1rem     | S - 1.5rem  | 400 (regular) |
| mobile    | S - 1rem     | S - 1.5rem  | 400 (regular) |
| tablet    | M - 1.125rem | M - 1.75rem | 400 (regular) |
| desktop   | M - 1.125rem | M - 1.75rem | 400 (regular) |

### S paragraph

```html
<div className="ecl-u-ph-m ecl-u-pv-xl">
  <div className="ecl-u-type-paragraph-s">S paragraph - The quick brown fox jumps over the lazy dog</div>
</div>
```

|           | Font size | Line height | Font weight   |
| --------- | --------- | ----------- | ------------- |
| mobile-xs | S - 1rem  | S - 1.5rem  | 400 (regular) |
| mobile    | S - 1rem  | S - 1.5rem  | 400 (regular) |
| tablet    | S - 1rem  | S - 1.5rem  | 400 (regular) |
| desktop   | S - 1rem  | S - 1.5rem  | 400 (regular) |

### XS paragraph

```html
<div className="ecl-u-ph-m ecl-u-pv-xl">
  <div className="ecl-u-type-paragraph-xs">XS paragraph - The quick brown fox jumps over the lazy dog</div>
</div>
```

|           | Font size     | Line height  | Font weight   |
| --------- | ------------- | ------------ | ------------- |
| mobile-xs | XS - 0.875rem | XS - 1.25rem | 400 (regular) |
| mobile    | XS - 0.875rem | XS - 1.25rem | 400 (regular) |
| tablet    | XS - 0.875rem | XS - 1.25rem | 400 (regular) |
| desktop   | XS - 0.875rem | XS - 1.25rem | 400 (regular) |

## Microcopy

### M microcopy

```html
<div className="ecl-u-ph-m ecl-u-pv-xl">
  <div className="ecl-u-type-microcopy-m">M microcopy - The quick brown fox jumps over the lazy dog</div>
</div>
```

|                  | Font size    | Line height | Font weight   |
| ---------------- | ------------ | ----------- | ------------- |
| mobile & desktop | M - 1.125rem | S - 1.5rem  | 400 (regular) |

### S microcopy

```html
<div className="ecl-u-ph-m ecl-u-pv-xl">
  <div className="ecl-u-type-microcopy-s">S microcopy - The quick brown fox jumps over the lazy dog</div>
</div>
```

|           | Font size     | Line height  | Font weight   |
| --------- | ------------- | ------------ | ------------- |
| mobile-xs | XS - 0.875rem | 2XS - 1rem   | 400 (regular) |
| mobile    | XS - 0.875rem | 2XS - 1rem   | 400 (regular) |
| tablet    | S - 1rem      | XS - 1.25rem | 400 (regular) |
| desktop   | S - 1rem      | XS - 1.25rem | 400 (regular) |

### XS microcopy

```html
<div className="ecl-u-ph-m ecl-u-pv-xl">
  <div className="ecl-u-type-microcopy-xs">XS microcopy - The quick brown fox jumps over the lazy dog</div>
</div>
```

|                  | Font size     | Line height | Font weight   |
| ---------------- | ------------- | ----------- | ------------- |
| mobile & desktop | XS - 0.875rem | 2XS - 1rem  | 400 (regular) |

### 2XS microcopy

```html
<div className="ecl-u-ph-m ecl-u-pv-xl">
  <div className="ecl-u-type-microcopy-2xs">2XS microcopy - The quick brown fox jumps over the lazy dog</div>
</div>
```

|                  | Font size     | Line height    | Font weight   |
| ---------------- | ------------- | -------------- | ------------- |
| mobile & desktop | 2XS - 0.75rem | 3XS - 0.875rem | 400 (regular) |
