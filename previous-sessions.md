# Previous ECL EC update sessions

This file preserves the completed session history moved out of the active tracker.
Keep the entries in order and append future session entries here. The active
snapshot, row statuses, findings and next recommendation remain in
[update-status.md](update-status.md).

## Session history

### S001 — 2026-09-25 — Establish the v5.3.1 update cycle

- **Scope:** refreshed upstream, created `updating-prompt.md`, and inventoried
  tools/content/gaps in `update-status.md`. No served content or handlers changed.
- **Upstream:** `git -C europa-component-library pull --ff-only` advanced
  `eba75687ecce5cddbb8d7c6ce8854a6e913986b3` to
  `cd0f615bd16816d8d99517192b1f817ae4a85618`; target independently pinned to release
  commit `0b3ca5a9190e1c32ff00fc092380e3a8f3571a05`.
- **Official reference checks:** EC homepage and getting-started displayed
  v5.3.1. The web retrieval tool could not fetch the What's New page; release
  evidence was read from `v5.3.1:CHANGELOG.md` instead. Detailed per-component
  online documentation review remains part of each implementation batch.
- **Live MCP validation:** `guide_list` and `components_list` matched the local
  18/69 inventories. Called all 18 guides, all 69 HTML examples, all 69 advertised
  Twig lookups, and the starter tool. Compared returned text/decoded template
  maps with local files (applying guide `__DIR__` substitution): **156 passed,
  one tooltip template error**. All 87 existing Twig files appeared in successful
  responses. Captured file/upload prefix collision and EU footer exposure.
- **Tagged-source validation:** compared all 87 local Twig files with the tag:
  54 identical, 31 different, 2 no longer present. Four branding files and all
  three font files are byte-identical to tagged sources. Both JS bundles report
  v5.0.1. These comparisons are initial evidence, not full component validation.
- **Repository hygiene:** preserved the user's existing `component-update.md`
  deletion. Historical source version/evidence can be recovered from Git. Only
  the two new workflow documents are authored in the MCP repository this session.
- **Tracker validation:** 234 unique work IDs; all 199 existing tracked files
  represented; local links and concrete upstream reference paths checked; summary
  status counts agree with the tables; whitespace checks passed.
- **Handoff:** all implementation rows remain pending except the explicit legacy
  tracker exclusion. Next batch is shared assets and setup guidance, as above.

For each later session append: date/ID, selected row IDs, changes, exact source
version, commands/tool calls and results, unresolved issues, and next batch.
If verification is incomplete, leave `Updated`/`Blocked` with an actionable note.

### S002 — 2026-09-25 — Shared assets and setup contract

- **Scope:** all 18 existing `ASSET-ecl-*`, favicon/logo and `FONT-*` file rows,
  `GUIDE-assets`, `GUIDE-start`; assessed the three optional stylesheet gaps and
  `ASSET-branding-coverage`. Added `SUPPORT-asset-provenance`. Updated loading
  snippets/cross-references in the other 16 guides without certifying their
  class/token content. `PAGE-starter` received shared setup fixes only and stays
  Needs update. No component HTML/Twig or server handlers changed.
