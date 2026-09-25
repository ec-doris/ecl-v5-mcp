# ECL EC update status

Standing record for the incremental update of the European Commission ECL MCP.
Resume with [updating-prompt.md](updating-prompt.md). Update this file in place;
preserve row IDs and append session history. Work sequentially with one agent.

## Target and observed baseline

| Field | Recorded value |
| --- | --- |
| Inventory date | 2026-09-25 |
| Scope | European Commission (EC), ECL v5 |
| Target for this cycle | **v5.3.1**, released 2026-09-21 |
| Pinned release commit | `0b3ca5a9190e1c32ff00fc092380e3a8f3571a05` |
| Official EC documentation | <https://ec.europa.eu/component-library/ec/> (v5.3.1 observed) |
| Release reference | <https://github.com/ec-europa/europa-component-library/tree/v5.3.1> |
| Release changelog | <https://github.com/ec-europa/europa-component-library/blob/v5.3.1/CHANGELOG.md> |
| MCP repository at inventory | `main`; existing deletion of `component-update.md` preserved |
| Linked upstream | `europa-component-library` → `../europa-component-library`; branch `v5-dev`, tracking `origin/v5-dev` |
| Upstream before pull | `eba75687ecce5cddbb8d7c6ce8854a6e913986b3` |
| Upstream after `git pull --ff-only` | `cd0f615bd16816d8d99517192b1f817ae4a85618`; pull succeeded, checkout clean |
| Existing content evidence | Guides/start and historical tracker identify v5.0.1, commit `eceefe9468e44f7ce9c57801c91c4c0c057548b4`; both JS bundles contain `ECL.version="5.0.1"` |
| Version discrepancy | User recalled starting at 5.0.2; checked-in evidence above identifies 5.0.1. Use file evidence when comparing; do not relabel it as 5.0.2. |
| Current delivery model | Six Node.js MCP tools over stdio; content read on each call; no Laravel application |

**The development checkout is not the release baseline.** Its HEAD differs from
v5.3.1 in markup and behavior, as well as metadata. Inspect reference files with
`git -C europa-component-library show v5.3.1:<path>`. Build from the pinned release,
not the moving development checkout. Pulling upstream does not update this MCP's
copied content or compiled assets.

S002 refreshed shared assets to v5.3.1 and reconciled setup guidance. S003
delivered the EC site-wide template family, corrected the MCP template-family
contract, removed accidental EU footer exposure from the EC delivery, and
aligned the starter shell. S004 delivered the first high-drift component slice:
highlighted-search, story-card/slider and carousel. Remaining component-example
HTML audits and most guide content still await their batches. See the latest
session for the WebTools and mobile-control verification limits.

## Status and evidence rules

| Status | Meaning |
| --- | --- |
| Review | Inventoried; target conformance or a coverage decision remains to be checked. |
| Needs update | Concrete version drift, source difference, or delivery problem identified; work pending. |
| Missing | Upstream item/reference is absent locally. Add when required, or record a reasoned exclusion/coverage decision. |
| In progress | Selected for the current sequential batch. Leave a concrete resume note if unfinished. |
| Updated | Changes made for the target; some required validation or live MCP verification is still pending. |
| Verified | Correct for the recorded target, including justified no-change decisions; applicable source, rendered/runtime and live MCP checks completed. |
| Blocked | A specific unresolved dependency prevents completion; record the next action. |
| Excluded | Deliberately outside this cycle, with rationale; never counted as EC content upgraded. |

All pending rows below target **v5.3.1**. The last column is the per-row completion
record: replace `—` with `version / date / evidence or session ID` only when the
required verification is complete. Findings are the 2026-09-25 baseline. Update
them as work proceeds; preserve earlier evidence in session history. Exact Twig
identity or a successful MCP read alone is not complete conformance verification.

## Summary

| Inventory | Count / result |
| --- | --- |
| Registered MCP tools | 6 |
| Existing guides | 18 |
| Existing HTML component IDs | 71 |
| Existing Twig files | 92 (77 identical to target, 13 different, 2 absent/retired upstream) |
| Existing starter pages | 1 |
| Existing asset/font files | 15 assets + 3 font files |
| Newly identified public components | 2 delivered in S004: highlighted-search, story-card |
| Missing Twig references | 1: layout-wrapper |
| Connected content checks | S013: range/rating-field component responses and range/rating-field/file-upload-status template key/value matches disk; S012: seven remaining form component responses and nine Twig template key/value matches disk; S011: form-group, search-form and page-summary component responses and all three template key/value matches disk; S010: fact-figures component response and template key match disk; S008: accordion component response and template key match disk; S007: table/news-ticker component responses and both template keys match disk; S006: picture/link/video/media-container/text-media component responses and all five template keys match disk; S005: file/gallery component responses and all returned template keys match disk; S004: new component responses and all returned template keys match disk; S003: affected component/template calls and starter response match disk; tooltip has no advertised template; S002: 25/25 sampled content calls passed |
| Connected list checks | S013: 71 component IDs, 18 guide topics and range/rating-field discoverability plus the file-upload family status-template call passed; S012: 71 component IDs, 18 guide topics and seven form-family discoverability/template calls passed; S011: 71 component IDs, 18 guide topics and form-group/search-form/page-summary discoverability/family calls passed; S010: 71 component IDs, 18 guide topics and fact-figures discoverability/family calls passed; S008: 71 component IDs, 18 guide topics and accordion discoverability/family calls passed; S007: 71 component IDs, 18 guide topics and current family calls passed; S006: 71 component IDs, 18 guide topics and current family calls passed; S005: 71 component IDs and file/gallery family calls passed; S004: 71 component IDs and affected family calls passed; S003: 3/3 affected list/family checks passed |
| Content verified for v5.3.1 | **56 files** — 18 asset/font files, GUIDE-start, the four S007 table/news-ticker files, the two S008 accordion files, the two S009 description-list files, the two S010 fact-figures files, the six S011 forms/page-summary files, the 16 S012 remaining forms files and the five S013 range/rating/status Twig/HTML files; GUIDE-assets remains Updated |
| Tracked work rows | 235 (excluding setup milestones) |
| Excluded | 7 |
| Missing | 4 |
| Needs update | 23 |
| Review | 103 |
| Updated | 10 |
| Verified work rows | 88 (33 prior verified rows + 8 S005 source/delivery rows + 10 S006 media/link rows + 4 S007 table/news-ticker rows + 2 S008 accordion rows + 2 S009 description-list rows + 2 S010 fact-figures rows + 6 S011 forms/page-summary rows + 16 S012 remaining forms rows + 5 S013 range/rating/status rows) |

## Completed setup milestones

| ID | Milestone | Status | Evidence |
| --- | --- | --- | --- |
| SETUP-upstream | Refresh linked upstream and pin the published target | Verified | 2026-09-25 / fast-forward pull; v5.3.1 tag resolves to pinned commit; official EC homepage and getting-started show v5.3.1. |
| SETUP-prompt | Write reusable sequential session prompt | Verified | 2026-09-25 / updating-prompt.md records baseline, batch selection, validation and handoff requirements. |
| SETUP-inventory | Enumerate MCP contract, local content and upstream gaps | Verified | 2026-09-25 / index.js registrations, local file enumeration, tagged source comparison and connected MCP reads. This does not certify content currency. |

## Findings that affect the update order

1. **Shared assets are updated (S002).** Both JS bundles now identify v5.3.1.
   All 18 existing asset/font files have provenance and integration checks.
   WebTools icons remain an external verification limitation; GUIDE-assets is
   Updated until that check can finish.
2. **Preserve the tested loading contract (S002).** Use reset, utilities, main
   screen CSS, then color modes; load print CSS with print media. The official
   getting-started page puts all optional styles first, but the tagged cascade
   requires color modes after main CSS for modes on `html`. Module initialization
   must wait for its import; a prior autoInit call’s `update()` does not discover
   newly inserted nodes. These differences are documented and browser-tested.
3. **Review changed families with their dependencies.** Notable tagged release
   changes include file redesign, carousel/slider behavior, story card and
   highlighted search, table filtering, the news-ticker redesign, gallery media, navigation, colour tokens,
   and accessibility. Consult the pinned changelog for each batch. v5.3.1 itself
   fixes layout-wrapper spacing and the header's missing-search-form handling.
4. **Template discovery is now explicit and EC-scoped (S003).** `components_list`
   no longer advertises a nonexistent tooltip template. Exact family mapping keeps
   `file` separate from `file-upload` and returns only the EC site-footer pair;
   the legacy EU Twig file remains inventoried but excluded from active EC lookup.
5. **Keep meaningful coverage.** Existing rendered examples contain variants and
   local adaptations from the prior cycle. Compare before replacing them; do not
   reduce an example to one demo or declare it current because a Twig file matches.
6. **Keep verification honest.** No project test files or ESLint configuration were
   found in tracked files at inventory. `npm test` declares Jest but that alone is
   not a test suite. This documentation-only setup session did not run application
   tests, build upstream assets, or certify browser behavior.

## Reference key

References below are paths in the **pinned upstream release**, not necessarily the
same content in the linked working tree. Read them via `git show v5.3.1:<path>`.
`D/components/.../` includes the page and its `docs/` children. For a public page
directory, the live EC URL is `https://ec.europa.eu/component-library/ec/` plus the
directory after `D/`; omit source filenames and `docs/` children. Use the live URL
and tagged source together; log discrepancies or later releases.

| Prefix | Upstream path |
| --- | --- |
| C/ | src/components/ |
| D/ | src/website/src/pages/ec/ |
| U/ | src/utilities/ |
| P/ | src/presets/ |
| R/ | src/resources/ |
| L/ | src/layout/ |
| X/ | src/compositions/ |
| E/ | src/page-example/ |

## MCP tools and protocol surface

All six tools are registered in `index.js` and exposed over stdio. There are no registered MCP resources, resource templates, prompts or HTTP routes. Assets are copied from disk via the assets guide; there is no asset-download tool. Successful delivery below is a baseline check, not a v5.3.1 conformance result.

