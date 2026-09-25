# Reusable ECL EC update prompt

Paste the prompt below into a new session in this repository, or ask the agent to
read this file and carry it out. Optionally specify tracker IDs or a component at
the end. `update-status.md` is the standing record; update it in place after every
session.

---

Continue the incremental update of this ECL MCP server for the **European
Commission (EC)**. Its purpose is to give developers and AI agents dependable,
accessible examples and guidance that follow the official Europa Component
Library. Focus on EC throughout, including branding, assets, examples and
documentation.

Read `AGENTS.md` instructions that apply, `README.md`, `index.js`, and
`update-status.md` before editing. Respect existing user changes. Work sequentially
with one agent; this is a calm, iterative process across sessions, not a request
to update the entire library in one pass.

## Establish the baseline

1. Read the target release, pinned upstream commit, latest session entry, next
   recommended batch, and unresolved findings in `update-status.md`.
2. Inspect this repository's Git status and the `europa-component-library` symlink
   and its target's Git status. The symlink points to a separate upstream Git
   repository. Do not overwrite its local changes or assume its development
   branch is the published release.
3. Check the official EC site at
   <https://ec.europa.eu/component-library/ec/> and the release notes. Record any
   newer release, but keep the tracker’s pinned target for this cycle unless the
   user asks to change it. Never silently mix releases or reset completed rows.
   When an upstream refresh is needed and its checkout is clean, use
   `git -C europa-component-library pull --ff-only`; record before/after commits.
   If a pull cannot fast-forward, record the issue without resetting or rebasing
   the user's checkout.
4. Read reference files at the pinned release using
   `git -C europa-component-library show <tag>:<path>`. For building or rendering,
   use a separate temporary checkout of that release if needed. Do not build the
   moving `v5-dev` branch and label its output as the pinned release. A pre-existing
   upstream `dist/` or `node_modules/` may be stale after a pull.

## Choose and complete a manageable batch

Follow the user's selected rows if supplied. Otherwise take the next recommended
batch from `update-status.md`, respecting shared-asset and component dependencies.
Prefer one component family or a small group of related guides. State the selected
IDs and intended result briefly, then proceed without asking about routine
implementation choices. Mark selected rows `In progress`.

For each selected item:

- Compare the MCP's actual output and local files with **both** the official EC
  usage/accessibility/API documentation and the pinned upstream source. Use
  source paths, demo data, stories and EC test snapshots as evidence. When the
  live documentation has advanced beyond the pinned release, use its versioned
  source at the pinned commit and record the difference.
- Read the upstream changelog between the previous baseline and target release.
  Follow relevant markup, API, JavaScript, accessibility and dependency changes;
  a matching Twig file alone does not prove an HTML example is current.
- Update the HTML example and its complete Twig family together, including
  helper templates and required dependencies. Preserve useful example coverage,
  use official EC conventions, and explain intentional local adaptations in the
  tracker. Do not merely change version labels or copy development snapshots.
- Check semantics, valid nesting, unique IDs, ARIA relationships, labels,
  keyboard behavior, responsive behavior and exact `data-ecl-*` initialization
  hooks. Use matching EC CSS/JS and `ECL.autoInit()` where required. Keep examples
  reusable; avoid accidental dependencies on the documentation website.
- Update affected guides, cross-references and the starter page when a shared
  contract changes. Include newly introduced EC components or helpers and any
  required assets. Add tracker rows for newly discovered work before it is lost.
- Keep CSS, JavaScript, source maps, fonts and branding assets from a consistent,
  traceable release/build. Record provenance and any local transformations.
  Preserve working asset paths and verify all referenced files. Treat fonts'
  own version separately from the ECL version.
- Resolve retired files and accidental EU exposure deliberately, checking users
  of the existing MCP IDs before changing the tool contract. The tracker contains
  legacy files for completeness; it is not an instruction to expand EU support.

## Verify the result through the MCP

This checkout supplies the connected ECL MCP server. Changes to content files
should be visible on subsequent tool calls because `index.js` reads them on each
request. Changes to JavaScript registration/handlers require a server restart or
client reconnect; do not mistake a running old process for the edited code.

1. Call the relevant connected tools (`guide_list`, `guide`, `components_list`,
   `component`, `component_template`, `starter_template`) after editing. Compare
   returned content with the files on disk, including `__DIR__` substitution for
   guide responses. Check list discoverability and every affected template key.
2. Verify shared dependencies and exercise interactive components in a browser
   when behavior or rendered markup changed. Use a representative EC page, check
   console errors and missing requests, and record what was actually tested.
3. Run focused checks appropriate to the changes. Inspect `package.json` and the
   available configuration first: this server is Node.js, and script names alone
   do not prove a working test suite exists. If Laravel code ever changes, follow
   the personal requirement to run focused tests and
   `php artisan test --parallel`, unless explicitly skipped or blocked.
4. If the connected MCP is unavailable or serving a different checkout, report
   it accurately. A fresh local stdio client is useful additional evidence, but
   does not prove that the user's existing connection has refreshed. Leave live
   verification pending where necessary.

## Maintain the standing record

- Preserve stable row IDs and previous session history in `update-status.md`.
- For each worked row record status, target version, date, reference paths/URLs,
  changes or the reason no change was required, and verification evidence.
- `Verified` means the item is correct for the pinned target and the applicable
  checks, including live MCP delivery, passed. `Updated` means edits are complete
  but verification remains. `Review` means inventoried but not yet reviewed for
  the target. Do not equate a successful tool call with ECL conformance.
- Use `Needs update`, `Missing`, `Blocked`, `In progress` and `Excluded` according
  to the tracker legend. Record a concrete reason and next action for blockers
  or exclusions. Do not count excluded work as EC content updated.
- Update summary counts and append a session entry listing rows worked,
  validation, unresolved issues and the next recommended batch. If a newer
  release appears, preserve version-specific evidence and record the proposed
  next cycle separately.
- Finish with a concise report of what changed, what was verified, anything
  unfinished, and which rows to do next. Do not commit, push or publish unless
  requested. Leave the repository and tracker ready for the next session.

Optional focus for this session: **[tracker IDs, component family, or “next
recommended batch”]**.