- **Baseline and sources:** official EC homepage/getting-started and GitHub
  [release page](https://github.com/ec-europa/europa-component-library/releases/tag/v5.3.1)
  checked; GitHub releases/latest API still reports v5.3.1, published
  2026-09-21T08:12:27Z. No newer release observed. Upstream remains clean at
  `cd0f615bd16816d8d99517192b1f817ae4a85618`; no repeat pull/build was needed after
  S001’s same-day refresh. All source reads used `git show v5.3.1:<path>`.
  Read `CHANGELOG.md` and preset/resource diffs from prior baseline
  `eceefe9468e44f7ce9c57801c91c4c0c057548b4`: new story-card/highlighted-search,
  Picture/StoryCard JS exports, slider/carousel refactoring, file redesign,
  table filtering, color token changes and site-header/layout fixes remain
  relevant to subsequent component batches. Their inclusion in the new bundles
  does not verify old examples. The What's New, HTML-tag and WebTools showcase
  URLs could not be retrieved through the web tool; tagged HTML-tag usage was
  read alongside the accessible getting-started page.
- **Distribution:** downloaded the official
  [ec-preset-v5.3.1.zip](https://github.com/ec-europa/europa-component-library/releases/download/v5.3.1/ec-preset-v5.3.1.zip)
  with `curl -fsSL`; SHA-256
  `3bfd276a3cb13563cd819235c0ebeab260ffa1400a90658782144c1556d152e3`
  matches the GitHub release API digest. No moving-branch build or existing
  upstream dist/node_modules was used. The release’s EC banner is
  `2026-09-21T08:14:20.968Z`; reset’s is `2026-09-21T08:14:16.155Z`.
- **Asset changes:** copied seven CSS/JS files unchanged, flattening release
  `styles/`, `styles/optional/` and `scripts/` into `assets/`. Updated all four
  corresponding maps. Their published maps referenced CI paths with no embedded
  source: resolved package names through pinned package.json files, rewrote
  `sources` to raw GitHub URLs at the pinned commit, and embedded exact tagged
  `sourcesContent` (empty text for synthetic `<no source>`). All other map fields,
  including `mappings`, remain identical. Retained four branding files and three
  font files byte-for-byte. Full upstream/local SHA-256 values and source paths
  are in [docs/ecl-v5.3.1-assets.json](docs/ecl-v5.3.1-assets.json).
- **Setup fixes:** reset/utilities precede main screen CSS; color modes follow
  it. A fresh-page cascade comparison confirmed a green-dark class on `html`
  gives `--cm-surface-0: #00002e` (overwritten) when color modes precede main CSS,
  versus intended `#003d3d` when they follow. Nested color modes and a 24px margin
  utility work with the selected order. This is an intentional exception to the
  official optional-CSS order. Screen styles no longer leak into print.
  The starter switches no-js/has-js in the head, loads classic JS at body end,
  calls autoInit after loading, and no longer includes unused Duet, an arbitrary
  datepicker z-index override, a logo masquerading as a touch icon, or `</source>`.
  Guides show classic and safe import-and-init module alternatives and explain
  fresh initialization for new DOM. The source evidence is
  `src/tools/dom-utils/autoinit/index.js`: update retains the original node list;
  destroy clears the global registry. Live getting-started has the same module
  timing pitfall as the pinned page, not a newer-release discrepancy.
- **Coverage decisions:** default/default-print and easy-to-read styles are
  Excluded for this cycle because the supplied examples use explicit ECL classes
  and no `.ecl-easy-to-read` content. GUIDE-assets documents upstream opt-in and
  the `.ecl` namespace; DOC-html-tag can reopen that decision if an example needs
  it. The current English logo/favicons cover this starter; extra languages can
  be obtained from the pinned archive. The old platform-favicon package is
  deprecated. Example media and detailed logo guidance remain separate pending
  rows. Duet 1.4.0 is documented as an optional self-hosted/CDN dependency only
  for datepicker pages; no datepicker markup or behavior was changed/tested here.
- **Browser checks:** temporary Playwright runtime outside the repository,
  headless Chrome 153.0.8010.53, local HTTP server. Starter initialized SiteHeader
  and Menu with both classic and imported ESM bundles reporting 5.3.1. No page
  errors or missing local requests; all 18 asset/font URLs returned 200. Checked
  widths 375/480/768/996/1140/1280 with no horizontal overflow; visually inspected
  desktop/mobile and print screenshots. Enter/Escape on language dialogs at
  desktop/mobile restored focus; mobile menu Enter/Escape and search Enter/Escape
  updated state and focus. Print hides header actions, menu contents and footer,
  and renders black headings. No duplicate IDs observed. Fresh scoped autoInit
  initialized 20 newly inserted notification roots; prior update initialized
  none and a repeated fresh call preserved registry size. This tests the setup
  API, not notification-family conformance. No screen-reader or cross-browser
  accessibility certification is claimed.
- **External limitation:** WebTools `load.js` failed with `ERR_BLOCKED_BY_ORB` in
  this browser environment, leaving icons unrendered. Both remote Inter requests
  returned 403 and **both local normal/italic fallbacks loaded successfully**.
  Keep GUIDE-assets Updated until actual icon delivery can be verified; retry
  with GUIDE-icons/HTML-icon in a reachable environment. Do not replace the
  official loader with a downloaded workaround. Starter’s existing empty search
  `aria-controls`, unnamed search toggle, CMS-specific fields/links and
  mega-menu modifier around Menu markup are recorded for Batch 2.
- **MCP checks:** connected tools read this checkout’s edits without a restart.
  All 18 guides matched disk after `__DIR__` substitution; guide_list matched
  18 topics and snippets, components_list matched 69 IDs, and starter_template
  matched the edited file. Sampled component and component_template for
  site-header, menu and site-footer: all HTML and all seven returned template
  keys matched disk, including the still-exposed EU footer. These are delivery
  checks, not component conformance claims. Final changed guide/starter reads
  were repeated after the cascade correction.
- **Focused checks:** all 18 manifest SHA-256 values passed; seven compiled
  CSS/JS files match archive bytes; four maps preserve original mappings and
  all 191 non-synthetic embedded source entries match pinned Git content.
  Every local CSS/font/source-map URL resolves. `node --check` passed for
  index.js and both bundles; `git diff --check` passed. `npm pack --dry-run`
  includes the provenance manifest and excludes the upstream symlink. No project
  tests or ESLint configuration exist, so no Jest/ESLint suite is claimed; no
  Laravel code changed. User deletion of component-update.md and all upstream
  state preserved. No commit, push or publication.
- **Handoff:** 18 asset/font files and GUIDE-start verified, GUIDE-assets Updated
  with the external icon check pending; branding coverage and provenance verified.
  Next is Batch 2 above. Other guides’ v5.0.1 labels deliberately remain until
  their content audits are complete.

### S003 — 2026-09-25 — Batch 2: EC site-wide shell and template delivery

- **Scope:** `TOOL-components-list`, `TOOL-component-template`,
  `TOOL-starter-template`, the EC site-header/site-footer HTML examples, the
  changed site-header, mega-menu, page-header and EC footer Twig families,
  `PAGE-starter`, and `SUPPORT-runtime`. The unchanged Menu and standalone
  mega-menu/page-header HTML examples remain Review rows for a later rendered
  example audit.
- **Sources:** checked the official [EC library](https://ec.europa.eu/component-library/ec/)
  (v5.3.1), the [v5.3.1 release](https://github.com/ec-europa/europa-component-library/releases/tag/v5.3.1),
  the tagged [source tree](https://github.com/ec-europa/europa-component-library/tree/v5.3.1)
  and [changelog](https://github.com/ec-europa/europa-component-library/blob/v5.3.1/CHANGELOG.md).
  The target tag resolves to `0b3ca5a9190e1c32ff00fc092380e3a8f3571a05`; all changed
  Twig files were copied from `git show v5.3.1:<path>` and checked against the tag;
  three files received whitespace-only normalization for clean repository diffs.
- **Template delivery:** replaced the seven changed EC Twig files with exact
  v5.3.1 sources and confirmed the paired unchanged family helpers against the
  tag. Added explicit template-family mapping in `index.js`; `file` no longer
  captures `file-upload`, `site-footer` no longer exposes the legacy EU footer,
  and tooltip is no longer advertised because it has no standalone Twig source.
  The legacy EU Twig file stays on disk for traceability and is marked Excluded.
- **EC HTML/starter changes:** updated the site-header examples to use the
  pinned button/search-dialog contract, removed the EU-only header variant,
  removed the EU footer demo/empty output, and kept EC footer/color-mode coverage.
  The starter now has a named search button, a labelled dialog, a reusable GET
  form, no Drupal/CMS fields, official-language labelling, and the standard
  `ecl-site-header--has-menu` modifier around the standard Menu component.
- **MCP checks:** fresh stdio verification passed `components_list` (69 IDs),
  affected HTML delivery, starter delivery, and template calls. `site-footer`
  returns exactly `site-footer-ec.html.twig` and
  `site-footer-ec-section.html.twig`; `file` returns exactly `file.html.twig`;
  tooltip returns the expected no-template error and is absent from list
  advertising. `node --check index.js`, HTML parsing/duplicate-ID checks for all
  70 HTML files, `git diff --check`, and `npm pack --dry-run` passed. No project
  Jest tests or ESLint configuration exist; no Laravel code changed.
- **Browser checks:** local HTTP serving of the starter used the pinned v5.3.1
  assets. At 375px, the accessible Search action expanded the dialog, focused
  `site-header-search-input`, and collapsed on Escape; Menu expanded and
  collapsed independently. Desktop shell loading also passed. The mouse hit-test
  shows the existing ECL mobile stacking overlap between the Search and Menu
  buttons, so the semantic accessibility action was used for the search assertion;
  no source/runtime handler failure was found. WebTools icon loading remains
  blocked by ORB as recorded in S002.
- **Handoff:** Batch 2 delivery rows are recorded as Verified/Updated/Excluded
  according to the evidence above. Batch 3 is the high-drift component-family
  batch; the standalone HTML example Review rows can be pulled forward if that
  coverage is preferred.

### S004 — 2026-09-25 — Batch 3: highlighted search, story card/slider and carousel

- **Scope:** HTML-highlighted-search, HTML-story-card,
  HTML-carousel, TWIG-highlighted-search, TWIG-story-card,
  TWIG-story-card-card, TWIG-slider-pager, TWIG-carousel,
  TOOL-components-list, TOOL-component, TOOL-component-template and
  SUPPORT-runtime. The existing public IDs were preserved; slider-pager
  was delivered only as a shared dependency and no standalone HTML ID was
  invented.
- **Baseline and sources:** the linked upstream checkout remained clean on its
  moving v5-dev branch at cd0f615bd16816d8d99517192b1f817ae4a85618; the
  cycle remained pinned to tag v5.3.1 at
  0b3ca5a9190e1c32ff00fc092380e3a8f3571a05. The official EC homepage and
  component index and the versioned usage/showcase pages showed v5.3.1 and
  listed/rendered highlighted search, story card and carousel. The carousel
  usage guidance (visible controls, responsive content and no critical-task use)
  and story-card usage/accessibility navigation were checked alongside the
  v5.3.1 release notes/changelog for carousel
  Embla/teaser navigation, slider pager, story-card keyboard/context changes
  and highlighted-search labelling. Relevant tagged data, stories, README
  parameters and Jest snapshots were read from C/highlighted-search,
  C/story-card, C/slider, C/carousel and their D/components/... documentation
  paths. No newer release was observed.
- **Twig changes:** added exact tagged sources for
  highlighted-search.html.twig, story-card.html.twig,
  story-card-card.html.twig and slider-pager.html.twig; replaced the old
  carousel Twig with the exact tagged v5.3.1 source. Byte comparisons passed
  for all five files. The component-family map now returns the shared pager
  with carousel and story-card, while highlighted-search returns its own
  family. Existing form-group, button, icon, tag-set, picture and link Twig
  files remain shared dependencies rather than duplicated copies.
- **HTML changes:** added EC highlighted-search default/blue-mode form examples
  with valid labels, GET/POST action coverage, helper and suggestion
  relationships. Added story and testimonial variants with mobile carousel
  hooks, desktop tablist/panel relationships, pager controls and author/source
  metadata. Replaced the old carousel example with v5.3.1
  ecl-slider-pager, teaser navigation, counter, viewport, inert inactive
  slides and full-width/color-mode coverage, retaining image, credit and video
  banner examples. Remote media URLs remain the official demo references.
- **MCP checks:** a fresh stdio client reported 71 component IDs. The three
  affected component calls matched disk. Template calls returned exactly:
  highlighted-search → 1 key; story-card → story-card, story-card-card and
  slider-pager; carousel → carousel and slider-pager. All returned template
  values matched disk. The tooltip no-template contract remained unchanged.
- **Static checks:** HTML parser checks found no duplicate IDs, parse errors or
  missing aria-labelledby, aria-describedby or aria-controls targets in the
  three affected examples. Required ECL auto-init, slider, teaser, counter,
  inert-slide and Story Card tab hooks were asserted. node --check index.js,
  git diff --check and npm pack --dry-run passed; the package included all new
  HTML/Twig files and no upstream symlink. npm test -- --runInBand was
  attempted and reported no tests found; no Jest test suite or ESLint
  configuration exists in this repository.
- **Browser checks:** a temporary local HTTP page loaded the pinned v5.3.1
  EC CSS and JS, fetched all three examples, initialized them and exposed the
  labelled search fields, Story Card tabs/panels and carousel controls in the
  accessibility tree. Story Card Next changed the selected tab and details
  panel; Carousel Next advanced the visible slide and counter. The harness
  initialized the upstream registry map before ECL.autoInit() because the
  pinned Story Card implementation assumes that map already exists; no
  distribution asset was changed. The smoke was desktop-width only, so the
  story-card and carousel HTML rows remain Updated pending a mobile-width
  check. WebTools icon rendering remains blocked by the previously recorded
  ORB limitation; blank icon boxes in the local screenshot are environmental,
  not a replacement asset.
- **Handoff:** highlighted-search and all five worked Twig rows are Verified;
  story-card and carousel HTML are Updated with the responsive follow-up
  recorded above. Next: run that mobile-width smoke, then take the file and
  gallery families from Batch 3 with their dependencies.

### S005 — 2026-09-25 — Batch 4: file and gallery families

- **Scope:** completed the pending narrow-width smoke for HTML-story-card and
  HTML-carousel, then delivered HTML-file and HTML-gallery with the active
  file/gallery Twig families. The two local translation helper files remain on
  disk for traceability but are excluded from active EC lookup because the
  pinned file template inlines that markup and local reference auditing found
  no active callers.
- **Sources:** rechecked the official [EC component library](https://ec.europa.eu/component-library/ec/),
  the [v5.3.1 release](https://github.com/ec-europa/europa-component-library/releases/tag/v5.3.1),
  the tagged [source tree](https://github.com/ec-europa/europa-component-library/tree/v5.3.1)
  and [v5.3.1 changelog](https://github.com/ec-europa/europa-component-library/blob/v5.3.1/CHANGELOG.md).
  The pinned tag resolves to `0b3ca5a9190e1c32ff00fc092380e3a8f3571a05`.
  Reviewed the tagged file and gallery README, demo data, Storybook stories,
  snapshots and website usage/code/accessibility references. The release
  material covers the file redesign and gallery media/date behavior; the
  local target remains the published v5.3.1 tag, not the moving v5-dev checkout.
- **Twig changes:** replaced `components/file.html.twig`,
  `components/gallery.html.twig`, `components/gallery-item.html.twig` and
  `components/gallery-overlay.html.twig` with the exact tagged sources,
  normalizing only trailing whitespace. The file template now exposes the
  article/primary-meta/inline-translation contract, deprecated compatibility
  inputs and FileDownload hooks. The gallery family now exposes mixed-media,
  video-duration/publication-date, mobile action and overlay-date hooks.
- **HTML changes:** rebuilt `components/file.html` with default, labelled,
  translated, thumbnail/taxonomy and six EC color-mode examples. Rebuilt
  `components/gallery.html` with mixed images/videos, responsive pictures,
  grid/no-overlay/empty cases, EC color modes, captions, date/duration metadata,
  overlay controls and mobile action coverage. The HTML video caption track is
  an inline data resource so the example does not depend on an untracked local
  file.
- **MCP checks:** a fresh stdio client passed `guide_list` (18 topics),
  `components_list` (71 IDs), `component` for file/gallery/story-card/carousel,
  and `component_template` for file and gallery. File/gallery component
  responses matched the local `.html` examples exactly. The file template call
  returned `file.html.twig`; the gallery call returned exactly
  `gallery.html.twig`, `gallery-item.html.twig` and `gallery-overlay.html.twig`,
  and every returned template value matched disk.
- **Static checks:** HTML parsing found no duplicate IDs, parse errors or
  unresolved `aria-labelledby`, `aria-describedby` or `aria-controls` targets
  in the file/gallery examples. Required file translation, gallery media/date,
  overlay and auto-init hooks were asserted. Tagged Twig comparisons passed;
  `node --check index.js`, `git diff --check` and `npm pack --dry-run` passed.
  No project Jest suite or ESLint configuration exists, so no application test
  command was available to run.
- **Browser checks:** the temporary local page loaded the pinned v5.3.1 EC
  assets. After the harness seeded `ECL.components` after the bundle load,
  file translation expansion/collapse passed, gallery overlay opening and
  next-item navigation passed (counter 1 → 2 and video publication date shown),
  and the overlay closed successfully. At a temporary 250% zoom producing an
  effective narrow CSS width of about 357px, Story Card and Carousel Next
  advanced their content; the browser zoom was restored to 100% and DevTools
  closed afterward. WebTools font/icon requests still return the previously
  recorded 403/ORB limitation; no replacement asset was added.
- **Handoff:** file/gallery HTML and Twig rows, the completed Story Card and
  Carousel mobile follow-up, the file/gallery tool checks and runtime support
  are Verified. Next recommended batch: audit the remaining standalone media
  and content examples, starting with `HTML-video`, `HTML-media-container`,
  `HTML-text-media` and their shared picture/link dependencies; keep the
  external WebTools icon check and GUIDE-assets limitation recorded.

### S006 — 2026-09-25 — Batch 5: media, picture and link families

- **Scope:** `HTML-link`, `HTML-picture`, `HTML-video`,
  `HTML-media-container`, `HTML-text-media` and the paired
  `TWIG-link`, `TWIG-picture`, `TWIG-video`, `TWIG-media-container` and
  `TWIG-text-media` dependencies. The five HTML examples were checked as
  standalone component payloads and in the scoped page/grid harness used for
  responsive checks.
- **Sources:** rechecked the official [EC component library](https://ec.europa.eu/component-library/ec/),
  the [v5.3.1 release](https://github.com/ec-europa/europa-component-library/releases/tag/v5.3.1),
  the tagged [source tree](https://github.com/ec-europa/europa-component-library/tree/v5.3.1)
  and [v5.3.1 changelog](https://github.com/ec-europa/europa-component-library/blob/v5.3.1/CHANGELOG.md).
  The pinned tag remains `0b3ca5a9190e1c32ff00fc092380e3a8f3571a05`.
  Reviewed the tagged link, picture, video, media-container and text-media
  README/data/stories/snapshots plus the EC media-container, link and
  text-media usage/accessibility/code guidance. The live component homepage
  showed v5.3.1; the versioned source remained the conformance target.
- **Twig changes:** aligned `link.html.twig` and `picture.html.twig` exactly
  with the pinned v5.3.1 sources, including tertiary link types,
  `no_icon_wrapping`, focal-point/debug initialization and image pending
  attributes. `media-container.html.twig`, `text-media.html.twig` and
  `video.html.twig` were already byte-identical and passed the paired-family
  verification. No new Twig family or asset was invented.
- **HTML changes:** added tertiary and long-icon link coverage; added the
  picture focal-point/debug example and replaced untracked local placeholder
  media URLs with official EC demo media while preserving empty/source-alias
  edge cases; added media-container iframe titles, captions/credits and
  play/pause/video labels; and added accessible labels to video autoplay,
  partial, empty and color-mode preview cases. Text-media image/video,
  color-mode, link and nested media-container examples were audited without
  changing their established IDs or relationships.
- **MCP checks:** a fresh stdio client reported 71 component IDs and 18 guide
  topics. The five affected component responses matched disk. Each affected
  `component_template` call returned exactly its expected template key and
  every returned value matched disk; the starter response also remained
  unchanged and matched disk.
- **Static checks:** the focused HTML parser found no duplicate IDs, unresolved
  ARIA references, iframe without titles, controls/autoplay video without
  labels or play/pause button without labels. Focal-point initialization was
  asserted. `node --check index.js`, `git diff --check` and the final
  `npm pack --dry-run` passed. `npm test -- --runInBand` still reports no tests
  found, and `npm run lint` still has no ESLint configuration; no Laravel code
  was changed.
- **Browser checks:** the temporary page loaded pinned v5.3.1 EC assets and
  initialized all five families. Picture focal-point initialization completed
  with no missing local media requests; iframe titles, media play/pause state,
  expandable content and link labels were checked. At 375px, scoped
  text-media, media-container and link content stayed within their grid/page
  context, with no console errors or warnings. Remote media availability can
  still leave a video paused after a play request; this is an external media
  condition, not a markup/runtime error. WebTools icon/font loading remains
  blocked by the previously recorded ORB limitation.
- **Handoff:** all ten S006 HTML/Twig rows and the affected MCP checks are
  Verified. The next recommended batch is `HTML-table`, `HTML-news-ticker`,
  `TWIG-table` and `TWIG-news-ticker`, including required helpers. No commit or
  push was made.

### S007 — 2026-09-25 — Batch 6: table and news-ticker families

- **Scope:** `HTML-table`, `HTML-news-ticker`, `TWIG-table` and
  `TWIG-news-ticker`. The table work includes the new filterable example and
  the existing simple, zebra, multi-header and extension cases. The news-ticker
  work includes valid multi-slide, single-item, empty-output and EC color-mode
  coverage.
- **Sources:** rechecked the official [EC component library](https://ec.europa.eu/component-library/ec/),
  the [v5.3.1 release](https://github.com/ec-europa/europa-component-library/releases/tag/v5.3.1),
  the tagged [source tree](https://github.com/ec-europa/europa-component-library/tree/v5.3.1)
  and [v5.3.1 changelog](https://github.com/ec-europa/europa-component-library/blob/v5.3.1/CHANGELOG.md).
  The live homepage still showed v5.3.1; no newer release was observed and the
  pinned commit remains `0b3ca5a9190e1c32ff00fc092380e3a8f3571a05`.
  Reviewed the tagged table/news-ticker README, demo data, stories, snapshots,
  JS hooks and EC usage/accessibility/API/code documentation. The relevant
  changelog entries are table filtering and the news-ticker redesign in 5.3.0;
  v5.3.1 contains no further change to either family.
- **Twig changes:** replaced both differing local files with the exact tagged
  v5.3.1 Twig. Table now exposes filter parameters and hooks in addition to
  sorting. News ticker now supports color mode, Phosphor/default newspaper
  media, slide icon/content wrappers, branded links, deprecated image input
  compatibility and an LTR counter.
- **HTML changes:** added the table sort marker and a multi-row filter example
  with labelled column fields created by the runtime; existing table variants
  and extension hooks remain. Reworked the ticker examples to the new slide
  wrappers and Phosphor icon contract, retained custom labels and EC color-mode
  classes, and removed auto-init from empty static swatches so the browser does
  not initialize an invalid zero-slide ticker.
- **MCP checks:** a fresh local stdio client reported all six tools, 18 guides
  and 71 components. `components_list`, both affected `component` calls and
  both affected `component_template` calls matched the files on disk; the
  starter response also matched disk.
- **Static checks:** `node --check index.js`, `git diff --check`, the focused
  hook/duplicate-ID assertions and `npm pack --dry-run` passed. The package
  declares Jest but has no test files, so `npm test -- --runInBand` remains a
  no-tests result; ESLint has no project configuration, so `npm run lint`
  remains a configuration failure. No Laravel code was changed.
- **Browser checks:** a temporary page loaded the pinned local EC CSS/JS and
  initialized the valid table and ticker roots. Table filtering narrowed the
  Organization column to the EU-LISA row; the sortable header toggled its
  direction label; and the ticker next control advanced the visible counter.
  The accessible tree showed generated filter labels/inputs, initialized
  hooks, branded links, valid slide wrappers and no duplicate IDs. Empty and
  static color-mode roots were deliberately not auto-initialized because the
  tagged NewsTicker JS expects at least one slide.
- **Handoff:** all four S007 HTML/Twig rows and affected MCP checks are
  Verified. The next recommended batch is `HTML-accordion` and
  `TWIG-accordion`, including required nested helpers. GUIDE-assets/GUIDE-icons
  WebTools rendering remains pending because the external loader is still
  blocked; no commit or push was made.

### S008 — 2026-09-25 — Batch 7: accordion family

- **Scope:** `HTML-accordion` and `TWIG-accordion`. The example retains useful
  EC-specific coverage while adopting the tagged native details/summary
  contract: four-item default data with the third item open, a named exclusive
  group, a configurable collapsible sidebar, a single non-plus indicator,
  structured content, extension hooks and the non-default EC color modes.
- **Sources:** rechecked the official [EC component library](https://ec.europa.eu/component-library/ec/),
  the [v5.3.1 release](https://github.com/ec-europa/europa-component-library/releases/tag/v5.3.1),
  the tagged [accordion source](https://github.com/ec-europa/europa-component-library/tree/v5.3.1/src/components/accordion),
  the tagged [EC accordion documentation source](https://github.com/ec-europa/europa-component-library/tree/v5.3.1/src/website/src/pages/ec/components/accordion)
  and [v5.3.1 changelog](https://github.com/ec-europa/europa-component-library/blob/v5.3.1/CHANGELOG.md).
  The live homepage still showed v5.3.1; no newer release was observed and the
  pinned commit remains `0b3ca5a9190e1c32ff00fc092380e3a8f3571a05`. Relevant
  changelog changes between the prior baseline and target include the native
  accordion markup, sidebar variant, configurable sidebar media query, default
  open items, EC open-item background and sidebar background reset.
- **Twig changes:** aligned `components/accordion.html.twig` byte-for-byte
  with the pinned v5.3.1 source. The template now documents and emits the
  `open` item parameter and, for sidebar examples, the
  `data-ecl-accordion-sidebar-media-query` root attribute while preserving
  icon fallback, color modes, exclusive `name`, custom classes and attributes.
  No nested accordion helper is required; the icon template remains a separate
  shared component contract.
- **HTML changes:** updated the default example to the tagged four-item EC
  demo shape with the third item initially open, corrected the stale v5.0.1
  wording, and added the v5.3.1 configurable sidebar hook. Existing exclusive,
  single-icon, structured-content, extension-hook and color-mode examples were
  retained and checked for valid nesting, unique IDs and current initialization
  hooks.
- **MCP checks:** a fresh local stdio client reported all six tools, 18 guides
  and 71 components. The accordion component response matched disk; its
  `component_template` response returned exactly `accordion.html.twig` and
  matched disk; the accordion remained discoverable from `components_list`; the
  starter response also matched disk.
- **Static checks:** the exact tagged Twig comparison, focused accordion
  structure/hook/duplicate-ID assertions, `node --check index.js`,
  `git diff --check` and `npm pack --dry-run` passed. `npm test -- --runInBand`
  still reports no tests found, and `npm run lint` still has no ESLint
  configuration. No Laravel code was changed.
- **Browser checks:** a temporary page loaded the pinned local EC CSS/JS and
  initialized all 21 accordion roots without console errors or warnings. The
  default third item was open initially; ordinary items toggled independently;
  the named group closed its first item when the second opened; and the
  sidebar's `(min-width: 768px)` hook kept its filter panel open at desktop
  width. The accessibility tree exposed the filter label/input and action
  buttons. WebTools icon rendering remains blocked by the previously recorded
  external loader limitation.
- **Handoff:** both S008 accordion rows and affected MCP checks are Verified.
  The next recommended batch is `HTML-description-list` and
  `TWIG-description-list`, including required list helpers. GUIDE-assets/
  GUIDE-icons WebTools rendering remains pending; no commit or push was made.

### S009 — 2026-09-25 — Batch 8: description-list family

- **Scope:** `HTML-description-list` and `TWIG-description-list`, with the
  existing `link.html.twig` and `tag.html.twig` helper contracts checked as
  dependencies. The example covers the current vertical and horizontal list
  demos, collapsible definitions, standalone and inline links, external and
  social icons, link tags, taxonomy links, extension attributes, omission
  branches and EC color modes.
- **Sources:** rechecked the official [EC component library](https://ec.europa.eu/component-library/ec/),
  the [v5.3.1 release](https://github.com/ec-europa/europa-component-library/releases/tag/v5.3.1),
  the tagged [description-list source](https://github.com/ec-europa/europa-component-library/tree/v5.3.1/src/components/description-list),
  the tagged [EC Lists documentation source](https://github.com/ec-europa/europa-component-library/tree/v5.3.1/src/website/src/pages/ec/components/list)
  and [v5.3.1 changelog](https://github.com/ec-europa/europa-component-library/blob/v5.3.1/CHANGELOG.md).
  The live homepage still showed v5.3.1; no newer release was observed and the
  pinned commit remains `0b3ca5a9190e1c32ff00fc092380e3a8f3571a05`. Relevant
  changes between the prior baseline and target include description-list text
  wrapping, the button-based “show more” control, focus on the first revealed
  item, the inline-link fallback and the current API documentation for
  retrieving an existing instance.
- **Twig changes:** aligned `components/description-list.html.twig` byte-for-
  byte with the pinned v5.3.1 source. The inline-link branch now trims output
  consistently and accepts either a link object or plain text definition,
  matching the tagged fallback. The separate link and tag Twig dependencies
  are already byte-identical to v5.3.1; no helper change was required.
- **HTML changes:** updated the vertical example to the tagged nine-item data
  shape, including the long wrapping link, Mastodon icon, seven tags and six
  taxonomy entries. Added runtime hooks to the horizontal variant, supplied
  representative links/tags for its responsive layout, and separated the
  term-only and definition-only omission branches. Existing extension and
  color-mode coverage remains.
- **MCP checks:** a fresh local stdio client reported all six tools, 18 guides
  and 71 components. The description-list component response matched disk; its
  `component_template` response returned exactly `description-list.html.twig`
  and matched disk; the component remained discoverable from
  `components_list`; and the starter response also matched disk.
- **Static checks:** the exact tagged Twig comparison, byte-identical link/tag
  dependency checks, focused structure/hook/color-mode/duplicate-ID assertions,
  `node --check index.js` and `git diff --check` passed. `npm pack --dry-run`
  includes both description-list files. `npm test -- --runInBand` still reports
  no tests found, and `npm run lint` still has no ESLint configuration. No
  Laravel code was changed.
- **Browser checks:** a temporary page loaded the pinned local EC CSS/JS and
  initialized the two description-list roots with runtime hooks. The tagged JS
  inserted five accessible “Show more items” buttons, hid excess definition
  items, and after activation focused the first revealed link (`Standalone link
  3`). The accessibility tree exposed the external-link label and the
  horizontal variant. The browser console reported no errors or warnings;
  WebTools icon rendering remains blocked by the previously recorded external
  loader limitation.
- **Handoff:** both S009 description-list rows and affected MCP checks are
  Verified. The next recommended batch is `HTML-fact-figures` and
  `TWIG-fact-figures`, including required helpers. GUIDE-assets/GUIDE-icons
  WebTools rendering remains pending; no commit or push was made.

### S010 — 2026-09-25 — Batch 9: fact-figures family

- **Scope:** `HTML-fact-figures` and `TWIG-fact-figures`, with the existing
  `link.html.twig` and `icon.html.twig` helpers checked as dependencies. The
  example covers 1–4 columns, centered and icon-free variants, large and medium
  value sizing, value/title fallbacks, per-item and global sources, plain-text
  and linked sources, long external source labels, view-all links, extension
  attributes, empty output and all EC color modes.
- **Sources:** rechecked the official [EC component library](https://ec.europa.eu/component-library/ec/),
  the [v5.3.1 release](https://github.com/ec-europa/europa-component-library/releases/tag/v5.3.1),
  the tagged [fact-figures source](https://github.com/ec-europa/europa-component-library/tree/v5.3.1/src/components/fact-figures),
  the tagged [Fact and figures documentation](https://github.com/ec-europa/europa-component-library/tree/v5.3.1/src/website/src/pages/ec/components/fact-figures)
  and the [v5.3.1 changelog](https://github.com/ec-europa/europa-component-library/blob/v5.3.1/CHANGELOG.md).
  The live homepage still showed v5.3.1, and the pinned commit remains
  `0b3ca5a9190e1c32ff00fc092380e3a8f3571a05`. Relevant changes from the prior
  baseline include per-item sources and the v5.3.1 source-wrapping fixes for
  linked sources, including the `no_icon_wrapping` contract.
- **Twig changes:** replaced the older local template with the exact pinned
  v5.3.1 source. It now defines the tagged source-rendering macro, supports
  per-item source labels and mixed source objects, preserves global sources,
  prevents source icons from wrapping away from long labels, and retains the
  current value/title, icon, extension-attribute and view-all behavior. The
  existing link and icon Twig dependencies are byte-identical to v5.3.1; no
  helper change was required.
- **HTML changes:** added representative item-level source markup to the
  default example, including a long external link, ordinary link and plain text;
  retained global sources and all prior column, centered, icon-free, view-all,
  empty and color-mode coverage. No static script or documentation-site-only
  dependency was added.
- **MCP checks:** a fresh local stdio client reported all six tools, 18 guides
  and 71 components. The fact-figures component response matched disk; its
  `component_template` response returned exactly `fact-figures.html.twig` and
  matched disk; the component remained discoverable from `components_list`.
- **Static checks:** exact tagged Twig comparison, byte-identical link/icon
  dependency checks, focused structure/column/source/color-mode/duplicate-ID
  assertions, `node --check index.js` and `git diff --check` passed. The package
  dry-run includes both fact-figures files. `npm test -- --runInBand` still
  reports no tests found, and `npm run lint` still has no ESLint configuration.
  `tidy` reports only expected HTML5/ARIA warnings for the standalone component
  fragment; no parse error was reported. No Laravel code was changed.
- **Browser checks:** a temporary page loaded the pinned local EC CSS/JS and
  rendered 21 fact-figures roots and 26 items, including the per-item/global
  source structures, two external-link icons and two view-all links. The browser
  console reported no errors or warnings. The screenshot showed the default
  source layout and long-label wrapping; WebTools icon glyph rendering remains
  limited by the previously recorded external loader issue.
- **Handoff:** both S010 fact-figures rows and affected MCP checks are Verified.
  The next recommended batch is the forms and page-summary high-drift families,
  including required shared Twig dependencies. GUIDE-assets/GUIDE-icons WebTools
  rendering remains pending; no commit or push was made.

### S011 — 2026-09-25 — Batch 10: form-group, search-form and page-summary families

- **Scope:** `HTML/TWIG-form-group`, `HTML/TWIG-search-form` and
  `HTML/TWIG-page-summary`. The batch keeps the three form/page-summary changes
  coherent: form-group supplies the label and input relationships used by the
  search form, while page-summary supplies the matching color-mode and labelling
  coverage. The page-summary HTML was a justified no-change decision because it
  already contained the target variants.
- **Sources:** rechecked the official [EC component library](https://ec.europa.eu/component-library/ec/),
  the [v5.3.1 release](https://github.com/ec-europa/europa-component-library/releases/tag/v5.3.1),
  the tagged [form-group source](https://github.com/ec-europa/europa-component-library/tree/v5.3.1/src/components/form-group),
  [search-form source](https://github.com/ec-europa/europa-component-library/tree/v5.3.1/src/components/search-form),
  [page-summary source](https://github.com/ec-europa/europa-component-library/tree/v5.3.1/src/components/page-summary)
  and the [v5.3.1 changelog](https://github.com/ec-europa/europa-component-library/blob/v5.3.1/CHANGELOG.md).
  The live homepage still showed v5.3.1, and the pinned commit remains
  `0b3ca5a9190e1c32ff00fc092380e3a8f3571a05`.
- **Twig changes:** aligned all three templates byte-for-byte with the pinned
  source. Form-group now uses the label-wrapper/inner-label contract and keeps
  required or optional indicators visible alongside hidden labels; search-form
  removes the duplicate `role="search"` from its form wrapper; page-summary
  supports the tagged `color_mode` parameter and class handling.
- **HTML changes:** refreshed form-group coverage for required, optional,
  helper, invalid, select, textarea, datepicker, checkbox, radio, range, file,
  rating, hidden-label, disabled, extension and empty branches, plus all 15 EC
  color modes. Refreshed search-form coverage for default, extension,
  disabled, placeholder fallback, no-button, no-input and all 15 color modes.
  Page-summary retained its title/description, icon, list, title-only,
  extension, deterministic-ID and 15 color-mode variants without mutation.
- **Dependency checks:** datepicker, file-upload, select, text-area, text-input,
  checkbox-group, checkbox-item, radio-group and radio-button Twig helpers are
  byte-identical to v5.3.1. Range and rating-field remain pre-existing includes
  in form-group and are not standalone local helper files; their rows remain for
  the next forms audit.
- **MCP checks:** a fresh local stdio client reported all six tools, 18 guides
  and 71 components. All three component responses matched disk; each
  `component_template` call returned its exact expected key and byte-identical
  value; all three families remained discoverable from `components_list`.
- **Static checks:** exact tagged Twig comparisons, dependency comparisons,
  duplicate-ID/ARIA/role/color-mode assertions, `node --check index.js` and
  `git diff --check` passed. The browser DOM contained 28 form groups, 27
  label wrappers/inner labels, 21 search forms with no `role="search"` form,
  20 search buttons, and 20 page-summary roots/headings including 15 color
  modes. Standalone fragment checks retain expected HTML5/custom-element/ARIA
  warnings; they are not full-document validation. `npm test -- --runInBand`
  still reports no tests found, and `npm run lint` still has no ESLint
  configuration. No Laravel code was changed.
- **Browser checks:** a temporary page loaded the pinned local EC CSS/JS and
  exposed the form controls, search branches and page-summary headings in the
  accessibility tree. The browser console reported no errors or warnings;
  WebTools icon rendering remains limited by the previously recorded external
  loader issue.
- **Handoff:** all six S011 rows and affected MCP checks are Verified. The next
  recommended batch is the remaining checkbox, datepicker, file-upload, radio,
  select, text-area and text-input families, with range/rating-field coverage
  reconciled while exercising the shared form-group branches. GUIDE-assets and
  GUIDE-icons WebTools rendering remain pending; no commit or push was made.

### S012 — 2026-09-25 — Batch 11: remaining form families

- **Scope:** `HTML/TWIG-checkbox`, `TWIG-checkbox-group`,
  `TWIG-checkbox-item`, `HTML/TWIG-datepicker`, `HTML/TWIG-file-upload`,
  `TWIG-file-upload`, `HTML/TWIG-radio`, `TWIG-radio-group`,
  `TWIG-radio-button`, `HTML/TWIG-select`, `HTML/TWIG-text-area` and
  `HTML/TWIG-text-input`. The existing HTML already contained the complete
  target-oriented coverage, so this was a verified no-content-change audit.
- **Sources:** rechecked the official [EC component library](https://ec.europa.eu/component-library/ec/),
  the [v5.3.1 release](https://github.com/ec-europa/europa-component-library/releases/tag/v5.3.1),
  the tagged form component sources and their README/demo data, the tagged EC
  documentation pages for [checkbox](https://github.com/ec-europa/europa-component-library/tree/v5.3.1/src/website/src/pages/ec/components/forms/checkbox),
  [datepicker](https://github.com/ec-europa/europa-component-library/tree/v5.3.1/src/website/src/pages/ec/components/forms/datepicker),
  [file upload](https://github.com/ec-europa/europa-component-library/tree/v5.3.1/src/website/src/pages/ec/components/forms/file-upload),
  [radio](https://github.com/ec-europa/europa-component-library/tree/v5.3.1/src/website/src/pages/ec/components/forms/radio),
  [select](https://github.com/ec-europa/europa-component-library/tree/v5.3.1/src/website/src/pages/ec/components/forms/select),
  [text area](https://github.com/ec-europa/europa-component-library/tree/v5.3.1/src/website/src/pages/ec/components/forms/text-area),
  [text field](https://github.com/ec-europa/europa-component-library/tree/v5.3.1/src/website/src/pages/ec/components/forms/text-field)
  and the [v5.3.1 changelog](https://github.com/ec-europa/europa-component-library/blob/v5.3.1/CHANGELOG.md).
  Relevant target changes include required/optional text remaining visible with
  hidden labels, checkbox/radio disabled colors, datepicker focus behavior,
  file-upload focus behavior and select alignment fixes.
- **Twig checks:** all nine local Twig helpers are byte-identical to their
  pinned v5.3.1 sources: checkbox group/item, datepicker, file-upload, radio
  group/button, select, text-area and text-input. No template mutation was
  required.
- **HTML checks:** checkbox and radio examples cover groups/items, required or
  optional indicators, helper/invalid/disabled states, binary/minimal/empty
  branches and all 15 EC color modes. Datepicker covers Duet markup, default,
  required, disabled, invalid, custom, empty, min/max, first-day and 15 color
  modes. File-upload covers single/multiple, optional/disabled/invalid/empty,
  extension attributes, selected-file list hooks and 15 color modes. Select
  covers single/multiple, option groups/states, widths, invalid/disabled,
  extension hooks, multiple search/select-all/submit/clear and 15 color modes.
  Text-area and text-input cover their status, type/value, width, extension,
  empty and 15 color-mode branches. No HTML mutation was required.
- **MCP checks:** a fresh local stdio client checked all six tools, 18 guides
  and 71 components; each of the seven HTML component responses matched disk,
  each of the nine `component_template` responses returned the expected key and
  byte-identical value, and all seven families remained discoverable. The
  missing `file-upload-status` composition remains unresolved for a later
  explicit coverage decision.
- **Static/browser checks:** exact tagged Twig comparisons, duplicate-ID checks,
  input/label and `aria-describedby` checks, `node --check index.js` and
  `git diff --check` passed. A temporary page loaded all seven examples with
  the pinned EC CSS/JS: 172 unique IDs, 21 Duet date-picker elements, 22 file
  inputs, 24 selects, 24 radios, 22 checkboxes, 25 text areas and 29 text
  inputs. The browser exposed the controls in the accessibility tree; select,
  file-upload and datepicker hooks were present; the console reported no errors
  or warnings. Standalone fragment validation retains the expected HTML5,
  custom-element and ARIA warnings.
- **Handoff:** all 16 S012 rows are Verified. The next recommended batch is
  range/rating-field plus an explicit assessment of the missing
  `file-upload-status` composition. GUIDE-assets and GUIDE-icons WebTools
  rendering remain pending. This S012 tracker update is not yet committed or
  pushed.

### S013 — 2026-09-25 — Batch 12: range, rating-field and file-upload-status

- **Scope:** `HTML/TWIG-range`, `HTML/TWIG-rating-field` and
  `TWIG-file-upload-status`. The batch combines the remaining form controls
  with the file-upload status composition that the official file-upload usage
  guidance links as an upload-progress/removal companion.
- **Sources:** rechecked the official [EC component library](https://ec.europa.eu/component-library/ec/),
  the [v5.3.1 release](https://github.com/ec-europa/europa-component-library/releases/tag/v5.3.1),
  the tagged [range source](https://github.com/ec-europa/europa-component-library/tree/v5.3.1/src/components/range),
  [rating-field source](https://github.com/ec-europa/europa-component-library/tree/v5.3.1/src/components/rating-field),
  the [file-upload-status composition](https://github.com/ec-europa/europa-component-library/tree/v5.3.1/src/compositions/file-upload-status),
  their README/demo/test snapshot sources and the [v5.3.1 changelog](https://github.com/ec-europa/europa-component-library/blob/v5.3.1/CHANGELOG.md).
  The range/rating sources are part of the EC forms navigation; file-upload
  usage explicitly links the status composition for progress and removal.
- **Twig changes:** aligned `rating-field.html.twig` to the exact v5.3.1
  source. The target keeps rating items in ascending order and emits each
  accessible label before its radio input; the previous local template reversed
  items and emitted inputs first. `range.html.twig` was already exact. Added
  the exact `file-upload-status.html.twig` source and mapped it into the
  file-upload family in `index.js`, preserving EC-scoped discovery without
  inventing a standalone HTML component ID.
- **HTML changes:** updated rating-field examples to the target label-before-
  input order and ascending values across required, checked, disabled, minimal,
  empty and 15 color-mode cases. Expanded range color-mode coverage so every
  EC mode contains a real initialized slider rather than an empty wrapper;
  existing required, disabled, invalid, width, extension and empty cases remain.
- **MCP checks:** a fresh local stdio client checked all six tools, 18 guides
  and 71 component IDs. Range and rating-field component responses matched
  disk; their Twig template responses matched exact disk content; the
  file-upload family returned both `file-upload.html.twig` and
  `file-upload-status.html.twig`, both matching disk; all affected families
  remained discoverable.
- **Static/browser checks:** exact tagged comparisons, rating label/input order,
  range hook/ID/ARIA checks, `node --check index.js` and `git diff --check`
  passed. The file-upload-status source is byte-identical to its tagged
  composition and reuses the local spinner/link helpers. Browser smoke covered
  range initialization and accessible rating controls with no console errors or
  warnings. `npm pack --dry-run` includes the new helper and affected files.
  `npm test -- --runInBand` still reports no tests found, and `npm run lint`
  still has no ESLint configuration. No Laravel code was changed.
- **Handoff:** all five S013 rows are Verified. The next recommended batch is
  the remaining high-drift quiz, slogan-ticker, social-media-follow and
  splash-page families. GUIDE-assets and GUIDE-icons WebTools rendering remain
  pending. This S013 work is ready to commit and push.

### S014 — 2026-09-25 — Batch 13: quiz, slogan-ticker, social-media-follow and splash-page

- **Scope:** `HTML/TWIG-quiz`, `TWIG-quiz-card`, `HTML/TWIG-slogan-ticker`,
  `HTML/TWIG-social-media-follow` and `HTML/TWIG-splash-page`. This completes
  the four remaining high-drift content families selected by the previous
  handoff.
- **Sources:** rechecked the official [EC component library](https://ec.europa.eu/component-library/ec/),
  the [v5.3.1 release](https://github.com/ec-europa/europa-component-library/releases/tag/v5.3.1),
  the tagged quiz, slogan-ticker, social-media-follow and splash-page source
  directories, their README/demo/story/test snapshot files and the
  [v5.3.1 changelog](https://github.com/ec-europa/europa-component-library/blob/v5.3.1/CHANGELOG.md).
  The pinned target remains `0b3ca5a9190e1c32ff00fc092380e3a8f3571a05`.
- **Twig changes:** restored exact pinned v5.3.1 sources for quiz and its
  quiz-card helper, slogan-ticker, social-media-follow and splash-page. The
  changes cover the shared slider pager and counter, quiz color mode and card
  propagation, updated ticker screen-reader defaults, single-link div/list
  semantics and single-item language-category tags.
- **HTML changes:** updated quiz pager hooks/dot template/counter; changed the
  default ticker labels to Continue scrolling/Pause scrolling; added the
  single-link social and single-language splash `div` branches; corrected the
  splash logo examples to the packaged EC asset paths; and preserved
  multi-link/list coverage plus extension, empty, active, responsive and all
  15 EC color-mode examples.
- **MCP checks:** a fresh local stdio client checked all six tools. Quiz,
  slogan-ticker, social-media-follow and splash-page responses matched disk;
  quiz returned both `quiz.html.twig` and `quiz-card.html.twig`, and each other
  family returned its exact Twig helper. All four families remained listed and
  discoverable.
- **Static/browser checks:** exact tagged Twig comparisons, unique-ID and
  semantic-nesting checks, `node --check index.js` and `git diff --check`
  passed. Browser smoke initialized 35 ECL roots with 15 color modes, exposed
  the new quiz pager, advanced the narrow quiz to `2 / 2`, toggled ticker
  pause/resume, and confirmed the single-link/single-language DOM semantics;
  no console errors or warnings were recorded. `npm test -- --runInBand`
  still reports no tests found, and `npm run lint` still has no ESLint
  configuration. No Laravel code was changed.
- **Handoff:** all nine S014 rows are Verified. The next recommended batch is
  breadcrumb, inpage-navigation and navigation-list with their paired item
  helpers. GUIDE-assets and GUIDE-icons WebTools rendering remain pending.

### S015 — 2026-09-25 — Batch 14: breadcrumb, inpage-navigation and navigation-list

- **Scope:** `HTML/TWIG-breadcrumb`, `HTML/TWIG-inpage-navigation`,
  `HTML-navigation-list`, `TWIG-navigation-list-item` and
  `TWIG-navigation-list`. Existing Twig was already byte-identical to the
  pinned target; this batch completed the paired example and runtime audit.
- **Sources:** rechecked the official [EC component library](https://ec.europa.eu/component-library/ec/),
  the [v5.3.1 release](https://github.com/ec-europa/europa-component-library/releases/tag/v5.3.1),
  the tagged breadcrumb, inpage-navigation and navigation-list source
  directories, README/demo/story/test snapshot/JS files and the
  [v5.3.1 changelog](https://github.com/ec-europa/europa-component-library/blob/v5.3.1/CHANGELOG.md).
  The pinned target remains `0b3ca5a9190e1c32ff00fc092380e3a8f3571a05`.
- **Twig and HTML:** no component source mutation was needed. Breadcrumb
  covers empty, single, two-item, simple, long/custom ellipsis, extensions and
  all 15 EC color modes. In-page navigation covers desktop/mobile hooks, six
  valid heading targets, active/runtime, extension/empty cases and all 15
  color modes. Navigation-list covers two/three columns, border propagation,
  picture/image and illustration variants, mixed link groups, extensions,
  unsupported columns and all 15 color modes.
- **MCP checks:** a fresh local stdio client listed all six tools; all three
  component responses matched disk; breadcrumb and inpage-navigation returned
  their exact Twig templates; navigation-list returned both exact
  `navigation-list.html.twig` and `navigation-list-item.html.twig` templates;
  all three families remained discoverable.
- **Static/browser checks:** exact tagged Twig comparisons, duplicate-ID and
  ARIA target checks, link-to-heading checks, color-mode coverage,
  `node --check index.js` and `git diff --check` passed. Browser smoke loaded
  the three examples with six initialized roots and no console errors or
  warnings; desktop breadcrumb ellipsis expansion and narrow collapse passed;
  navigation-list accessibility and media/variant structure passed. The
  pinned v5.3.1 inpage-navigation bundle binds the mobile trigger twice, so a
  single click opens and immediately closes the list; the two inpage rows stay
  `Updated` pending an upstream/bundle decision rather than changing the
  vendored pinned asset.
- **Checks and handoff:** `npm test -- --runInBand` still reports no tests
  found, and `npm run lint` still has no ESLint configuration. No Laravel code
  was changed. Five S015 rows are Verified and two remain Updated. S016 follows
  with pagination, tabs and skip-link navigation; keep the inpage bundle
  decision visible for the next navigation batch. GUIDE-assets and GUIDE-icons
  WebTools rendering remain pending.

### S016 — 2026-09-25 — Batch 15: pagination, tabs and skip-link navigation

- **Scope:** `HTML/TWIG-pagination`, `HTML/TWIG-tabs` and
  `HTML/TWIG-skip-link`. The three Twig files were already byte-identical to
  the pinned v5.3.1 sources; this batch completed their dependency, paired
  example and runtime audit.
- **Sources:** rechecked the official [EC component library](https://ec.europa.eu/component-library/ec/),
  the [v5.3.1 release](https://github.com/ec-europa/europa-component-library/releases/tag/v5.3.1),
  tagged README/demo/data/Story/test snapshot/accessibility/API/JS/SCSS files,
  and the [v5.3.1 changelog](https://github.com/ec-europa/europa-component-library/blob/v5.3.1/CHANGELOG.md).
  The pinned target remains `0b3ca5a9190e1c32ff00fc092380e3a8f3571a05`.
- **Twig and HTML:** pagination and skip-link source markup has no v5.3.1
  change. Tabs includes the v5.3.1 runtime breakpoint and listener-cleanup
  behavior; the local example was expanded to 10 default and 8 content-managed
  items, and its stale v5.0.1 text was corrected to the pinned runtime.
  Pagination and skip-link examples retain their long/short/empty, extension,
  accessibility-label and all-15-color-mode coverage.
- **MCP checks:** live connected calls returned 71 components, 18 guides and
  the starter template; all three component responses and their exact single
  Twig template keys/values matched disk. A fresh local stdio client repeated
  the exact comparisons and discoverability checks.
- **Static/browser checks:** no duplicate IDs, 15 EC color modes, 19 pagination
  navs with 18 current markers, 8 Tabs content targets, 10 default Tabs items
  and 19 skip links passed. `node --check index.js` and `git diff --check`
  passed. Chrome smoke loaded the local v5.3.1 assets with 200/304 requests;
  the harness had only its expected favicon 404. Tabs content activation,
  desktop overflow, forced 320px responsive Previous/Next controls, pagination
  labels and skip-link keyboard focus/navigation to `#top` passed. No runtime
  failure was observed.
- **Checks and handoff:** `npm test -- --runInBand` still reports no tests
  found, and `npm run lint` still has no ESLint configuration. No Laravel code
  was changed. All six S016 rows are Verified. The two S015 inpage-navigation
  rows remain Updated because the pinned bundle's duplicate mobile-trigger
  listener still needs an upstream/bundle decision. Next take menu, mega-menu
  and page-header with their site-wide helpers and runtime behavior; keep
  GUIDE-assets/GUIDE-icons WebTools rendering pending until the external loader
  is reachable.

### S017 — 2026-09-25 — Batch 16: menu, mega-menu and page-header navigation

- **Scope:** `HTML/TWIG-menu`, `HTML/TWIG-mega-menu`, `HTML/TWIG-page-header` and
  their paired helpers. The target remains the pinned commit
  `0b3ca5a9190e1c32ff00fc092380e3a8f3571a05`.
- **Sources:** rechecked the official [EC component library](https://ec.europa.eu/component-library/ec/),
  the [v5.3.1 release](https://github.com/ec-europa/europa-component-library/releases/tag/v5.3.1),
  tagged navigation/site-wide demos, source, tests, snapshots and the
  [v5.3.1 changelog](https://github.com/ec-europa/europa-component-library/blob/v5.3.1/CHANGELOG.md).
- **Twig and HTML:** all seven paired Twig files match the pinned EC sources
  semantically; `mega-menu.html.twig` and `mega-menu-item.html.twig` retain
  whitespace-only local formatting differences. The menu examples now give each of the 15 color modes a
  complete auto-initializable menu, while the intentionally empty menu stays
  static because the pinned runtime dereferences an optional toggle during
  initialization. The mega-menu example now exercises the pinned current-page
  class/title contract; page-header coverage required no HTML mutation.
- **MCP checks:** a fresh stdio client returned 71 component IDs and 18 guide
  topics. `component` responses for menu, mega-menu and page-header contained
  the expected hooks; their component-template calls returned the exact family
  keys (menu: 2, mega-menu: 3, page-header: 2), with non-empty values matching
  the local files.
- **Static/browser checks:** the clean Chrome harness loaded the local v5.3.1
  CSS/JS with no console errors. It initialized 17/17 runtime-capable menu
  examples, 18/18 mega-menu examples and the expandable page-header; it found
  no duplicate IDs or broken ARIA references, one current mega-menu item and
  all 15 EC color modes. The page-header toggle opened/closed its panel with
  synchronized `aria-expanded`/`hidden`; the mega-menu opened and closed on
  Escape. The menu toggle is hidden at the desktop viewport, so mobile-toggle
  activation remains a responsive-viewport follow-up rather than an invented
  desktop result.
- **Checks and handoff:** `node --check index.js` and `git diff --check` pass.
  `npm test -- --runInBand` still reports no tests found, and `npm run lint`
  still has no ESLint configuration. No Laravel code was changed. All ten S017
  rows are Verified. The two S015 inpage-navigation rows remain Updated because
  the pinned bundle's duplicate mobile-trigger listener still needs an
  upstream/bundle decision. GUIDE-assets and GUIDE-icons WebTools rendering
  remain pending until the external loader is reachable. Next take modal,
  popover and notification with their paired helpers and runtime behavior.

### S018 — 2026-09-25 — Batch 17: modal, popover and notification interaction

- **Scope:** `HTML/TWIG-modal`, `HTML/TWIG-popover` and
  `HTML/TWIG-notification`, including the 15 EC color-mode examples and the
  pinned runtime contracts. The target remains commit
  `0b3ca5a9190e1c32ff00fc092380e3a8f3571a05` (v5.3.1).
- **Sources:** rechecked the official [EC component library](https://ec.europa.eu/component-library/ec/),
  the [v5.3.1 release](https://github.com/ec-europa/europa-component-library/releases/tag/v5.3.1),
  tagged modal/popover/notification README, demo data, stories, tests,
  snapshots, JS, SCSS, package dependencies and EC usage/accessibility/API
  sources, plus the [v5.3.1 changelog](https://github.com/ec-europa/europa-component-library/blob/v5.3.1/CHANGELOG.md).
  The relevant release history includes modal focus-style clipping prevention,
  body-scroll locking, popover focus improvements and the EC modal/notification
  display updates; the component JS and Twig are unchanged from the recorded
  baseline through v5.3.1.
- **Twig and HTML:** all three local Twig files remain byte-identical to the
  pinned EC sources. The modal example keeps default/information interactive
  dialogs, static variant/branch coverage and all 15 color modes; orphan
  `data-ecl-modal-toggle` references were removed from static dialogs and the
  success icon now exposes the documented accessible name. Popover retains
  button/link, no-close, rich-content, icon-only, indicator, extension,
  placement and 15-mode coverage. Notification retains all four variants,
  empty/extension branches, links, close hooks and 15-mode coverage.
- **MCP checks:** live connected calls returned 71 component IDs and 18 guide
  topics. `component` responses for modal, popover and notification matched
  disk; each `component_template` response returned its exact single Twig key
  and value, and all three families remained discoverable. A fresh local
  stdio client repeated the exact component and Twig comparisons. The
  connected content/list checks are recorded as S018 above.
- **Static/browser checks:** no duplicate IDs or missing ARIA/label references
  were found. The local v5.3.1 harness initialized 70 nodes with no console
  errors: 23 modals, 26 popovers, 20 notifications and one nested indicator;
  it covered all 15 color modes. Modal open/focus/body-scroll/Escape/close,
  popover open/close/focus-return/Escape/link-toggle and notification removal
  all passed. `node --check index.js` and `git diff --check` passed.
- **Checks and handoff:** `npm test -- --runInBand` remains blocked by the
  repository having no test files; `npm run lint` remains blocked by the lack
  of an ESLint configuration. No Laravel code was changed. All six S018 rows
  are Verified. The two S015 inpage-navigation rows remain Updated pending the
  pinned bundle's duplicate mobile-trigger listener decision; GUIDE-assets and
  GUIDE-icons WebTools rendering remain pending. Next take the remaining
  changed or interactive standalone families, beginning with
  `animated-numbers`/`blockquote`.

### S019 — 2026-09-25 — Batch 18: animated numbers and blockquotes

- **Scope:** `HTML/TWIG-animated-numbers` and `HTML/TWIG-blockquote`, the next
  recommended standalone families. The pinned target remains commit
  `0b3ca5a9190e1c32ff00fc092380e3a8f3571a05` (v5.3.1).
- **Sources:** rechecked the official [EC component library](https://ec.europa.eu/component-library/ec/),
  which still reports v5.3.1 and lists both components, the [v5.3.1 release](https://github.com/ec-europa/europa-component-library/releases/tag/v5.3.1),
  the tagged component README/demo/story/test snapshot/JS/SCSS/API/accessibility/usage sources,
  and the [v5.3.1 changelog](https://github.com/ec-europa/europa-component-library/blob/v5.3.1/CHANGELOG.md).
  Relevant history is the v5.1.0 individual-source addition, v5.2.0 blockquote
  author-markup update, and v5.3.0 source wrapping fixes; v5.3.1 itself changes
  layout-wrapper and site-header only.
- **Twig:** restored the exact tagged animated-numbers template, including its
  source-rendering macro, per-item sources and label fallback, branded/inverted
  Link propagation and `no_icon_wrapping`; restored the exact blockquote source,
  changing the author wrapper from `cite` to `span` as required by the target.
- **HTML:** added a per-item source list with an external-link icon/no-wrap
  example, aligned the dark-background source class with the target Link
  contract, and changed all blockquote author wrappers to `span`. Existing
  empty/value/source-only, responsive/decorative image, extension, language and
  15-mode EC coverage remains intact.
- **MCP checks:** a fresh local stdio client exercised all six tools. It returned
  71 component IDs and 18 guide topics; both component responses matched disk;
  each family returned its exact single Twig key/value; and the starter response
  retained `ECL.autoInit()`.
- **Static/browser checks:** tagged Twig diffs are empty, 24 animated-number
  roots initialized under the local v5.3.1 assets, all 15 EC color modes were
  present for both families, source links exposed the expected external icon
  structure, all 20 blockquote author nodes were `span`, responsive and
  decorative image cases loaded, and no console warnings/errors were recorded.
  `node --check index.js` and `git diff --check` pass. The temporary browser
  harness was removed after testing. `npm test -- --runInBand` still has no test
  files and `npm run lint` still has no ESLint configuration. No Laravel code
  changed.
- **Handoff:** all four S019 rows are Verified. The two S015 inpage-navigation
  rows remain Updated pending the pinned bundle's duplicate mobile-trigger
  listener decision; GUIDE-assets and GUIDE-icons WebTools rendering remain
  pending. Next take `add-to-calendar` with `banner` or another small related
  standalone/media group, while keeping the inpage and WebTools findings visible.

### S020 — 2026-09-25 — Batch 19: add-to-calendar and banner

- **Scope:** `HTML/TWIG-add-to-calendar` and `HTML/TWIG-banner`, the next
  recommended small standalone family. The pinned target remains commit
  `0b3ca5a9190e1c32ff00fc092380e3a8f3571a05` (v5.3.1).
- **Sources:** rechecked the official [EC component library](https://ec.europa.eu/component-library/ec/),
  which still reports v5.3.1 and lists both components, the [v5.3.1 release](https://github.com/ec-europa/europa-component-library/releases/tag/v5.3.1),
  the tagged component README/demo/story/test snapshot/JS/SCSS/API/accessibility/usage
  sources, the [v5.3.1 changelog](https://github.com/ec-europa/europa-component-library/blob/v5.3.1/CHANGELOG.md),
  and the official [WeSaveToCalendar demo](https://webtools.europa.eu/showcase/demo?comp=savetocalendar&demo=basic&lang=en&section=demo).
  The relevant release history includes the v5.2.0 add-to-calendar color-token
  update; v5.3.1 itself changes layout-wrapper and site-header, while both
  component Twig files remain unchanged from the pinned source.
- **Twig:** both local files are byte-identical to the pinned v5.3.1 sources.
  Add-to-calendar preserves metadata list/div branching, icon size forcing,
  full-width container handling, WebTools action markup and root extension
  attributes. Banner preserves Picture/Video/Button/Link composition,
  automatic initialization, aspect-ratio behavior, CTA description relations
  and extension attributes.
- **HTML:** add-to-calendar covers title-only, single and multiple metadata,
  icon/no-icon, action-only, full-width, extension and all 15 EC color modes;
  its two JSON action payloads now use the official seconds-inclusive date
  format, and the stale v5.0.1 label is corrected to v5.3.1. Banner covers
  image/video/no-media, responsive source, full-width/overlay/alignment/size,
  description-only and CTA-only relationships, empty input and all 15 EC color
  modes. The nonexistent `/captions/banner-en.vtt` request was removed; the
  muted decorative video is `aria-hidden` and its message remains repeated in
  page text. The add-to-calendar HTML row remains Updated because the external
  WebTools loader did not expose a generated action in the browser harness.
- **MCP checks:** a fresh local stdio client exercised all six tools. It returned
  71 component IDs and 18 guide topics; both component responses matched disk;
  each family returned its exact single Twig key/value; and the starter retained
  `ECL.autoInit()`. A separate connected MCP surface was not exposed in this
  session, so that existing-connection refresh remains an explicit limitation.
- **Static/browser checks:** tagged Twig diffs are empty; HTML parsing found no
  mismatched tags or duplicate IDs; both examples contain all 15 EC color modes;
  both action JSON payloads parse and match the official WebTools shape; 22
  Banner roots initialized under the local v5.3.1 assets. Chrome rendered the
  image/video/no-media branches and the video pause/play control toggled in both
  harness passes. Local requests were 200/304 except the expected harness
  favicon 404. `node --check index.js` and `git diff --check` pass. `npm test
  -- --runInBand` still has no test files and `npm run lint` still has no ESLint
  configuration. No Laravel code changed; the temporary harness was removed.
- **Handoff:** `HTML-banner`, `TWIG-banner` and `TWIG-add-to-calendar` are
  Verified; `HTML-add-to-calendar` is Updated pending WebTools action delivery.
  The two S015 inpage-navigation rows remain Updated pending the pinned bundle's
  duplicate mobile-trigger listener decision; GUIDE-assets and GUIDE-icons
  WebTools rendering remain pending. Next take `button`/`card` with their
  Link/Icon dependencies, optionally adding `content-block`/`content-item` if
  the shared contract remains a small coherent slice.

### S021 — 2026-09-25 — Batch 20: button, card and shared content composition

- **Scope:** `HTML/TWIG-button`, `HTML/TWIG-card`, `HTML/TWIG-content-block`,
  `HTML/TWIG-content-item` and `HTML/TWIG-icon`, selected as the next coherent
  batch because Card and Content item share the Content block/Picture/Link/Icon
  contracts. Link was already verified in S006. The pinned target remains
  commit `0b3ca5a9190e1c32ff00fc092380e3a8f3571a05` (v5.3.1).
- **Sources:** rechecked the official [EC component library](https://ec.europa.eu/component-library/ec/)
  homepage and component listings. The live Button/Card/Link pages exposed
  stale cached version labels in this session (v5.2.1/v4.11.2/v5.1.0 where
  applicable), so the pinned v5.3.1 source, tagged README/demo/story/test
  snapshots, JS/SCSS/API/accessibility/usage files and package dependencies
  remain the target evidence. The v5.3.1 [changelog](https://github.com/ec-europa/europa-component-library/blob/v5.3.1/CHANGELOG.md)
  changes layout-wrapper and site-header only; the relevant component Twig
  sources are unchanged at the pinned release.
- **Twig:** all five local files are byte-identical to the pinned v5.3.1
  sources. Button preserves Icon/Indicator and label/type contracts; Card
  preserves Picture/Content block/Link/Icon composition; Content block preserves
  semantic single/multiple wrappers and Link/Icon/Label/Description-list logic;
  Content item preserves Picture/Date block/Content block branches; Icon
  preserves its size/transform/color/accessibility/family/style contracts.
- **HTML:** Card responsive picture sources now use official EC example assets
  (`example-image2.jpg` through `example-image5.jpg`); the standalone
  information icon now has `title="Information"` and `role="img"` alongside
  `aria-hidden="false"`. Button, Content block, Content item and the remaining
  Icon branches were retained after coverage and accessibility review, including
  the 15 EC color modes where supported.
- **MCP checks:** a fresh local stdio client exercised all six tools. It returned
  71 component IDs and 18 guide topics; Button/Card/Content block/Content item/
  Icon component responses and exact single Twig key/value responses matched
  disk; and the starter retained `ECL.autoInit()`. A separate connected MCP
  surface was not exposed in this session.
- **Static/browser checks:** tagged Twig diffs are empty; no duplicate IDs were
  found; Card, Content block, Content item and Icon each expose all 15 color
  modes; all five official example images completed with nonzero natural width;
  60 Content block roots and three auto-initialized Content block instances
  rendered; the information icon reported `aria-hidden="false"`, role `img` and
  title `Information`; and browser logs were empty. `node --check index.js` and
  `git diff --check` pass. `npm test -- --runInBand` still has no test files and
  `npm run lint` still has no ESLint configuration. No Laravel code changed.
- **Handoff:** all ten S021 rows are Verified. `HTML-add-to-calendar` remains
  Updated pending external WebTools action delivery; the two S015
  inpage-navigation rows remain Updated pending the pinned bundle's duplicate
  mobile-trigger listener decision; and GUIDE-assets/GUIDE-icons WebTools
  rendering remains pending. Next take remaining navigation, forms,
  content/media and simple components, then focused guides/coverage gaps and
  final EC-wide checks; do not repeat the inventory.

### S022 — 2026-09-25 — Batch 21: category-filter and expandable navigation/disclosure

- **Scope:** `HTML/TWIG-category-filter` (including the recursive
  `category-filter-items` helper) and `HTML/TWIG-expandable`, selected as the
  first small interactive/navigation slice from the S021 handoff. The pinned
  target remains commit `0b3ca5a9190e1c32ff00fc092380e3a8f3571a05`
  (v5.3.1).
- **Sources:** rechecked the official [EC component library](https://ec.europa.eu/component-library/ec/),
  the official category-filter [usage guidance](https://ec.europa.eu/component-library/ec/components/category-filter/usage/),
  the official expandable [usage guidance](https://ec.europa.eu/component-library/ec/components/expandable/usage/),
  the [v5.3.1 release](https://github.com/ec-europa/europa-component-library/releases/tag/v5.3.1),
  the pinned component README/demo data/Storybook stories/tests/snapshots/JS/SCSS,
  EC API/accessibility/usage pages and package manifests, plus the [v5.3.1 changelog](https://github.com/ec-europa/europa-component-library/blob/v5.3.1/CHANGELOG.md).
  The changelog’s v5.3.1 fixes concern layout-wrapper spacing and the site-header
  search guard; neither selected component has a target-source change after the
  recorded v5.0 baseline.
- **Twig:** all three local files are byte-identical to the pinned EC source.
  Category filter retains its optional label/id/color mode and recursive
  four-level helper with current state, parent `aria-controls`/expanded hooks,
  Icon branches and escaped extensions. Expandable retains Button composition,
  generated content IDs, label-state hooks, hidden panel and auto-init contract.
- **HTML:** category-filter retains labelled four-level/current/extension/empty
  coverage and all 15 EC color modes; its extension `nav` now has an accessible
  name. Expandable retains default, rich, extension, empty and 15-mode coverage;
  its empty-label branch now has an explicit accessible name while preserving
  the empty-label/empty-content contract.
- **MCP checks:** a fresh local stdio client exercised all six tools. It returned
  71 component IDs and 18 guide topics; both component responses matched disk;
  category-filter returned exactly `category-filter.html.twig` and
  `category-filter-items.html.twig`, expandable returned exactly
  `expandable.html.twig`, and all returned template values matched disk. The
  starter retained `ECL.autoInit()` and guide `__DIR__` substitution passed. A
  separate connected MCP surface was not exposed in this session.
- **Static/browser checks:** tagged Twig diffs are empty; static checks found no
  duplicate IDs or broken `aria-controls` targets, and both examples expose all
  15 EC color modes. Chrome initialized all 18 category-filter and 20
  expandable roots with no console warnings/errors; nested category expansion,
  exclusive top-level category behavior, expandable open/close state, dynamic
  labels, named empty-label control, and hidden-panel state passed. The browser
  audit found no unnamed navs or buttons after the local example corrections.
  `node --check index.js` and `git diff --check` pass. `npm test -- --runInBand`
  still finds no test files, and `npm run lint` still has no ESLint
  configuration. No Laravel code changed.
- **Handoff:** all five S022 rows are Verified. `HTML-add-to-calendar` remains
  Updated pending external WebTools action delivery; the two S015
  inpage-navigation rows remain Updated pending the pinned bundle’s duplicate
  mobile-trigger listener decision; and GUIDE-assets/GUIDE-icons WebTools
  rendering remain pending. Next take the small simple-family slice of
  `date-block`, `label` and `separator`, then continue with remaining
  content/media families and focused guides/coverage gaps.

### S023 — 2026-09-25 — Batch 22: date block, label and separator

- **Scope:** `HTML/TWIG-date-block`, `HTML/TWIG-label` and
  `HTML/TWIG-separator`, the next recommended small simple-family slice. The
  pinned target remains commit `0b3ca5a9190e1c32ff00fc092380e3a8f3571a05`
  (v5.3.1).
- **Sources:** rechecked the official [EC component library](https://ec.europa.eu/component-library/ec/),
  which still reports v5.3.1 and lists Date blocks, Divider and Labels, the
  live [date-block usage guidance](https://ec.europa.eu/component-library/ec/components/date-block/usage/),
  [label usage guidance](https://ec.europa.eu/component-library/ec/components/label/usage/),
  the pinned EC date-block/label/separator README, demo data, stories, tests,
  snapshots, SCSS/print sources, package manifests and EC usage/accessibility
  docs, plus the [v5.3.1 changelog](https://github.com/ec-europa/europa-component-library/blob/v5.3.1/CHANGELOG.md).
  The target release changes layout-wrapper spacing and the site-header search
  guard only; none of these three component Twig sources changed in the target
  release. The live accessibility links for date block, label and divider
  currently resolve to 404-style paths, so the pinned versioned docs were used
  for those checks.
- **Twig:** all three local templates are byte-identical to their pinned
  v5.3.1 sources. Date block retains grid/screen-reader utility dependencies,
  optional machine-date/month branches, status classes and escaped extension
  attributes; label retains its typography dependency and four variant classes;
  separator retains semantic `<hr>` output and escaped valued/boolean
  extension attributes.
- **HTML:** date block retains default, ongoing/cancelled/past,
  no-abbreviation, no-machine-date, extension and all 15 EC color-mode cases.
  Its status variants now include screen-reader-only state text as required by
  the pinned accessibility guidance, and the no-machine-date month branch uses
  an accessible span fallback. Label retains all four variants, extension and
  empty branches, and all 15 modes. Separator retains semantic `<hr>` rules,
  extra class/attribute branches, unordered/ordered/description-list contexts
  and all 15 modes.
- **MCP checks:** a fresh local stdio client exercised all six tools. It
  returned 71 component IDs and 18 guide topics; all three component responses
  matched disk; each family returned its exact single Twig key/value; the
  starter retained `ECL.autoInit()`; and guide `__DIR__` substitution passed.
  The separate connected MCP surface was not exposed in this session.
- **Static/browser checks:** tagged Twig diffs are empty; static checks found
  all 15 modes in each example, 22 date-block roots, all four label variants,
  21 separator rules and the expected semantic contexts. The local v5.3.1
  Chrome harness rendered all three families; its accessibility tree exposed
  the three state labels and all date/label/list content, with local CSS/JS/
  component requests returning 200/304 except the expected harness favicon
  404. `node --check index.js` and `git diff --check` pass. `npm test
  -- --runInBand` remains blocked by the absence of test files, and
  `npm run lint` remains blocked by the absence of an ESLint configuration. No
  Laravel code changed; the temporary harness is removed after this session.
- **Handoff:** all six S023 rows are Verified. `HTML-add-to-calendar` remains
  Updated pending external WebTools action delivery; the two S015
  inpage-navigation rows remain Updated pending the pinned bundle's duplicate
  mobile-trigger listener decision; and GUIDE-assets/GUIDE-icons WebTools
  rendering remain pending. Next take the remaining simple/content-media
  families, beginning with `featured-item`/`highlight-box` or the list/timeline
  group, then finish focused guides/coverage gaps and the final EC-wide checks.