| ID | Local item / lookup | Target reference | Finding / next action | Status | Verified version / date / evidence |
| --- | --- | --- | --- | --- | --- |
| TOOL-guide | `guide({topic})` | `index.js`; `guides/*.md` | 18/18 live responses match disk after `__DIR__` substitution. Recheck after guide updates. | Review | — |
| TOOL-guide-list | `guide_list({})` | `index.js` | 18 topics match local filenames; snippets are the first 120 characters. Recheck new topics and version labels. | Review | — |
| TOOL-components-list | `components_list({})` | `index.js` | 71 HTML IDs match local filenames. Template calls are advertised for exact active EC families; carousel and story-card include the shared slider pager, file/gallery return their scoped families, and tooltip is not advertised because no standalone template exists. | Verified | v5.3.1 / 2026-09-25 / S007; live list and current-family checks |
| TOOL-component | `component({id})` | `index.js`; `components/*.html` | 71/71 live responses match disk, including the S007 table and news-ticker examples, the S006 media families and the previously delivered high-drift families. | Verified | v5.3.1 / 2026-09-25 / S007; fresh stdio component calls and disk comparison |
| TOOL-component-template | `component_template({id})` | `index.js`; `components/*.html.twig` | Exact EC family mapping returns the table and news-ticker templates plus the previously delivered picture, link, video, media-container, text-media, file, gallery, highlighted-search, story-card/story-card-card/slider-pager and carousel/slider-pager families; tooltip correctly reports no templates. | Verified | v5.3.1 / 2026-09-25 / S007; live table/news-ticker template calls and disk comparison |
| TOOL-starter-template | `starter_template({})` | `index.js`; `starter-template.html` | Connected response matches disk; page setup, Search and Menu runtime checks are recorded under PAGE-starter. | Verified | v5.3.1 / 2026-09-25 / S003; live response and browser smoke |

## Existing guides — 18 topics

MCP lookup: `guide({"topic":"<filename without .md>"})`. GUIDE-start is verified; GUIDE-assets awaits external icon validation. The other
guides received setup-only edits in S002 and retain their v5.0.1 content audit status.

| ID | Local item / lookup | Target reference | Finding / next action | Status | Verified version / date / evidence |
| --- | --- | --- | --- | --- | --- |
| GUIDE-assets | [guides/assets.md](guides/assets.md) | `D/getting-started/index.mdx; P/ec/ecl-builder.config.js; R/` | v5.3.1 provenance/copy paths, tested CSS order exception, classic/module loading, fonts, optional assets and Duet guidance updated; live response matches disk. WebTools icon loader is blocked by ORB here: retry a representative icon page when reachable before marking Verified. | Updated | — |
| GUIDE-background | [guides/background.md](guides/background.md) | `D/utilities/background/; U/background/` | Guide is labelled v5.0.1; compare documented classes, values, examples and responsive behavior with the target. S002 updated loading snippets only; content audit remains pending. | Needs update | — |
| GUIDE-border | [guides/border.md](guides/border.md) | `D/utilities/border/; U/border/` | Guide is labelled v5.0.1; compare documented classes, values, examples and responsive behavior with the target. S002 updated loading snippets only; content audit remains pending. | Needs update | — |
| GUIDE-clearfix | [guides/clearfix.md](guides/clearfix.md) | `D/utilities/clearfix/; U/clearfix/` | Guide is labelled v5.0.1; compare documented classes, values, examples and responsive behavior with the target. S002 updated loading snippets only; content audit remains pending. | Needs update | — |
| GUIDE-colours | [guides/colours.md](guides/colours.md) | `D/guidelines/colours/index.mdx; src/themes/ec/; src/themes/color-modes/` | Re-audit tokens and modes; release notes include removal of cm-surface-color-mode-lowest. S002 updated loading snippets only; content audit remains pending. | Needs update | — |
| GUIDE-dimension | [guides/dimension.md](guides/dimension.md) | `D/utilities/dimension/; U/dimension/` | Guide is labelled v5.0.1; compare documented classes, values, examples and responsive behavior with the target. S002 updated loading snippets only; content audit remains pending. | Needs update | — |
| GUIDE-display | [guides/display.md](guides/display.md) | `D/utilities/display/; U/display/` | Guide is labelled v5.0.1; compare documented classes, values, examples and responsive behavior with the target. S002 updated loading snippets only; content audit remains pending. | Needs update | — |
| GUIDE-flex | [guides/flex.md](guides/flex.md) | `D/utilities/layout/stacks/; U/flex/` | Guide is labelled v5.0.1; compare documented classes, values, examples and responsive behavior with the target. S002 updated loading snippets only; content audit remains pending. | Needs update | — |
| GUIDE-float | [guides/float.md](guides/float.md) | `D/utilities/float/; U/float/` | Guide is labelled v5.0.1; compare documented classes, values, examples and responsive behavior with the target. S002 updated loading snippets only; content audit remains pending. | Needs update | — |
| GUIDE-grid | [guides/grid.md](guides/grid.md) | `D/utilities/layout/grid/; L/grid/` | Guide is labelled v5.0.1; compare documented classes, values, examples and responsive behavior with the target. S002 updated loading snippets only; content audit remains pending. | Needs update | — |
| GUIDE-icons | [guides/icons.md](guides/icons.md) | `D/guidelines/iconography/index.mdx; D/components/icon/; C/icon/; R/icons/` | Recheck WebTools integration, icon families, accessibility and the upstream icon lists. S002 updated loading snippets only; content audit remains pending. WebTools loader blocked by ORB during smoke testing; retry when accessible. | Needs update | — |
| GUIDE-media | [guides/media.md](guides/media.md) | `D/utilities/media/; U/media/` | Guide is labelled v5.0.1; compare documented classes, values, examples and responsive behavior with the target. S002 updated loading snippets only; content audit remains pending. | Needs update | — |
| GUIDE-shadow | [guides/shadow.md](guides/shadow.md) | `D/utilities/shadow/; U/shadow/` | Guide is labelled v5.0.1; compare documented classes, values, examples and responsive behavior with the target. S002 updated loading snippets only; content audit remains pending. | Needs update | — |
| GUIDE-spacing | [guides/spacing.md](guides/spacing.md) | `D/utilities/spacing/; U/spacing/; D/guidelines/spacing/index.mdx` | Cover guideline tokens and screen/print utility behavior at the target release. S002 updated loading snippets only; content audit remains pending. | Needs update | — |
| GUIDE-start | [guides/start.md](guides/start.md) | `D/getting-started/index.mdx; index.js` | Explains incremental content status and existing tool limitations; fixes dynamic autoInit guidance, module timing and loading contract. Live delivery and runtime examples checked. | Verified | v5.3.1 / 2026-09-25 / S002; checksum manifest, browser and live setup delivery |
| GUIDE-typography | [guides/typography.md](guides/typography.md) | `D/utilities/typography/; U/typography/; D/guidelines/typography/index.mdx` | Cover both design guidance and utility classes; verify Inter and compiled tokens. S002 updated loading snippets only; content audit remains pending. | Needs update | — |
| GUIDE-utility-classes | [guides/utility-classes.md](guides/utility-classes.md) | `D/utilities/; U/; P/ec/src/ec-utilities.scss; P/ec/src/ec-print.scss` | Recount/revalidate utility families; retains brief disable-scroll, screen-reader and print guidance. S002 updated loading snippets only; content audit remains pending. | Needs update | — |
| GUIDE-z-index | [guides/z-index.md](guides/z-index.md) | `D/utilities/z-index/; U/z-index/` | Guide is labelled v5.0.1; compare documented classes, values, examples and responsive behavior with the target. S002 updated loading snippets only; content audit remains pending. | Needs update | — |

## Documentation coverage gaps

These rows reconcile every guideline, utility and resource topic in the official EC navigation with current guide coverage. A missing dedicated file does not necessarily mean missing coverage; retain useful material in an existing guide when appropriate.

| ID | Local item / lookup | Target reference | Finding / next action | Status | Verified version / date / evidence |
| --- | --- | --- | --- | --- | --- |
| DOC-images | `images` coverage | `D/guidelines/images/index.md` | No dedicated official image-usage guide; distinguish design guidance from media utilities. | Missing | — |
| DOC-logos | `logos` coverage | `D/guidelines/logo/index.mdx` | Only asset references currently exist; document official EC logo use and variants. | Missing | — |
| DOC-html-tag | `html-tag` coverage | `D/utilities/html-tag/; P/ec/src/ec-default.scss; P/ec/src/ec-default-print.scss` | No HTML-tag styling guide; coordinate with optional default styles. | Missing | — |
| DOC-disablescroll | `disablescroll` coverage | `D/utilities/disablescroll/; U/disablescroll/` | Covered briefly in GUIDE-utility-classes; review completeness and decide whether a focused guide helps. | Review | — |
| DOC-screen-reader | `screen-reader` coverage | `D/utilities/screen-reader/; U/screen-reader/` | Covered briefly in GUIDE-utility-classes; review accessibility examples and cross-links. | Review | — |
| DOC-print | `print` coverage | `D/utilities/print/; U/print/` | Covered across existing guides; reconcile print loading and visibility before deciding on a focused guide. | Review | — |
| DOC-glossary | `glossary` coverage | `D/resources/glossary/index.md` | Review whether useful terminology should be linked or summarized in GUIDE-start; no automatic new endpoint. | Review | — |
| DOC-webtools | `webtools` coverage | `D/resources/webtools/index.md` | Reconcile existing icons/assets guidance with the official resource page. | Review | — |
| DOC-eui | `eui` coverage | `D/resources/eui/index.md` | Keep any useful distinction/link in onboarding; building an eUI library is outside this EC ECL update. | Review | — |

## Component HTML examples — 71 existing, 0 missing

One row per discoverable HTML ID. Source directories contain Twig, demo data, stories, styles, JavaScript and tests as available; inspect actual tagged paths. Website references include usage, code, API and accessibility where supplied. Existing HTML has been inventoried and delivered, not yet audited for v5.3.1.

