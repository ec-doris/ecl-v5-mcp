# Media Utilities

The ECL Media utilities provide CSS classes for controlling media elements such as images, videos, and background images. These utilities are part of the ECL (European Commission Library) design system, offering consistent sizing, aspect ratios, and background positioning for media content.

## Overview

Media utilities help you create responsive, properly sized media elements without custom CSS. They support different sizes, aspect ratios, and background image positioning to ensure your media looks great across all devices.

## Media Size Classes

Control the dimensions of media elements:

| Class             | Size   | Direction  | Description                                  |
| ----------------- | ------ | ---------- | -------------------------------------------- |
| `ecl-u-media-a-s` | Small  | All        | Small size applied to both width and height  |
| `ecl-u-media-a-m` | Medium | All        | Medium size applied to both width and height |
| `ecl-u-media-h-s` | Small  | Horizontal | Small width, auto height                     |
| `ecl-u-media-h-m` | Medium | Horizontal | Medium width, auto height                    |
| `ecl-u-media-v-s` | Small  | Vertical   | Auto width, small height                     |
| `ecl-u-media-v-m` | Medium | Vertical   | Auto width, medium height                    |

## Media Ratio Classes

Maintain specific aspect ratios for media containers:

| Class                    | Aspect Ratio | Description                            |
| ------------------------ | ------------ | -------------------------------------- |
| `ecl-u-media-ratio-16-9` | 16:9         | Widescreen ratio, ideal for videos     |
| `ecl-u-media-ratio-4-3`  | 4:3          | Standard ratio, good for older content |
| `ecl-u-media-ratio-3-2`  | 3:2          | Classic photo ratio                    |
| `ecl-u-media-ratio-1-1`  | 1:1          | Square ratio, perfect for thumbnails   |

## Background Media Classes

Control background image positioning and sizing:

### Background Position
| Class                             | CSS Value | Description      |
| --------------------------------- | --------- | ---------------- |
| `ecl-u-media-bg-position-initial` | `initial` | Default position |
| `ecl-u-media-bg-position-top`     | `top`     | Align to top     |
| `ecl-u-media-bg-position-bottom`  | `bottom`  | Align to bottom  |
| `ecl-u-media-bg-position-left`    | `left`    | Align to left    |
| `ecl-u-media-bg-position-right`   | `right`   | Align to right   |
| `ecl-u-media-bg-position-center`  | `center`  | Center alignment |

### Background Origin
| Class                           | CSS Value     | Description                      |
| ------------------------------- | ------------- | -------------------------------- |
| `ecl-u-media-bg-origin-padding` | `padding-box` | Position relative to padding box |
| `ecl-u-media-bg-origin-border`  | `border-box`  | Position relative to border box  |
| `ecl-u-media-bg-origin-content` | `content-box` | Position relative to content box |

### Background Repeat
| Class                        | CSS Value   | Description               |
| ---------------------------- | ----------- | ------------------------- |
| `ecl-u-media-bg-repeat-none` | `no-repeat` | No repetition             |
| `ecl-u-media-bg-repeat-all`  | `repeat`    | Repeat in both directions |
| `ecl-u-media-bg-repeat-x`    | `repeat-x`  | Repeat horizontally only  |
| `ecl-u-media-bg-repeat-y`    | `repeat-y`  | Repeat vertically only    |

### Background Size
| Class                         | CSS Value | Description                     |
| ----------------------------- | --------- | ------------------------------- |
| `ecl-u-media-bg-size-contain` | `contain` | Scale to fit within container   |
| `ecl-u-media-bg-size-cover`   | `cover`   | Scale to cover entire container |
| `ecl-u-media-bg-size-auto`    | `auto`    | Original size                   |

## Usage Examples

### Basic Media Sizing

```html
<!-- Small image -->
<img src="example.jpg" alt="Example" class="ecl-u-media-a-s">

<!-- Medium width image -->
<img src="example.jpg" alt="Example" class="ecl-u-media-h-m">

<!-- Small height container -->
<div class="ecl-u-media-v-s">
  <img src="example.jpg" alt="Example">
</div>
```

### Aspect Ratio Containers

```html
<!-- 16:9 video container -->
<div class="ecl-u-media-ratio-16-9">
  <iframe src="video-url" class="ecl-u-media-content"></iframe>
</div>

<!-- Square image container -->
<div class="ecl-u-media-ratio-1-1">
  <img src="thumbnail.jpg" alt="Thumbnail" class="ecl-u-media-content">
</div>
```

### Background Images

```html
<!-- Hero banner with centered background -->
<div class="ecl-u-media-a-m ecl-u-media-bg-position-center ecl-u-media-bg-size-cover ecl-u-media-bg-repeat-none"
     style="background-image: url('hero-image.jpg');">
  <h1>Hero Content</h1>
</div>

<!-- Pattern background -->
<div class="ecl-u-media-bg-repeat-all ecl-u-media-bg-size-auto"
     style="background-image: url('pattern.png');">
  Content with repeating background
</div>
```

### Combined Example

Here's a comprehensive example showing media sizing, ratios, and background utilities:

```html
<div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem; margin-top: 0.5rem;">
  <div style="display: flex; flex-direction: column; align-items: flex-start;">
    <img
      src="https://inno-ecl.s3.amazonaws.com/media/examples/example-image4.jpg"
      alt="example"
      class="ecl-u-media-h-m"
    />
    ecl-u-media-h-m
  </div>

  <div style="display: flex; flex-direction: column; align-items: flex-end;">
    <div style="background-image: url(https://inno-ecl.s3.amazonaws.com/media/examples/example-image4.jpg); background-position: 50%; background-size: cover; min-height: 1rem; min-width: 1rem;" class="ecl-u-media-h-m">
    </div>
    ecl-u-media-h-m
  </div>
</div>

<div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem; margin-top: 0.5rem;">
  <div style="display: flex; flex-direction: column; align-items: flex-start;">
    <div class="ecl-u-media-ratio-16-9 ecl-u-media-h-m">
      <img
        src="https://inno-ecl.s3.amazonaws.com/media/examples/example-image4.jpg"
        alt="example"
        class="ecl-u-media-content"
      />
    </div>
    ecl-u-media-ratio-16-9
  </div>

  <div style="display: flex; flex-direction: column; align-items: flex-end;">
    <div class="ecl-u-media-ratio-16-9 ecl-u-media-h-m">
      <div style="background-image: url(https://inno-ecl.s3.amazonaws.com/media/examples/example-image4.jpg); background-position: 50%; background-size: cover; min-height: 1rem; min-width: 1rem;" class="ecl-u-media-content"></div>
    </div>
    ecl-u-media-ratio-16-9
  </div>
</div>

<div style="background-image: url(https://inno-ecl.s3.amazonaws.com/media/examples/example-image3.jpg); border: 5px dashed #FFD617; margin: 1rem; min-height: 1rem; min-width: 1rem; padding: 1rem;" class="ecl-u-media-a-m ecl-u-media-bg-position-center ecl-u-media-bg-origin-padding ecl-u-media-bg-repeat-none ecl-u-media-bg-size-contain">
</div>
```

## Notes

- Use `ecl-u-media-content` class on the actual media element inside ratio containers to ensure proper positioning.
- Background utilities work best when combined with size classes like `ecl-u-media-a-m`.
- For responsive designs, ECL provides breakpoint-specific variants of these utilities.
- Always provide appropriate `alt` text for images and consider accessibility when using background images.
- The ratio classes create a responsive container that maintains the specified aspect ratio regardless of content size.

These utilities help maintain visual consistency and responsive behavior for all media elements in your ECL-based applications.
