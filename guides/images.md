# ECL EC image guidance (v5.3.1)

The pinned EC guideline at `src/website/src/pages/ec/guidelines/images/index.md`
is content guidance, not a replacement for the media components. The target is
ECL v5.3.1 at commit `0b3ca5a9190e1c32ff00fc092380e3a8f3571a05`.

## Choose an image for a reason

Use visual material only when it adds meaning to the page. The EC guidance
distinguishes:

- photographs for dynamic subjects such as news and people;
- illustrations for informative, transformable topics and themes; and
- infographics for visual explanations of complex information.

Place an image near the content it supports, with the most important image near
the top of the page. Do not put essential text inside an image: HTML text is
searchable, translatable and available to more people.

## Accessibility and rights

Give informative images an alternative that conveys their purpose. Decorative
images should use the empty alternative appropriate to their surrounding
markup. Follow the application's accessibility review for complex images and
infographics; the EC page links to the Web Style Guide's alt-text guidance.

Check copyright before publishing, especially when cropping or otherwise
altering a photograph. Do not add decorative frames, gradients, borders or
drop shadows as a substitute for selecting suitable source material.

## Formats and ECL components

The EC page lists GIF, JPEG/JPG, PNG and SVG as widely supported formats. Raster
images are pixel-based and can become blurry when enlarged; SVG remains sharp
at different resolutions but still needs an accessible treatment in its actual
context.

For responsive sources, captions, credits, video, zoom and aspect ratios use
the relevant component examples instead of inventing a media wrapper:

- `component({"id":"picture"})` for responsive image sources;
- `component({"id":"media-container"})` for image/video/embed behavior;
- `component({"id":"gallery"})`, `component({"id":"featured-item"})`,
  `component({"id":"spotlight"})` and `component({"id":"text-media"})`
  for their documented compositions; and
- `guide("media")` for utility size, ratio and background contracts.

Example media must remain durable and traceable. Replace upstream demo URLs
only with application-owned resources, and verify alternative text, loading,
dimensions and missing-request behavior at the consuming site.

Reference: [official EC image guidance](https://ec.europa.eu/component-library/ec/guidelines/images/).