| ID | Local item / lookup | Target reference | Finding / next action | Status | Verified version / date / evidence |
| --- | --- | --- | --- | --- | --- |
| HTML-accordion | [components/accordion.html](components/accordion.html) | `C/accordion/`; `D/components/accordion/` | Updated to v5.3.1 native details/summary coverage: four-item default with third item open, named exclusive group, configurable sidebar media query, single indicator, structured content, extension hooks and EC color modes. | Verified | v5.3.1 / 2026-09-25 / S008; tagged README/demo/data/sidebar/story/tests/snapshots/docs/changelog, semantic/static checks, live MCP/disk match and Chrome initialization/toggle/sidebar smoke; WebTools icon rendering remains an external limitation |
| HTML-add-to-calendar | [components/add-to-calendar.html](components/add-to-calendar.html) | `C/add-to-calendar/`; `D/components/add-to-calendar/` | Live HTML matches disk; audit official EC variants, dependencies, accessibility and behavior. | Review | — |
| HTML-animated-numbers | [components/animated-numbers.html](components/animated-numbers.html) | `C/animated-numbers/`; `D/components/animated-numbers/` | Target Twig differs in this family; review HTML against the new contract, demos and EC snapshots. | Review | — |
| HTML-banner | [components/banner.html](components/banner.html) | `C/banner/`; `D/components/banner/` | Live HTML matches disk; audit official EC variants, dependencies, accessibility and behavior. | Review | — |
| HTML-blockquote | [components/blockquote.html](components/blockquote.html) | `C/blockquote/`; `D/components/blockquote/` | Target Twig differs in this family; review HTML against the new contract, demos and EC snapshots. | Review | — |
| HTML-breadcrumb | [components/breadcrumb.html](components/breadcrumb.html) | `C/breadcrumb/`; `D/components/navigation/breadcrumb/` | Live HTML matches disk; audit official EC variants, dependencies, accessibility and behavior. | Review | — |
| HTML-button | [components/button.html](components/button.html) | `C/button/`; `D/components/button/` | Live HTML matches disk; audit official EC variants, dependencies, accessibility and behavior. | Review | — |
| HTML-card | [components/card.html](components/card.html) | `C/card/`; `D/components/card/` | Live HTML matches disk; audit official EC variants, dependencies, accessibility and behavior. | Review | — |
| HTML-carousel | [components/carousel.html](components/carousel.html) | `C/carousel/`; `D/components/carousel/` | Updated to the v5.3.1 pager/teaser/viewport contract, including shared slider-pager hooks, inert inactive slides, counter labels, full-width/color-mode coverage and banner/video examples. Desktop and narrow-width next-slide behavior passed. | Verified | v5.3.1 / 2026-09-25 / S005; S004 tagged data/snapshot markers and parser/ARIA checks, live MCP, desktop plus narrow-width browser smoke |
| HTML-category-filter | [components/category-filter.html](components/category-filter.html) | `C/category-filter/`; `D/components/category-filter/` | Live HTML matches disk; audit official EC variants, dependencies, accessibility and behavior. | Review | — |
| HTML-checkbox | [components/checkbox.html](components/checkbox.html) | `C/checkbox/`; `D/components/forms/checkbox/` | Existing examples already cover checkbox group/item, required/optional, helper/invalid, disabled and standalone states, plus all EC color modes; no HTML mutation was required. | Verified | v5.3.1 / 2026-09-25 / S012; tagged README/demo/story/tests/snapshots/changelog, static ID/label/state checks, live MCP/disk match and browser accessibility/DOM smoke |
| HTML-content-block | [components/content-block.html](components/content-block.html) | `C/content-block/`; `D/components/content-item/` | Live HTML matches disk; audit official EC variants, dependencies, accessibility and behavior. | Review | — |
| HTML-content-item | [components/content-item.html](components/content-item.html) | `C/content-item/`; `D/components/content-item/` | Live HTML matches disk; audit official EC variants, dependencies, accessibility and behavior. | Review | — |
| HTML-date-block | [components/date-block.html](components/date-block.html) | `C/date-block/`; `D/components/date-block/` | Live HTML matches disk; audit official EC variants, dependencies, accessibility and behavior. | Review | — |
| HTML-datepicker | [components/datepicker.html](components/datepicker.html) | `C/datepicker/`; `D/components/forms/datepicker/` | Existing examples already cover Duet date-picker markup, default/required/disabled/invalid/custom/empty states, min/max and first-day settings, Datepicker hooks and all EC color modes; no HTML mutation was required. | Verified | v5.3.1 / 2026-09-25 / S012; tagged README/demo/story/tests/snapshots/changelog, static custom-element/hook checks, live MCP/disk match and browser accessibility/DOM smoke |
| HTML-description-list | [components/description-list.html](components/description-list.html) | `C/description-list/`; `D/components/list/` | Updated to v5.3.1 vertical and horizontal coverage: nine-item link/tag/taxonomy demo data, collapsible definitions, real runtime hooks, omission branches, extension attributes and EC color modes. | Verified | v5.3.1 / 2026-09-25 / S009; tagged README/demo/story/tests/snapshots/JS/SCSS/EC docs/changelog, semantic/static checks, live MCP/disk match and Chrome initialization/Show more focus smoke |
| HTML-expandable | [components/expandable.html](components/expandable.html) | `C/expandable/`; `D/components/expandable/` | Live HTML matches disk; audit official EC variants, dependencies, accessibility and behavior. | Review | — |
| HTML-fact-figures | [components/fact-figures.html](components/fact-figures.html) | `C/fact-figures/`; `D/components/fact-figures/` | Aligned the EC fact-and-figures demo with v5.3.1 individual/global sources, wrapping external links, value/title variants, 1–4 columns, centered and icon-free modes, view-all behavior, extension hooks, empty output and EC color modes. | Verified | v5.3.1 / 2026-09-25 / S010; tagged README/demo/story/tests/snapshots/EC usage/accessibility/changelog, static checks, live MCP/disk match and browser rendering smoke |
| HTML-featured-item | [components/featured-item.html](components/featured-item.html) | `C/featured-item/`; `D/components/media/featured-item/` | Live HTML matches disk; audit official EC variants, dependencies, accessibility and behavior. | Review | — |
| HTML-file-upload | [components/file-upload.html](components/file-upload.html) | `C/file-upload/`; `D/components/forms/file-upload/` | Existing examples already cover single/multiple upload, disabled/invalid/optional/empty states, extension attributes, selected-file list markup, file-list hooks and all EC color modes; no HTML mutation was required. | Verified | v5.3.1 / 2026-09-25 / S012; tagged README/demo/story/tests/snapshots/changelog, static ID/ARIA/hook checks, live MCP/disk match and browser accessibility/DOM smoke |
| HTML-file | [components/file.html](components/file.html) | `C/file/`; `D/components/file/` | Aligned the file examples with the v5.3.1 article/container, primary metadata, thumbnail, color-mode and inline translation contract; translation toggles pass runtime checks. | Verified | v5.3.1 / 2026-09-25 / S005; tagged file data/story/snapshot/docs, parser/ARIA checks, live MCP/disk match and browser expand/collapse smoke |
| HTML-form-group | [components/form-group.html](components/form-group.html) | `C/form-group/`; `D/components/forms/` | Aligned the examples with the v5.3.1 label-wrapper contract, required/optional visibility, helper/invalid relationships, supported input-family markup, extension hooks, disabled/hidden-label cases and EC color modes. | Verified | v5.3.1 / 2026-09-25 / S011; tagged README/demo/story/tests/snapshots/changelog, static ID/ARIA/hook checks, live MCP/disk match and browser accessibility/DOM smoke |
| HTML-gallery | [components/gallery.html](components/gallery.html) | `C/gallery/`; `D/components/media/gallery/` | Aligned mixed image/video, grid, no-overlay, empty and EC color-mode examples with v5.3.1 publication-date, video-duration, overlay and icon hooks; overlay navigation passes runtime checks. | Verified | v5.3.1 / 2026-09-25 / S005; tagged gallery data/story/snapshot/docs, parser/ARIA checks, live MCP/disk match and browser overlay/navigation smoke |
| HTML-highlight-box | [components/highlight-box.html](components/highlight-box.html) | `C/highlight-box/`; `D/components/highlight-box/` | Live HTML matches disk; audit official EC variants, dependencies, accessibility and behavior. | Review | — |
| HTML-icon | [components/icon.html](components/icon.html) | `C/icon/`; `D/components/icon/` | Live HTML matches disk; audit official EC variants, dependencies, accessibility and behavior. | Review | — |
| HTML-indicator | [components/indicator.html](components/indicator.html) | `C/indicator/`; `D/components/loading-indicator/` | Live HTML matches disk; audit official EC variants, dependencies, accessibility and behavior. | Review | — |
| HTML-inpage-navigation | [components/inpage-navigation.html](components/inpage-navigation.html) | `C/inpage-navigation/`; `D/components/navigation/inpage-navigation/` | Live HTML matches disk; audit official EC variants, dependencies, accessibility and behavior. | Review | — |
| HTML-label | [components/label.html](components/label.html) | `C/label/`; `D/components/label/` | Live HTML matches disk; audit official EC variants, dependencies, accessibility and behavior. | Review | — |
| HTML-link | [components/link.html](components/link.html) | `C/link/`; `D/components/navigation/link/` | Added the tagged link coverage for tertiary variants, external label, indicator, icon placement and no-icon-wrapping; accessible names and all link targets checked in the browser. | Verified | v5.3.1 / 2026-09-25 / S006; tagged link README/story/snapshots/docs, parser/ARIA checks, live MCP/disk match and browser link smoke |
| HTML-list-illustration | [components/list-illustration.html](components/list-illustration.html) | `C/list-illustration/`; `D/components/list-illustration/` | Live HTML matches disk; audit official EC variants, dependencies, accessibility and behavior. | Review | — |
| HTML-media-container | [components/media-container.html](components/media-container.html) | `C/media-container/`; `D/components/media/media-container/` | Aligned examples with the tagged image/video/embed/ratio/expandable contract; captions/credits, iframe titles, video labels and autoplay controls are covered. | Verified | v5.3.1 / 2026-09-25 / S006; tagged media-container demos/story/README/snapshots/docs, parser/ARIA checks, live MCP/disk match and desktop+narrow browser controls |
| HTML-mega-menu | [components/mega-menu.html](components/mega-menu.html) | `C/mega-menu/`; `D/components/navigation/mega-menu/` | Target Twig differs in this family; review HTML against the new contract, demos and EC snapshots. | Review | — |
| HTML-menu | [components/menu.html](components/menu.html) | `C/menu/`; `D/components/navigation/menu/` | Live HTML matches disk; audit official EC variants, dependencies, accessibility and behavior. | Review | — |
| HTML-modal | [components/modal.html](components/modal.html) | `C/modal/`; `D/components/modal/` | Live HTML matches disk; audit official EC variants, dependencies, accessibility and behavior. | Review | — |
| HTML-navigation-list | [components/navigation-list.html](components/navigation-list.html) | `C/navigation-list/`; `D/components/navigation/navigation-list/` | Live HTML matches disk; audit official EC variants, dependencies, accessibility and behavior. | Review | — |
| HTML-news-ticker | [components/news-ticker.html](components/news-ticker.html) | `C/news-ticker/`; `D/components/news-ticker/` | Aligned default and single-item examples with the v5.3.1 redesign: slide icon/content wrappers, branded links, Phosphor icons, default newspaper fallback, LTR counter and safe static color-mode hooks. | Verified | v5.3.1 / 2026-09-25 / S007; tagged README/demo/story/snapshot/docs, parser checks, live MCP/disk match and browser next-control smoke |
| HTML-notification | [components/notification.html](components/notification.html) | `C/notification/`; `D/components/notification/` | Live HTML matches disk; audit official EC variants, dependencies, accessibility and behavior. | Review | — |
| HTML-ordered-list | [components/ordered-list.html](components/ordered-list.html) | `C/ordered-list/`; `D/components/list/` | Live HTML matches disk; audit official EC variants, dependencies, accessibility and behavior. | Review | — |
| HTML-page-header | [components/page-header.html](components/page-header.html) | `C/page-header/`; `D/components/site-wide/page-header/` | Target Twig differs in this family; review HTML against the new contract, demos and EC snapshots. | Review | — |
| HTML-page-information | [components/page-information.html](components/page-information.html) | `C/page-information/`; `D/components/page-information/` | Live HTML matches disk; audit official EC variants, dependencies, accessibility and behavior. | Review | — |
| HTML-page-summary | [components/page-summary.html](components/page-summary.html) | `C/page-summary/`; `D/components/page-summary/` | Existing example already covered the v5.3.1 title/description, icon, list, deterministic IDs, extension attributes and all EC color modes; no HTML mutation was required. | Verified | v5.3.1 / 2026-09-25 / S011; tagged README/demo/story/tests/snapshots/changelog, static ID/ARIA/color-mode checks, live MCP/disk match and browser DOM smoke |
| HTML-pagination | [components/pagination.html](components/pagination.html) | `C/pagination/`; `D/components/navigation/pagination/` | Live HTML matches disk; audit official EC variants, dependencies, accessibility and behavior. | Review | — |
| HTML-picture | [components/picture.html](components/picture.html) | `C/picture/`; `D/components/media/media-container/` | Added focal-point/debug/lazy/zoom coverage, replaced untracked local placeholder source URLs with official EC demo media, and preserved source alias/empty-input edge cases. | Verified | v5.3.1 / 2026-09-25 / S006; tagged Picture source/tests/snapshot, parser checks, fresh Picture browser smoke with no missing local requests |
| HTML-popover | [components/popover.html](components/popover.html) | `C/popover/`; `D/components/popover/` | Live HTML matches disk; audit official EC variants, dependencies, accessibility and behavior. | Review | — |
| HTML-quiz | [components/quiz.html](components/quiz.html) | `C/quiz/`; `D/components/quiz/` | Target Twig differs in this family; review HTML against the new contract, demos and EC snapshots. | Review | — |
| HTML-radio | [components/radio.html](components/radio.html) | `C/radio/`; `D/components/forms/radio/` | Existing examples already cover radio group/button, disabled/helper/invalid, binary, minimal/empty output and all EC color modes; no HTML mutation was required. | Verified | v5.3.1 / 2026-09-25 / S012; tagged README/demo/story/tests/snapshots/changelog, static ID/label/state checks, live MCP/disk match and browser accessibility/DOM smoke |
| HTML-range | [components/range.html](components/range.html) | `C/range/`; `D/components/forms/range/` | Aligned range examples with the v5.3.1 input/container/value-hook contract, including required, disabled, invalid, widths, extensions, empty output and real instances for all EC color modes. | Verified | v5.3.1 / 2026-09-25 / S013; tagged README/demo/story/tests/snapshots/changelog, static ID/ARIA/hook checks, live MCP/disk match and browser range smoke |
| HTML-rating-field | [components/rating-field.html](components/rating-field.html) | `C/rating-field/`; `D/components/forms/rating-field/` | Aligned rating examples with the v5.3.1 accessible label-before-input order, ascending values, checked/disabled/minimal/empty branches and all EC color modes. | Verified | v5.3.1 / 2026-09-25 / S013; tagged README/demo/story/tests/snapshots/changelog, static label/order/ID checks, live MCP/disk match and browser accessibility smoke |
| HTML-search-form | [components/search-form.html](components/search-form.html) | `C/search-form/`; `D/components/forms/search-form/` | Aligned examples with the v5.3.1 no-duplicate-role form contract, accessible button label, placeholder fallback, extension hooks, disabled/no-input/no-button branches and EC color modes. | Verified | v5.3.1 / 2026-09-25 / S011; tagged README/demo/story/tests/snapshots/changelog, static ID/ARIA/role checks, live MCP/disk match and browser accessibility/DOM smoke |
| HTML-select | [components/select.html](components/select.html) | `C/select/`; `D/components/forms/select/` | Existing examples already cover single/multiple select, option groups/states, required/disabled/invalid states, widths, extension hooks, multiple search/select-all/submit/clear behavior, empty output and all EC color modes; no HTML mutation was required. | Verified | v5.3.1 / 2026-09-25 / S012; tagged README/demo/story/tests/snapshots/changelog, static ID/ARIA/hook checks, live MCP/disk match and browser select accessibility/runtime smoke |
| HTML-separator | [components/separator.html](components/separator.html) | `C/separator/`; `D/components/divider/` | Live HTML matches disk; audit official EC variants, dependencies, accessibility and behavior. | Review | — |
| HTML-site-footer | [components/site-footer.html](components/site-footer.html) | `C/site-footer/`; `D/components/site-wide/site-footer/` | EC examples and empty/color-mode roots retained; accidental EU harmonised example and EU empty output removed. Full component-example audit remains open. | Updated | v5.3.1 / 2026-09-25 / S003; EC-scope review, parser and MCP delivery checks |
| HTML-site-header | [components/site-header.html](components/site-header.html) | `C/site-header/`; `D/components/site-wide/site-header/` | EC header examples use button-based search toggles, dialog-labelled forms and clean EC scope; the tagged Twig is paired. Full component-example audit remains open. | Updated | v5.3.1 / 2026-09-25 / S003; tagged pairing, parser and MCP delivery checks |
| HTML-skip-link | [components/skip-link.html](components/skip-link.html) | `C/skip-link/`; `D/components/navigation/skip-link/` | Live HTML matches disk; audit official EC variants, dependencies, accessibility and behavior. | Review | — |
| HTML-slogan-ticker | [components/slogan-ticker.html](components/slogan-ticker.html) | `C/slogan-ticker/`; `D/components/slogan-ticker/` | Target Twig differs in this family; review HTML against the new contract, demos and EC snapshots. | Review | — |
| HTML-social-media-follow | [components/social-media-follow.html](components/social-media-follow.html) | `C/social-media-follow/`; `D/components/social-media-follow/` | Target Twig differs in this family; review HTML against the new contract, demos and EC snapshots. | Review | — |
| HTML-spinner | [components/spinner.html](components/spinner.html) | `C/spinner/`; `D/components/loading-indicator/` | Live HTML matches disk; audit official EC variants, dependencies, accessibility and behavior. | Review | — |
| HTML-splash-page | [components/splash-page.html](components/splash-page.html) | `C/splash-page/`; `D/components/splash-page/` | Target Twig differs in this family; review HTML against the new contract, demos and EC snapshots. | Review | — |
| HTML-spotlight | [components/spotlight.html](components/spotlight.html) | `C/spotlight/`; `D/components/spotlight/` | Live HTML matches disk; audit official EC variants, dependencies, accessibility and behavior. | Review | — |
| HTML-table | [components/table.html](components/table.html) | `C/table/`; `D/components/table/` | Added the v5.3.1 sort marker and a filterable EC table with labelled column fields, multiple rows, unique header relationships and mobile header data; existing simple, zebra, multi-header and extension coverage remains. | Verified | v5.3.1 / 2026-09-25 / S007; tagged README/demo/story/snapshot/docs, parser checks, live MCP/disk match and browser filter/sort smoke |
| HTML-tabs | [components/tabs.html](components/tabs.html) | `C/tabs/`; `D/components/navigation/tabs/` | Live HTML matches disk; audit official EC variants, dependencies, accessibility and behavior. | Review | — |
| HTML-tag | [components/tag.html](components/tag.html) | `C/tag/`; `D/components/tag/` | Live HTML matches disk; audit official EC variants, dependencies, accessibility and behavior. | Review | — |
| HTML-text-area | [components/text-area.html](components/text-area.html) | `C/text-area/`; `D/components/forms/text-area/` | Existing examples already cover default/value, invalid, disabled, required, readonly, widths, extension attributes, empty output and all EC color modes; no HTML mutation was required. | Verified | v5.3.1 / 2026-09-25 / S012; tagged README/demo/story/tests/snapshots/changelog, static state/ID checks, live MCP/disk match and browser accessibility/DOM smoke |
| HTML-text-input | [components/text-input.html](components/text-input.html) | `C/text-input/`; `D/components/forms/text-field/` | Existing examples already cover default/named/type, invalid, disabled, required, readonly, widths, extension attributes, empty output and all EC color modes; no HTML mutation was required. | Verified | v5.3.1 / 2026-09-25 / S012; tagged README/demo/story/tests/snapshots/changelog, static state/ID checks, live MCP/disk match and browser accessibility/DOM smoke |
| HTML-text-media | [components/text-media.html](components/text-media.html) | `C/text-media/`; `D/components/media/text-and-media/` | Audited image/video/primary/full-width/EC color-mode variants; unique title IDs and link aria-describedby relationships are retained with nested Media Container hooks. | Verified | v5.3.1 / 2026-09-25 / S006; tagged text-media data/story/snapshot/docs, parser/ARIA checks, live MCP/disk match and narrow scoped layout/browser smoke |
| HTML-timeline | [components/timeline.html](components/timeline.html) | `C/timeline/`; `D/components/timeline/` | Live HTML matches disk; audit official EC variants, dependencies, accessibility and behavior. | Review | — |
| HTML-tooltip | [components/tooltip.html](components/tooltip.html) | `C/tooltip/`; `D/components/tooltip/` | Live HTML works; listed Twig call fails. Upstream has no standalone tooltip Twig: resolve discovery/contract, do not invent one. | Review | — |
| HTML-unordered-list | [components/unordered-list.html](components/unordered-list.html) | `C/unordered-list/`; `D/components/list/` | Live HTML matches disk; audit official EC variants, dependencies, accessibility and behavior. | Review | — |
| HTML-video | [components/video.html](components/video.html) | `C/video/`; `D/components/media/media-container/` | Added accessible labels to autoplay/partial/empty/color-mode preview cases; default/multiple source/caption/zoom coverage is retained. | Verified | v5.3.1 / 2026-09-25 / S006; tagged video README/data/snapshot, parser/ARIA checks, live MCP/disk match and browser smoke |
| HTML-highlighted-search | [components/highlighted-search.html](components/highlighted-search.html) | `C/highlighted-search/`; `D/components/highlighted-search/` | Added EC default and blue-mode examples with labelled GET/POST search forms, helper text, suggestions, valid IDs and the target magnifying-glass hook. | Verified | v5.3.1 / 2026-09-25 / S004; official EC component index/showcase, tagged snapshot/data, parser/ARIA checks, live MCP and browser accessibility smoke |
| HTML-story-card | [components/story-card.html](components/story-card.html) | `C/story-card/`; `D/components/story-card/` | Added story and testimonial variants with mobile carousel hooks, desktop tablist/panels, slider pager controls, author/source metadata and unique tab relationships. Desktop and narrow-width next-card selection passed. | Verified | v5.3.1 / 2026-09-25 / S005; S004 official/tagged source, parser/ARIA and live MCP checks, desktop plus narrow-width browser smoke |

