# ECL EC logos (v5.3.1)

The pinned EC logo guideline is backed by `@ecl/resources-ec-logo` at
`0b3ca5a9190e1c32ff00fc092380e3a8f3571a05`. It provides muted logos and
standard EC logos in positive and negative variants for official EU languages
and other supported languages.

## Select the correct variant

- Use the muted variant only where the EC guideline calls for that treatment.
- Use a positive or negative standard logo according to the surrounding
  background and contrast requirements.
- Select the file for the actual page language. Do not substitute an EU logo or
  an English wordmark for an EC language variant.

The upstream resource uses paths such as:

```text
src/logo-ec--mute.svg
src/logo-ec--mute-negative.svg
src/positive/logo-ec--en.svg
src/negative/logo-ec--en.svg
```

The MCP bundles only the English positive and negative EC logos and the EC
favicon pair needed by its starter. Other language logos remain obtainable from
the same pinned release; copy the matching positive/negative files together
when an application needs them.

Keep the logo as an image or link with a meaningful accessible name supplied by
the surrounding page. Do not add the EC logo as an `apple-touch-icon` unless an
appropriate touch-icon asset and application requirement have been established.
Keep branding assets from one traceable ECL release and do not silently mix EC
and EU branding.

Reference: [official EC logo guidance](https://ec.europa.eu/component-library/ec/guidelines/logo/)
and [guide("assets")](assets.md).