## Twig files — 91 existing, 2 missing references

Every existing Twig file is listed, including helpers. Initial byte comparison against v5.3.1: **54 identical, 31 different, 2 absent upstream**. All 87 are delivered through at least one existing prefix lookup. Identity is source evidence only; it does not certify a component or its dependencies.

| ID | Local item / lookup | Target reference | Finding / next action | Status | Verified version / date / evidence |
| --- | --- | --- | --- | --- | --- |
| TWIG-accordion | [components/accordion.html.twig](components/accordion.html.twig) | `C/accordion/accordion.html.twig` | Exact v5.3.1 source; adds the `open` item parameter and configurable sidebar media-query attribute while preserving the icon fallback, color modes, names and extension attributes. | Verified | v5.3.1 / 2026-09-25 / S008; exact tagged comparison, live MCP template match and browser runtime smoke |
| TWIG-add-to-calendar | [components/add-to-calendar.html.twig](components/add-to-calendar.html.twig) | `C/add-to-calendar/add-to-calendar.html.twig` | Byte-identical to target Twig; still review dependencies, EC usage and paired HTML. | Review | — |
| TWIG-animated-numbers | [components/animated-numbers.html.twig](components/animated-numbers.html.twig) | `C/animated-numbers/animated-numbers.html.twig` | Differs from target Twig; review diff, update and validate its complete component family. | Needs update | — |
| TWIG-banner | [components/banner.html.twig](components/banner.html.twig) | `C/banner/banner.html.twig` | Byte-identical to target Twig; still review dependencies, EC usage and paired HTML. | Review | — |
| TWIG-blockquote | [components/blockquote.html.twig](components/blockquote.html.twig) | `C/blockquote/blockquote.html.twig` | Differs from target Twig; review diff, update and validate its complete component family. | Needs update | — |
| TWIG-breadcrumb | [components/breadcrumb.html.twig](components/breadcrumb.html.twig) | `C/breadcrumb/breadcrumb.html.twig` | Byte-identical to target Twig; still review dependencies, EC usage and paired HTML. | Review | — |
| TWIG-button | [components/button.html.twig](components/button.html.twig) | `C/button/button.html.twig` | Byte-identical to target Twig; still review dependencies, EC usage and paired HTML. | Review | — |
| TWIG-card | [components/card.html.twig](components/card.html.twig) | `C/card/card.html.twig` | Byte-identical to target Twig; still review dependencies, EC usage and paired HTML. | Review | — |
| TWIG-carousel | [components/carousel.html.twig](components/carousel.html.twig) | `C/carousel/carousel.html.twig` | Replaced with the exact v5.3.1 source; carousel family lookup also returns the shared slider-pager helper. | Verified | v5.3.1 / 2026-09-25 / S004; exact tagged source, live family lookup and runtime smoke |
| TWIG-category-filter-items | [components/category-filter-items.html.twig](components/category-filter-items.html.twig) | `C/category-filter/category-filter-items.html.twig` | Byte-identical to target Twig; still review dependencies, EC usage and paired HTML. | Review | — |
| TWIG-category-filter | [components/category-filter.html.twig](components/category-filter.html.twig) | `C/category-filter/category-filter.html.twig` | Byte-identical to target Twig; still review dependencies, EC usage and paired HTML. | Review | — |
| TWIG-checkbox-group | [components/checkbox-group.html.twig](components/checkbox-group.html.twig) | `C/checkbox/checkbox-group.html.twig` | Exact pinned v5.3.1 source; group/item composition, required/invalid propagation, single-item feedback and paired HTML are verified. | Verified | v5.3.1 / 2026-09-25 / S012; exact tagged comparison, live MCP template match and browser checkbox smoke |
| TWIG-checkbox-item | [components/checkbox-item.html.twig](components/checkbox-item.html.twig) | `C/checkbox/checkbox-item.html.twig` | Exact pinned v5.3.1 source; disabled/invalid classes, helper relationships and required/optional indicators are verified with paired HTML. | Verified | v5.3.1 / 2026-09-25 / S012; exact tagged comparison, live MCP template match and browser checkbox smoke |
| TWIG-content-block | [components/content-block.html.twig](components/content-block.html.twig) | `C/content-block/content-block.html.twig` | Byte-identical to target Twig; still review dependencies, EC usage and paired HTML. | Review | — |
| TWIG-content-item | [components/content-item.html.twig](components/content-item.html.twig) | `C/content-item/content-item.html.twig` | Byte-identical to target Twig; still review dependencies, EC usage and paired HTML. | Review | — |
| TWIG-date-block | [components/date-block.html.twig](components/date-block.html.twig) | `C/date-block/date-block.html.twig` | Byte-identical to target Twig; still review dependencies, EC usage and paired HTML. | Review | — |
| TWIG-datepicker | [components/datepicker.html.twig](components/datepicker.html.twig) | `C/datepicker/datepicker.html.twig` | Exact pinned v5.3.1 source; Duet attributes, Datepicker auto-init, invalid/disabled/required propagation and paired HTML are verified. | Verified | v5.3.1 / 2026-09-25 / S012; exact tagged comparison, live MCP template match and browser date-picker smoke |
| TWIG-description-list | [components/description-list.html.twig](components/description-list.html.twig) | `C/description-list/description-list.html.twig` | Exact v5.3.1 source; inline-link definitions now support both link objects and plain text, with current trimming and the existing link/tag helper contracts. | Verified | v5.3.1 / 2026-09-25 / S009; exact tagged comparison, byte-identical link/tag dependency checks, live MCP template match and browser runtime smoke |
| TWIG-expandable | [components/expandable.html.twig](components/expandable.html.twig) | `C/expandable/expandable.html.twig` | Byte-identical to target Twig; still review dependencies, EC usage and paired HTML. | Review | — |
| TWIG-fact-figures | [components/fact-figures.html.twig](components/fact-figures.html.twig) | `C/fact-figures/fact-figures.html.twig` | Exact v5.3.1 source: per-item/global source macro, individual source labels, plain-text/link sources, `no_icon_wrapping`, value/title fallbacks and current view-all/icon behavior. Existing link and icon dependencies are byte-identical. | Verified | v5.3.1 / 2026-09-25 / S010; exact tagged comparison, dependency checks, live MCP template match and browser smoke |
| TWIG-featured-item | [components/featured-item.html.twig](components/featured-item.html.twig) | `C/featured-item/featured-item.html.twig` | Byte-identical to target Twig; still review dependencies, EC usage and paired HTML. | Review | — |
| TWIG-file-translation-item | [components/file-translation-item.html.twig](components/file-translation-item.html.twig) | Absent at target; see `C/file/` | Retained only for traceability and excluded from active EC lookup: v5.3.1 inlines translation markup in `file.html.twig`, and no active local caller references this legacy helper. | Excluded | v5.3.1 / 2026-09-25 / S005; tagged file source and local `rg` reference audit |
| TWIG-file-translations | [components/file-translations.html.twig](components/file-translations.html.twig) | Absent at target; see `C/file/` | Retained only for traceability and excluded from active EC lookup: v5.3.1 inlines translation markup in `file.html.twig`, and no active local caller references this legacy helper. | Excluded | v5.3.1 / 2026-09-25 / S005; tagged file source and local `rg` reference audit |
| TWIG-file-upload | [components/file-upload.html.twig](components/file-upload.html.twig) | `C/file-upload/file-upload.html.twig` | Exact pinned v5.3.1 source; single/multiple, disabled/invalid classes, button labels and file-list hooks are verified with paired HTML. | Verified | v5.3.1 / 2026-09-25 / S012; exact tagged comparison, live MCP template match and browser file-upload smoke |
| TWIG-file | [components/file.html.twig](components/file.html.twig) | `C/file/file.html.twig` | Replaced with the exact pinned v5.3.1 source; deprecated variant/detail-meta inputs remain documented for compatibility while translation markup is inline. | Verified | v5.3.1 / 2026-09-25 / S005; exact tagged comparison, file-family MCP template call and browser smoke |
| TWIG-form-group | [components/form-group.html.twig](components/form-group.html.twig) | `C/form-group/form-group.html.twig` | Exact pinned v5.3.1 source: label-wrapper markup keeps required/optional indicators visible when the inner label is hidden and preserves all supported input branches and extension hooks. | Verified | v5.3.1 / 2026-09-25 / S011; exact tagged comparison, datepicker/file-upload/select/text-area/text-input/checkbox/radio dependency checks, live MCP template match and browser smoke |
| TWIG-gallery-item | [components/gallery-item.html.twig](components/gallery-item.html.twig) | `C/gallery/gallery-item.html.twig` | Replaced with the exact pinned v5.3.1 media-item source, including video, publication-date, duration and title-visibility hooks. | Verified | v5.3.1 / 2026-09-25 / S005; exact tagged comparison, gallery-family MCP template call and browser smoke |
| TWIG-gallery-overlay | [components/gallery-overlay.html.twig](components/gallery-overlay.html.twig) | `C/gallery/gallery-overlay.html.twig` | Replaced with the exact pinned v5.3.1 overlay source, including date output and duplicated mobile actions. | Verified | v5.3.1 / 2026-09-25 / S005; exact tagged comparison, gallery-family MCP template call and browser smoke |
| TWIG-gallery | [components/gallery.html.twig](components/gallery.html.twig) | `C/gallery/gallery.html.twig` | Replaced with the exact pinned v5.3.1 gallery source and validated against the paired item/overlay family. | Verified | v5.3.1 / 2026-09-25 / S005; exact tagged comparison, gallery-family MCP template call and browser smoke |
| TWIG-highlight-box | [components/highlight-box.html.twig](components/highlight-box.html.twig) | `C/highlight-box/highlight-box.html.twig` | Byte-identical to target Twig; still review dependencies, EC usage and paired HTML. | Review | — |
| TWIG-icon | [components/icon.html.twig](components/icon.html.twig) | `C/icon/icon.html.twig` | Byte-identical to target Twig; still review dependencies, EC usage and paired HTML. | Review | — |
| TWIG-indicator | [components/indicator.html.twig](components/indicator.html.twig) | `C/indicator/indicator.html.twig` | Byte-identical to target Twig; still review dependencies, EC usage and paired HTML. | Review | — |
| TWIG-inpage-navigation | [components/inpage-navigation.html.twig](components/inpage-navigation.html.twig) | `C/inpage-navigation/inpage-navigation.html.twig` | Byte-identical to target Twig; still review dependencies, EC usage and paired HTML. | Review | — |
| TWIG-label | [components/label.html.twig](components/label.html.twig) | `C/label/label.html.twig` | Byte-identical to target Twig; still review dependencies, EC usage and paired HTML. | Review | — |
| TWIG-link | [components/link.html.twig](components/link.html.twig) | `C/link/link.html.twig` | Exact v5.3.1 source; tertiary styles, no-icon-wrapping and label relationships are validated with the paired HTML example. | Verified | v5.3.1 / 2026-09-25 / S006; exact tagged source, MCP template match and browser link smoke |
| TWIG-list-illustration-item | [components/list-illustration-item.html.twig](components/list-illustration-item.html.twig) | `C/list-illustration/list-illustration-item.html.twig` | Byte-identical to target Twig; still review dependencies, EC usage and paired HTML. | Review | — |
| TWIG-list-illustration | [components/list-illustration.html.twig](components/list-illustration.html.twig) | `C/list-illustration/list-illustration.html.twig` | Byte-identical to target Twig; still review dependencies, EC usage and paired HTML. | Review | — |
| TWIG-media-container | [components/media-container.html.twig](components/media-container.html.twig) | `C/media-container/media-container.html.twig` | Byte-identical to v5.3.1 and validated with the paired image/video/embed, ratio and expandable examples. | Verified | v5.3.1 / 2026-09-25 / S006; exact tagged source, MCP template match, parser/ARIA checks and browser smoke |
| TWIG-mega-menu-featured-item | [components/mega-menu-featured-item.html.twig](components/mega-menu-featured-item.html.twig) | `C/mega-menu/mega-menu-featured-item.html.twig` | Byte-identical to target Twig; still review dependencies, EC usage and paired HTML. | Review | — |
| TWIG-mega-menu-item | [components/mega-menu-item.html.twig](components/mega-menu-item.html.twig) | `C/mega-menu/mega-menu-item.html.twig` | Aligned to the pinned EC source with local trailing-whitespace normalization; paired family delivery is live, while the rendered example remains a later audit. | Updated | v5.3.1 / 2026-09-25 / S003; tagged source comparison and live family lookup |
| TWIG-mega-menu | [components/mega-menu.html.twig](components/mega-menu.html.twig) | `C/mega-menu/mega-menu.html.twig` | Aligned to the pinned EC source with local whitespace normalization; paired family delivery is live, while the rendered example remains a later audit. | Updated | v5.3.1 / 2026-09-25 / S003; tagged source comparison and live family lookup |
| TWIG-menu-item | [components/menu-item.html.twig](components/menu-item.html.twig) | `C/menu/menu-item.html.twig` | Byte-identical to target Twig; still review dependencies, EC usage and paired HTML. | Review | — |
| TWIG-menu | [components/menu.html.twig](components/menu.html.twig) | `C/menu/menu.html.twig` | Byte-identical to target Twig; still review dependencies, EC usage and paired HTML. | Review | — |
| TWIG-modal | [components/modal.html.twig](components/modal.html.twig) | `C/modal/modal.html.twig` | Byte-identical to target Twig; still review dependencies, EC usage and paired HTML. | Review | — |
| TWIG-navigation-list-item | [components/navigation-list-item.html.twig](components/navigation-list-item.html.twig) | `C/navigation-list/navigation-list-item.html.twig` | Byte-identical to target Twig; still review dependencies, EC usage and paired HTML. | Review | — |
| TWIG-navigation-list | [components/navigation-list.html.twig](components/navigation-list.html.twig) | `C/navigation-list/navigation-list.html.twig` | Byte-identical to target Twig; still review dependencies, EC usage and paired HTML. | Review | — |
| TWIG-news-ticker | [components/news-ticker.html.twig](components/news-ticker.html.twig) | `C/news-ticker/news-ticker.html.twig` | Exact v5.3.1 source: adds color mode, Phosphor/default newspaper media, slide icon/content wrappers, branded links, deprecated image compatibility and LTR counter while preserving the required initialization hooks. | Verified | v5.3.1 / 2026-09-25 / S007; exact tagged source, MCP template match and browser initialization/control smoke |
| TWIG-notification | [components/notification.html.twig](components/notification.html.twig) | `C/notification/notification.html.twig` | Byte-identical to target Twig; still review dependencies, EC usage and paired HTML. | Review | — |
| TWIG-ordered-list | [components/ordered-list.html.twig](components/ordered-list.html.twig) | `C/ordered-list/ordered-list.html.twig` | Byte-identical to target Twig; still review dependencies, EC usage and paired HTML. | Review | — |
| TWIG-page-header-expandable | [components/page-header-expandable.html.twig](components/page-header-expandable.html.twig) | `C/page-header/page-header-expandable.html.twig` | Byte-identical to target Twig; still review dependencies, EC usage and paired HTML. | Review | — |
| TWIG-page-header | [components/page-header.html.twig](components/page-header.html.twig) | `C/page-header/page-header.html.twig` | Replaced with the exact pinned EC source; paired family delivery is live, while the rendered example remains a later audit. | Updated | v5.3.1 / 2026-09-25 / S003; exact tagged source and live family lookup |
| TWIG-page-information | [components/page-information.html.twig](components/page-information.html.twig) | `C/page-information/page-information.html.twig` | Byte-identical to target Twig; still review dependencies, EC usage and paired HTML. | Review | — |
| TWIG-page-summary | [components/page-summary.html.twig](components/page-summary.html.twig) | `C/page-summary/page-summary.html.twig` | Exact pinned v5.3.1 source with `color_mode` parameter/class handling, preserved section labelling, icon/title behavior and extension attributes. | Verified | v5.3.1 / 2026-09-25 / S011; exact tagged comparison, live MCP template match and browser color-mode/ARIA smoke |
| TWIG-pagination | [components/pagination.html.twig](components/pagination.html.twig) | `C/pagination/pagination.html.twig` | Byte-identical to target Twig; still review dependencies, EC usage and paired HTML. | Review | — |
| TWIG-picture | [components/picture.html.twig](components/picture.html.twig) | `C/picture/picture.html.twig` | Exact v5.3.1 focal-point/debug source; source aliases, image attributes and runtime initialization are validated. | Verified | v5.3.1 / 2026-09-25 / S006; exact tagged source, MCP template match, parser checks and fresh Picture browser smoke |
| TWIG-popover | [components/popover.html.twig](components/popover.html.twig) | `C/popover/popover.html.twig` | Byte-identical to target Twig; still review dependencies, EC usage and paired HTML. | Review | — |
| TWIG-quiz-card | [components/quiz-card.html.twig](components/quiz-card.html.twig) | `C/quiz/quiz-card.html.twig` | Differs from target Twig; review diff, update and validate its complete component family. | Needs update | — |
| TWIG-quiz | [components/quiz.html.twig](components/quiz.html.twig) | `C/quiz/quiz.html.twig` | Differs from target Twig; review diff, update and validate its complete component family. | Needs update | — |
| TWIG-radio-button | [components/radio-button.html.twig](components/radio-button.html.twig) | `C/radio/radio-button.html.twig` | Exact pinned v5.3.1 source; disabled/invalid/binary classes and helper relationships are verified with paired HTML. | Verified | v5.3.1 / 2026-09-25 / S012; exact tagged comparison, live MCP template match and browser radio smoke |
| TWIG-radio-group | [components/radio-group.html.twig](components/radio-group.html.twig) | `C/radio/radio-group.html.twig` | Exact pinned v5.3.1 source; item propagation, empty output and binary mode are verified with paired HTML. | Verified | v5.3.1 / 2026-09-25 / S012; exact tagged comparison, live MCP template match and browser radio smoke |
| TWIG-range | [components/range.html.twig](components/range.html.twig) | `C/range/range.html.twig` | Exact pinned v5.3.1 source; range input/container/value hooks, width/status attributes and `aria-describedby` handling are verified with paired HTML. | Verified | v5.3.1 / 2026-09-25 / S013; exact tagged comparison, live MCP template match and browser range smoke |
| TWIG-rating-field | [components/rating-field.html.twig](components/rating-field.html.twig) | `C/rating-field/rating-field.html.twig` | Updated to the exact pinned v5.3.1 source: items remain ascending and each accessible label precedes its radio input. | Verified | v5.3.1 / 2026-09-25 / S013; exact tagged comparison, rating snapshot/order review, live MCP template match and browser accessibility smoke |
| TWIG-search-form | [components/search-form.html.twig](components/search-form.html.twig) | `C/search-form/search-form.html.twig` | Exact pinned v5.3.1 source: removes the duplicate `role="search"` from the form wrapper while preserving form-group/button composition and extension blocks. | Verified | v5.3.1 / 2026-09-25 / S011; exact tagged comparison, live MCP template match and browser role/ARIA smoke |
| TWIG-select | [components/select.html.twig](components/select.html.twig) | `C/select/select.html.twig` | Exact pinned v5.3.1 source; single/multiple attributes, labels, option states and submit/search/clear configuration are verified with paired HTML. | Verified | v5.3.1 / 2026-09-25 / S012; exact tagged comparison, live MCP template match and browser select smoke |
| TWIG-separator | [components/separator.html.twig](components/separator.html.twig) | `C/separator/separator.html.twig` | Byte-identical to target Twig; still review dependencies, EC usage and paired HTML. | Review | — |
| TWIG-site-footer-ec-section | [components/site-footer-ec-section.html.twig](components/site-footer-ec-section.html.twig) | `C/site-footer/site-footer-ec-section.html.twig` | Aligned to the pinned EC source with local trailing-whitespace normalization; paired family delivery is live, while the rendered example remains a later audit. | Updated | v5.3.1 / 2026-09-25 / S003; tagged source comparison and live family lookup |
| TWIG-site-footer-ec | [components/site-footer-ec.html.twig](components/site-footer-ec.html.twig) | `C/site-footer/site-footer-ec.html.twig` | Replaced with the exact pinned EC source; paired family delivery is live, while the rendered example remains a later audit. | Updated | v5.3.1 / 2026-09-25 / S003; exact tagged source and live family lookup |
| TWIG-site-footer-eu | [components/site-footer-eu.html.twig](components/site-footer-eu.html.twig) | `C/site-footer/site-footer-eu.html.twig` | Legacy EU file remains on disk for traceability but is deliberately excluded from active EC `site-footer` discovery; no EU content was refreshed. | Excluded | v5.3.1 / 2026-09-25 / S003; EC scope decision and exact-family lookup |
| TWIG-site-header-language-switcher | [components/site-header-language-switcher.html.twig](components/site-header-language-switcher.html.twig) | `C/site-header/site-header-language-switcher.html.twig` | Replaced with the exact pinned EC source; paired family delivery is live, while the rendered example remains a later audit. | Updated | v5.3.1 / 2026-09-25 / S003; exact tagged source and live family lookup |
| TWIG-site-header | [components/site-header.html.twig](components/site-header.html.twig) | `C/site-header/site-header.html.twig` | Replaced with the exact pinned EC source; EC search dialog and language-switcher helpers are paired; rendered example audit remains open. | Updated | v5.3.1 / 2026-09-25 / S003; exact tagged source, parser and live family lookup |
| TWIG-skip-link | [components/skip-link.html.twig](components/skip-link.html.twig) | `C/skip-link/skip-link.html.twig` | Byte-identical to target Twig; still review dependencies, EC usage and paired HTML. | Review | — |
| TWIG-slogan-ticker | [components/slogan-ticker.html.twig](components/slogan-ticker.html.twig) | `C/slogan-ticker/slogan-ticker.html.twig` | Differs from target Twig; review diff, update and validate its complete component family. | Needs update | — |
| TWIG-social-media-follow | [components/social-media-follow.html.twig](components/social-media-follow.html.twig) | `C/social-media-follow/social-media-follow.html.twig` | Differs from target Twig; review diff, update and validate its complete component family. | Needs update | — |
| TWIG-spinner | [components/spinner.html.twig](components/spinner.html.twig) | `C/spinner/spinner.html.twig` | Byte-identical to target Twig; still review dependencies, EC usage and paired HTML. | Review | — |
| TWIG-splash-page | [components/splash-page.html.twig](components/splash-page.html.twig) | `C/splash-page/splash-page.html.twig` | Differs from target Twig; review diff, update and validate its complete component family. | Needs update | — |
| TWIG-spotlight | [components/spotlight.html.twig](components/spotlight.html.twig) | `C/spotlight/spotlight.html.twig` | Byte-identical to target Twig; still review dependencies, EC usage and paired HTML. | Review | — |
| TWIG-table | [components/table.html.twig](components/table.html.twig) | `C/table/table.html.twig` | Exact v5.3.1 source: adds filter and filter-label parameters, independent sort/filter initialization attributes and header filter hooks while preserving multi-header column mapping. | Verified | v5.3.1 / 2026-09-25 / S007; exact tagged source, MCP template match and browser filter/sort smoke |
| TWIG-tabs | [components/tabs.html.twig](components/tabs.html.twig) | `C/tabs/tabs.html.twig` | Byte-identical to target Twig; still review dependencies, EC usage and paired HTML. | Review | — |
| TWIG-tag-set | [components/tag-set.html.twig](components/tag-set.html.twig) | `C/tag/tag-set.html.twig` | Byte-identical to target Twig; still review dependencies, EC usage and paired HTML. | Review | — |
| TWIG-tag | [components/tag.html.twig](components/tag.html.twig) | `C/tag/tag.html.twig` | Byte-identical to target Twig; still review dependencies, EC usage and paired HTML. | Review | — |
| TWIG-text-area | [components/text-area.html.twig](components/text-area.html.twig) | `C/text-area/text-area.html.twig` | Exact pinned v5.3.1 source; invalid/disabled/required/width/extension branches are verified with paired HTML. | Verified | v5.3.1 / 2026-09-25 / S012; exact tagged comparison, live MCP template match and browser text-area smoke |
| TWIG-text-input | [components/text-input.html.twig](components/text-input.html.twig) | `C/text-input/text-input.html.twig` | Exact pinned v5.3.1 source; type/width/status/extension branches are verified with paired HTML. | Verified | v5.3.1 / 2026-09-25 / S012; exact tagged comparison, live MCP template match and browser text-input smoke |
| TWIG-text-media | [components/text-media.html.twig](components/text-media.html.twig) | `C/text-media/text-media.html.twig` | Byte-identical to v5.3.1 and validated with the paired image/video, link and nested media-container examples. | Verified | v5.3.1 / 2026-09-25 / S006; exact tagged source, MCP template match and paired browser smoke |
| TWIG-timeline-set | [components/timeline-set.html.twig](components/timeline-set.html.twig) | `C/timeline/timeline-set.html.twig` | Byte-identical to target Twig; still review dependencies, EC usage and paired HTML. | Review | — |
| TWIG-timeline | [components/timeline.html.twig](components/timeline.html.twig) | `C/timeline/timeline.html.twig` | Byte-identical to target Twig; still review dependencies, EC usage and paired HTML. | Review | — |
| TWIG-unordered-list | [components/unordered-list.html.twig](components/unordered-list.html.twig) | `C/unordered-list/unordered-list.html.twig` | Byte-identical to target Twig; still review dependencies, EC usage and paired HTML. | Review | — |
| TWIG-video | [components/video.html.twig](components/video.html.twig) | `C/video/video.html.twig` | Byte-identical to v5.3.1 and validated with standalone source, track, poster, zoom and accessible-label examples. | Verified | v5.3.1 / 2026-09-25 / S006; exact tagged source, MCP template match, parser/ARIA checks and browser smoke |
| TWIG-highlighted-search | [components/highlighted-search.html.twig](components/highlighted-search.html.twig) | `C/highlighted-search/highlighted-search.html.twig` | Added the exact v5.3.1 template; its existing form-group, icon, button and tag-set dependencies remain shared local templates. | Verified | v5.3.1 / 2026-09-25 / S004; exact tagged source and live lookup |
| TWIG-slider-pager | [components/slider-pager.html.twig](components/slider-pager.html.twig) | `C/slider/slider-pager.html.twig` | Added the exact shared v5.3.1 pager helper and return it with carousel/story-card families; no standalone HTML ID was invented. | Verified | v5.3.1 / 2026-09-25 / S004; exact tagged source and live dependent-family lookups |
| TWIG-story-card | [components/story-card.html.twig](components/story-card.html.twig) | `C/story-card/story-card.html.twig` | Added the exact v5.3.1 story-card template, including mobile carousel, desktop grid and keyboard/tab relationships. | Verified | v5.3.1 / 2026-09-25 / S004; exact tagged source and live family lookup |
| TWIG-story-card-card | [components/story-card-card.html.twig](components/story-card-card.html.twig) | `C/story-card/story-card-card.html.twig` | Added the exact v5.3.1 story-card content helper, including testimonial metadata and tab-aware link description. | Verified | v5.3.1 / 2026-09-25 / S004; exact tagged source and live family lookup |
| TWIG-file-upload-status | [components/file-upload-status.html.twig](components/file-upload-status.html.twig) | `X/file-upload-status/file-upload-status.html.twig` | Added the official EC `!dev` file-upload status composition as a scoped file-upload family helper; it renders upload progress, error text and Delete/Delete all links and reuses local spinner/link helpers. | Verified | v5.3.1 / 2026-09-25 / S013; exact tagged comparison, dependency/family mapping checks and live MCP template match |
| TWIG-layout-wrapper | `components/layout-wrapper.html.twig` (absent) | `L/layout-wrapper/layout-wrapper.html.twig` | Shared layout missing locally; assess component/page usage. v5.3.1 fixes its extra spacing. | Missing | — |

## Bundled assets and fonts — 18 files

Use a pinned official EC distribution or reproducible build at the target commit. `P/ec/ecl-builder.config.js` records output filenames; our package flattens styles/scripts into `assets/`, with `fonts/` alongside. Record downloads/build commands, checksums and intentional transformations in the session evidence. Source maps must stay paired with their CSS.

| ID | Local item / lookup | Target reference | Finding / next action | Status | Verified version / date / evidence |
| --- | --- | --- | --- | --- | --- |
| ASSET-ecl-ec-color-modes.css | [assets/ecl-ec-color-modes.css](assets/ecl-ec-color-modes.css) | `P/ec/src/ec-color-modes.scss` | Unmodified official v5.3.1 distribution; reset/utilities before main, color modes after main, separate print media. Local paths and rendered integration checked. | Verified | v5.3.1 / 2026-09-25 / S002; checksum manifest, browser and live setup delivery |
| ASSET-ecl-ec-color-modes.css.map | [assets/ecl-ec-color-modes.css.map](assets/ecl-ec-color-modes.css.map) | `P/ec/src/ec-color-modes.scss` | Updated from official EC release; original mappings retained, pinned source URLs and embedded SCSS added. All source entries and paired CSS verified; see manifest. | Verified | v5.3.1 / 2026-09-25 / S002; checksum manifest, browser and live setup delivery |
| ASSET-ecl-ec-print.css | [assets/ecl-ec-print.css](assets/ecl-ec-print.css) | `P/ec/src/ec-print.scss` | Unmodified official v5.3.1 distribution; reset/utilities before main, color modes after main, separate print media. Local paths and rendered integration checked. | Verified | v5.3.1 / 2026-09-25 / S002; checksum manifest, browser and live setup delivery |
| ASSET-ecl-ec-print.css.map | [assets/ecl-ec-print.css.map](assets/ecl-ec-print.css.map) | `P/ec/src/ec-print.scss` | Updated from official EC release; original mappings retained, pinned source URLs and embedded SCSS added. All source entries and paired CSS verified; see manifest. | Verified | v5.3.1 / 2026-09-25 / S002; checksum manifest, browser and live setup delivery |
| ASSET-ecl-ec-utilities.css | [assets/ecl-ec-utilities.css](assets/ecl-ec-utilities.css) | `P/ec/src/ec-utilities.scss` | Unmodified official v5.3.1 distribution; reset/utilities before main, color modes after main, separate print media. Local paths and rendered integration checked. | Verified | v5.3.1 / 2026-09-25 / S002; checksum manifest, browser and live setup delivery |
| ASSET-ecl-ec-utilities.css.map | [assets/ecl-ec-utilities.css.map](assets/ecl-ec-utilities.css.map) | `P/ec/src/ec-utilities.scss` | Updated from official EC release; original mappings retained, pinned source URLs and embedded SCSS added. All source entries and paired CSS verified; see manifest. | Verified | v5.3.1 / 2026-09-25 / S002; checksum manifest, browser and live setup delivery |
| ASSET-ecl-ec.css | [assets/ecl-ec.css](assets/ecl-ec.css) | `P/ec/src/ec.scss` | Unmodified official v5.3.1 distribution; reset/utilities before main, color modes after main, separate print media. Local paths and rendered integration checked. | Verified | v5.3.1 / 2026-09-25 / S002; checksum manifest, browser and live setup delivery |
| ASSET-ecl-ec.css.map | [assets/ecl-ec.css.map](assets/ecl-ec.css.map) | `P/ec/src/ec.scss` | Updated from official EC release; original mappings retained, pinned source URLs and embedded SCSS added. All source entries and paired CSS verified; see manifest. | Verified | v5.3.1 / 2026-09-25 / S002; checksum manifest, browser and live setup delivery |
| ASSET-ecl-ec.js | [assets/ecl-ec.js](assets/ecl-ec.js) | `P/ec/src/ec.js` | Unmodified official v5.3.1 bundle; classic and module initialization exercised in Chrome. Header/menu smoke only; other component-family behavior remains pending. | Verified | v5.3.1 / 2026-09-25 / S002; checksum manifest, browser and live setup delivery |
| ASSET-ecl-esm-ec.js | [assets/ecl-esm-ec.js](assets/ecl-esm-ec.js) | `P/ec/src/ec-esm.js` | Unmodified official v5.3.1 bundle; classic and module initialization exercised in Chrome. Header/menu smoke only; other component-family behavior remains pending. | Verified | v5.3.1 / 2026-09-25 / S002; checksum manifest, browser and live setup delivery |
| ASSET-ecl-reset.css | [assets/ecl-reset.css](assets/ecl-reset.css) | `P/reset/src/reset.scss` | Unmodified official v5.3.1 distribution; reset/utilities before main, color modes after main, separate print media. Local paths and rendered integration checked. | Verified | v5.3.1 / 2026-09-25 / S002; checksum manifest, browser and live setup delivery |
| ASSET-favicon.ico | [assets/favicon.ico](assets/favicon.ico) | `R/favicons/ec-favicon.ico` | Retained byte-identical pinned EC resource; checksum recorded and local HTTP path checked. Both English logos rendered in the starter. | Verified | v5.3.1 / 2026-09-25 / S002; checksum manifest, browser and live setup delivery |
| ASSET-favicon.svg | [assets/favicon.svg](assets/favicon.svg) | `R/favicons/ec-favicon.svg` | Retained byte-identical pinned EC resource; checksum recorded and local HTTP path checked. Both English logos rendered in the starter. | Verified | v5.3.1 / 2026-09-25 / S002; checksum manifest, browser and live setup delivery |
| ASSET-logo-ec-negative-en.svg | [assets/logo-ec-negative-en.svg](assets/logo-ec-negative-en.svg) | `R/logo-ec/src/negative/logo-ec--en.svg` | Retained byte-identical pinned EC resource; checksum recorded and local HTTP path checked. Both English logos rendered in the starter. | Verified | v5.3.1 / 2026-09-25 / S002; checksum manifest, browser and live setup delivery |
| ASSET-logo-ec-positive-en.svg | [assets/logo-ec-positive-en.svg](assets/logo-ec-positive-en.svg) | `R/logo-ec/src/positive/logo-ec--en.svg` | Retained byte-identical pinned EC resource; checksum recorded and local HTTP path checked. Both English logos rendered in the starter. | Verified | v5.3.1 / 2026-09-25 / S002; checksum manifest, browser and live setup delivery |
| FONT-InterVariable-Italic.woff2 | [fonts/InterVariable-Italic.woff2](fonts/InterVariable-Italic.woff2) | `P/ec/fonts/InterVariable-Italic.woff2` | Retained byte-identical target font resource (Inter 4.1). Both local font fallbacks load successfully when WebTools returns 403; sibling layout preserved. | Verified | v5.3.1 / 2026-09-25 / S002; checksum manifest, browser and live setup delivery |
| FONT-InterVariable.woff2 | [fonts/InterVariable.woff2](fonts/InterVariable.woff2) | `P/ec/fonts/InterVariable.woff2` | Retained byte-identical target font resource (Inter 4.1). Both local font fallbacks load successfully when WebTools returns 403; sibling layout preserved. | Verified | v5.3.1 / 2026-09-25 / S002; checksum manifest, browser and live setup delivery |
| FONT-version.txt | [fonts/version.txt](fonts/version.txt) | `P/ec/fonts/version.txt` | Retained byte-identical target font resource (Inter 4.1). Both local font fallbacks load successfully when WebTools returns 403; sibling layout preserved. | Verified | v5.3.1 / 2026-09-25 / S002; checksum manifest, browser and live setup delivery |

## Asset coverage gaps

Optional upstream assets are candidates to assess, not instructions to copy every language or platform asset. Required resources for the chosen EC examples must be bundled or documented.

| ID | Local item / lookup | Target reference | Finding / next action | Status | Verified version / date / evidence |
| --- | --- | --- | --- | --- | --- |
| ASSET-default-css | `assets/ecl-ec-default.css` (absent) | `P/ec/src/ec-default.scss` | Not bundled this cycle: current examples use explicit ECL classes. GUIDE-assets documents upstream opt-in with the paired print file and .ecl namespace; reconsider if DOC-html-tag adopts a bare-tag example. | Excluded | v5.3.1 / 2026-09-25 / S002 scope decision |
| ASSET-default-print-css | `assets/ecl-ec-default-print.css` (absent) | `P/ec/src/ec-default-print.scss` | Paired with excluded default screen CSS; no bare-tag example currently requires it. Upstream opt-in is documented; reconsider together with DOC-html-tag. | Excluded | v5.3.1 / 2026-09-25 / S002 scope decision |
| ASSET-easy-to-read-css | `assets/ecl-ec-easy-to-read.css` (absent) | `P/ec/src/ec-easy-to-read.scss` | No current example uses .ecl-easy-to-read. Tagged stylesheet assessed and optional acquisition documented; add only with an explicit easy-to-read content use case. | Excluded | v5.3.1 / 2026-09-25 / S002 scope decision |
| ASSET-branding-coverage | Additional EC logos/favicons | `R/logo-ec/`; `R/favicons/`; `R/favicons-ec/` | Current English EC examples need the two existing logos and favicon pair only; all retained unchanged. Other language logos remain obtainable from the pinned archive. Deprecated platform-favicon package deliberately not copied; no EC resource changes apart from package metadata. | Verified | v5.3.1 / 2026-09-25 / S002; checksum manifest, browser and live setup delivery |
| ASSET-example-media | Referenced images, video, captions and illustrations | Selected `C/*/demo/`; `D/guidelines/images/` | Inventory dependencies during each component batch; supply durable example media or explain external requirements. | Review | — |

## Starter page and official page examples

The only existing complete page returned by this MCP is `starter-template.html`. Official page examples below are inventoried as reference/coverage decisions, not silently treated as new required tools.

| ID | Local item / lookup | Target reference | Finding / next action | Status | Verified version / date / evidence |
| --- | --- | --- | --- | --- | --- |
| PAGE-starter | [starter-template.html](starter-template.html) | `D/getting-started/`; `C/site-header/`; `C/mega-menu/`; `C/site-footer/`; `E/` | S003 replaced empty search attributes with a named button/dialog contract, removed CMS-only fields/links, changed the header modifier to standard Menu, and removed the legacy EU footer exposure. At 375px the accessible Search action opens/focuses the form and closes on Escape; Menu opens/closes. WebTools icons remain externally unavailable. | Verified | v5.3.1 / 2026-09-25 / S003; parser, live MCP, mobile/desktop browser smoke |
| PAGE-page-fact-sheet | `page-fact-sheet` (not exposed) | `E/page-fact-sheet/page-fact.html.twig` | Official page example is reference material for the starter/compositions. Assess useful EC coverage; add only with a recorded scope decision. | Review | — |
| PAGE-page-home | `page-home` (not exposed) | `E/page-home/page-home.html.twig` | Official page example is reference material for the starter/compositions. Assess useful EC coverage; add only with a recorded scope decision. | Review | — |
| PAGE-page-inner | `page-inner` (not exposed) | `E/page-inner/page-inner.html.twig` | Official page example is reference material for the starter/compositions. Assess useful EC coverage; add only with a recorded scope decision. | Review | — |
| PAGE-page-president | `page-president` (not exposed) | `E/page-president/page-president.html.twig` | Official page example is reference material for the starter/compositions. Assess useful EC coverage; add only with a recorded scope decision. | Review | — |
| PAGE-page-rich-text | `page-rich-text` (not exposed) | `E/page-rich-text/page-rich-text.html.twig` | Official page example is reference material for the starter/compositions. Assess useful EC coverage; add only with a recorded scope decision. | Review | — |
| PAGE-page-search | `page-search` (not exposed) | `E/page-search/page-search.html.twig` | Official page example is reference material for the starter/compositions. Assess useful EC coverage; add only with a recorded scope decision. | Review | — |

## Server, package and supporting files

These files affect delivery, packaging and maintainability rather than defining an upstream EC component. The MCP package/server version 1.0.0 is independent of the ECL content version.

| ID | Local item / lookup | Target reference | Finding / next action | Status | Verified version / date / evidence |
| --- | --- | --- | --- | --- | --- |
| SUPPORT-runtime | [index.js](index.js) | Local MCP contract | Reads content from disk per call; exact template-family discovery now includes file/gallery and the previously delivered high-drift families. | Verified | v5.3.1 / 2026-09-25 / S005; node --check, fresh connected MCP client and component/template disk comparison |
| SUPPORT-package | [package.json](package.json) | Local package metadata and scripts | Review delivered file set and release/version documentation; scripts declare Jest/ESLint but no project tests or lint config were found. Do not claim a test suite passed without tests. | Review | — |
| SUPPORT-lockfile | [package-lock.json](package-lock.json) | Local dependency lock | Change only when required by package work; keep dependency reproducibility. | Review | — |
| SUPPORT-readme | [README.md](README.md) | Local setup; `D/getting-started/` | Document EC target, update workflow, available tools and how content/runtime changes reach the MCP. | Review | — |
| SUPPORT-ignore | [.gitignore](.gitignore) | Local packaging/checkout rules | Upstream symlink is ignored; confirm package contains intended EC content and excludes development-only files. | Review | — |
| SUPPORT-recipes-db | [components/recipes.db](components/recipes.db) | No reference from `index.js` | SQLite file is present but not exposed by any tool. Determine intended purpose/provenance before changing or removing it. | Review | — |
| SUPPORT-asset-provenance | [docs/ecl-v5.3.1-assets.json](docs/ecl-v5.3.1-assets.json) | Official EC v5.3.1 release archive and pinned source | Records archive SHA-256, upstream/local hashes for 18 files, flattened paths, font version and source-map transformations. All hashes and embedded sources checked; guide exposes path and package dry run includes it. | Verified | v5.3.1 / 2026-09-25 / S002 |
| SUPPORT-old-tracker | `component-update.md` (already deleted in working tree) | Historical `git show HEAD:component-update.md` | Pre-existing user deletion preserved. Historical v5.0.1 evidence is available in Git; this new tracker governs this update cycle. | Excluded | — |

## Next recommended batch

**Batch 13: remaining high-drift content families.**
S004 delivered the high-drift search/story/card/slider families, S005 delivered
file/gallery and the responsive follow-up, S006 delivered the media, picture,
link and text-media/video families, S007 delivered table/news-ticker and their
shared runtime hooks, S008 delivered the accordion family, S009 delivered
description-list with its link/tag dependencies, and S010 delivered
fact-figures with its source and link contracts, and S011 delivered the
form-group, search-form and page-summary families, and S012 verified the
remaining checkbox, datepicker, file-upload, radio, select, text-area and
text-input families with their exact shared Twig helpers, and S013 delivered
range/rating-field plus the file-upload-status helper. Next, take the remaining
high-drift quiz, slogan-ticker, social-media-follow and splash-page families in
a coherent content batch. Keep standalone mega-menu, Menu and page-header rows
in Review unless the rendered-example audit is the priority.
Keep the existing component IDs and use the tagged v5.3.1 source; do not rebuild
the assets or repeat the full inventory.
Revisit `GUIDE-assets`/`GUIDE-icons` WebTools rendering when the external loader
is reachable; the S002/S003 environment limitation does not prevent source work.

Suggested following order after Batch 12 (adjust for dependencies and user focus):

1. Remaining high-drift quiz, slogan-ticker, social-media-follow and splash-page
   families, including their changed Twig sources and paired HTML behavior.
2. Remaining navigation, forms, content/media and simple components in small
   coherent batches, including unchanged-source items.
3. Focused utility/design guides and coverage gaps; reconcile cross-links and
   package/README documentation as their dependencies settle.
4. Final EC-wide delivery, dependency, accessibility and browser checks. Resolve
   every pending row or record an explicit justified exclusion before closing
   the cycle.

No later session should redo the complete inventory as its default task. Read
the latest session entry, select the next batch, and continue the standing rows.

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
