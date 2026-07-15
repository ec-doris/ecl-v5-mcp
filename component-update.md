# ECL/EC component update tracker

This file is the durable checkpoint for updating the MCP component examples against the Europa Component Library (ECL) EC preset. Update it **before and after** changing a component so work can resume safely after an interruption.

## Baseline

- ECL source: `./europa-component-library` (symbolic link; do not copy it into this project)
- ECL source ref: tag `v5.0.1`
- ECL commit: `eceefe9468e44f7ce9c57801c91c4c0c057548b4`
- Compiled asset release: `v5.0.1`
- Inventory source: the 69 direct component packages in `europa-component-library/src/components/`, all of which are consumed by the EC preset
- Last tracker update: 2026-07-15

The linked checkout may remain on another branch. Read versioned source with `git -C europa-component-library show v5.0.1:<path>` and do not switch or modify the user's linked checkout. Change the source ref and commit above only when this project deliberately upgrades its compiled assets to the same release.

## Resume checkpoint

- Current component: none
- Status: ready
- Phase: none
- Last completed: `notification`
- Next component: `ordered-list`
- Next action: change `ordered-list` to `started` here before auditing its tagged v5.0.1 source or editing its files
- Evidence and warnings: Notification completed 2026-07-15. Preflight passed: `europa-component-library` is a symlink, tag `v5.0.1` resolves to `eceefe9468e44f7ce9c57801c91c4c0c057548b4`, outer and linked worktrees reported no short-status entries, and the tagged package contains README, package metadata, one component-owned Twig template, SCSS, print SCSS, JavaScript, four demo data files, story, tests, snapshots, and EC website docs. Audit found tagged Twig imports `icon`, `link`, and `button`; local dependency output can represent the v5.0.1 icon/link/button branches used by notification, and compiled assets contain the `Notification` auto-init, root hook, and close hook. Twig sync passed for `components/notification.html.twig`. Reusable HTML covers info, success, warning, error, empty variant/root-class branch, default and custom icons, `sr_icon` present/absent, title present/absent, description present/absent, no links, one link, multiple links, close present/absent, extra class, valued and valueless attributes, empty input/root-only output, runtime hooks, omission of authored `data-ecl-auto-initialized`, and all 15 non-default EC color modes. Runtime constructor options `closeSelector` and `attachClickListener`, event callbacks, and runtime-authored state are intentionally excluded from static HTML. Validation passed: Twig identity, no-Twig HTML, Prettier check, structural/IDREF check, color-mode set check, package dry-run inclusion using `npm pack --dry-run --json`, focused selector/hook checks, Jest smoke with `--passWithNoTests`, JS syntax check, and `git diff --check`. The npm pack `.gitignore` fallback warning and Jest no-tests result are expected. Laravel full-suite testing was not applicable because this repository has no `composer.json` or `artisan`.

On restart, resume any row marked `started` before choosing a `not started` row. If a row is `blocked`, do not skip it and start another component; read its evidence and obtain the recorded decision first.

## Inventory row and checkpoint status values

- `not started`: no component-file work or active checkpoint has begun; prepared read-only handoff notes may exist.
- `started`: work is in progress; read the row notes and resume checkpoint before editing.
- `completed`: Twig is synchronized, HTML configuration coverage is complete, and validation passed.
- `blocked`: work cannot continue; the row notes must explain why and give the exact next action.

Inventory rows use the four values above. The resume checkpoint's `Status` uses exactly `ready`, `started`, or `blocked`: `ready` requires `Current component: none`; `started` or `blocked` requires the active component in both `Current component` and `Next component`.

## Non-negotiable handoff rules

These rules are intentionally explicit so a new agent can continue without reconstructing earlier decisions.

1. Work on exactly one inventory row at a time. Do not edit another component, its tracker status, assets, `package.json`, `index.js`, or guides during a component pass unless the user explicitly expands the scope.
2. Before any component-file edit, change that row to `started` and persist the resume checkpoint. Do not create a missing HTML or Twig file first.
3. Treat tag `v5.0.1` as the only source of truth. The linked checkout is currently allowed to be on `v5-dev`; never copy from its working tree or from `HEAD`.
4. Never run `checkout`, `switch`, `pull`, `reset`, `clean`, install, or build inside `europa-component-library`. It is a read-only symlink to the user's separate repository.
5. Inspect both Git statuses before editing. Preserve every unrelated or pre-existing change and do not commit; the user handles commits.
6. Use `apply_patch` for project edits. A tagged upstream file may be written to `/tmp` for comparison, but not redirected directly into this project.
7. Keep component-owned Twig byte-for-byte identical to the tag. Never run Prettier on Twig. Format only the reusable HTML and this Markdown tracker.
8. Do not silently repair an upstream defect. Preserve exact Twig, omit a misleading or invalid static example if necessary, and record the evidence and exclusion.
9. Do not silently update imported components. A Twig file owned by another package is a separate inventory row. Audit the pinned v5.0.1 dependency output used by the current component; if the existing local dependency cannot render it correctly, stop and record the required scope decision.
10. Do not infer completion from `npm test`. This repository currently has no Jest tests. The command is only a smoke check. `npm run lint` is not a gate because the repository currently has no ESLint configuration; do not create one as part of a component update.

## Checkpoint state machine

Use these four phases, in this order: `upstream audit` -> `Twig sync` -> `HTML examples` -> `validation`.

When starting or resuming work, the checkpoint must identify the active row in both `Current component` and `Next component`. Keep `Last completed` unchanged until every validation gate passes. A useful active checkpoint looks like this:

```md
- Current component: `animated-numbers`
- Status: started
- Phase: Twig sync
- Last completed: `add-to-calendar`
- Next component: `animated-numbers`
- Next action: apply the tagged Twig with `apply_patch`, then run the exact `cmp` command
- Evidence and warnings: baseline commit verified; upstream inventory audited; linked checkout is on v5-dev, so use tag objects only
```

Update `Phase`, `Next action`, and `Evidence and warnings` after each phase **before** beginning the next one. If a command fails or work stops, leave the row `started` (or `blocked` when a decision is required) and record the exact failing command, output summary, and safest next action.

Only after all gates pass:

- change the row to `completed` and update missing file columns to their real paths;
- set `Current component` to `none` and `Status` to ready;
- move `Last completed` to the finished component;
- move `Next component` to the next inventory row and name its first action;
- verify that no row remains `started`.

## Component update procedure

### 1. Preflight and durable start

Select the existing `started` row, or the first `not started` row when none is active. Substitute that slug for `COMPONENT`, run this block, and review both status outputs:

```bash
set -euo pipefail
ECL_REF=v5.0.1
ECL_COMMIT=eceefe9468e44f7ce9c57801c91c4c0c057548b4
COMPONENT=animated-numbers

test -L europa-component-library
test "$(git -C europa-component-library rev-parse "${ECL_REF}^{commit}")" = "$ECL_COMMIT"
git status --short
git -C europa-component-library status --short
git -C europa-component-library ls-tree -r --name-only "$ECL_REF" -- \
  "src/components/$COMPONENT" \
  "src/website/src/pages/ec/components/$COMPONENT"
```

If the tag resolves to another commit, stop. A dirty outer project or linked checkout is not automatically a blocker, but record it and avoid those changes. Before touching component files, set the row to `started`, checkpoint `Status` to `started`, and checkpoint `Phase` to `upstream audit`.

### 2. Audit tagged source, not the linked branch

First inventory all existing paths with `ls-tree`; do not assume every component has the same files. Read each relevant file through `git -C europa-component-library show "v5.0.1:<path>"`. The mandatory audit is:

- every component-owned Twig template and partial;
- README and `package.json`;
- JavaScript runtime, SCSS, and print SCSS;
- story, all `prepareData` transformations, and demo data;
- tests and every matching snapshot export;
- EC website API, code, usage, and accessibility pages when present;
- imported Twig components, only far enough to confirm the pinned v5.0.1 dependency output used by this component can be rendered accurately with the local version;
- the matching selectors, modifiers, hooks, and auto-init name in this project's pinned compiled CSS and both JavaScript bundles.

Use this evidence priority when sources disagree:

1. Tagged Twig plus its tests/snapshots define the rendered markup contract.
2. Tagged JavaScript and SCSS define runtime and styling requirements.
3. Tagged story `prepareData` plus demo data define supported example inputs.
4. Tagged EC docs and README explain intent.

Do not treat a raw Storybook control as component API until `prepareData` has been traced. Compare the tag with the linked branch only to identify future-version traps; never use newer code to fill a v5.0.1 gap.

Before authoring HTML, put a coverage ledger in the active handoff/checkpoint. For every Twig option, optional field, modifier, layout, state, count-dependent branch, source/content shape, runtime hook, extension hook, and EC color mode, record:

- its default and whether it changes markup;
- the named example that covers both relevant branches;
- interacting combinations that need their own example;
- intentionally excluded inputs and the tagged evidence for excluding them.

Independent options may share an example. Do not generate a Cartesian product when the resulting markup shape is identical. This project treats the default mode plus all 15 classes in `assets/ecl-ec-color-modes.css` as reusable EC configurations; cover each non-default mode once, but do not combine every mode with every component variant.

### 3. Synchronize component-owned Twig

Use `apply_patch` to create or replace every component-owned Twig file listed by the tagged package and the inventory row. Compare each one against the tag; a successful `cmp` emits no output:

```bash
set -euo pipefail
ECL_REF=v5.0.1
COMPONENT=animated-numbers # Replace with the active slug.
LOCAL_TWIG=(components/animated-numbers.html.twig) # Use every Twig path from the row.
UPSTREAM_TWIG=(src/components/animated-numbers/animated-numbers.html.twig)

test "${#LOCAL_TWIG[@]}" -eq "${#UPSTREAM_TWIG[@]}"
for index in "${!LOCAL_TWIG[@]}"; do
  test -f "${LOCAL_TWIG[$index]}"
  cmp -s "${LOCAL_TWIG[$index]}" \
    <(git -C europa-component-library show \
      "$ECL_REF:${UPSTREAM_TWIG[$index]}")
done
```

The local and upstream arrays are an explicit one-to-one mapping; do not synthesize names from the component slug. Include every component-owned partial. Do not copy or update cross-component imports here. A no-Twig component such as `tooltip` uses two empty arrays only because that exception is documented in its row.

### 4. Author the reusable HTML examples

Create or update `components/<component>.html` as directly reusable, fully rendered HTML. It must contain no Twig and must cover the completed coverage ledger:

- render every distinct supported markup shape, including both branches of markup-affecting booleans and meaningful optional fields;
- preserve required component classes, JavaScript hooks, auto-init values, ARIA, no-JavaScript content, and unique IDs exactly as the tag produces them;
- include valued and valueless extension attributes and extra classes when the Twig exposes those hooks;
- use headings or short comments to name examples;
- use snapshots as output oracles, but never copy Jest wrappers, backticks, or snapshot-only self-closing non-void HTML;
- do not author runtime-generated state such as `data-ecl-auto-initialized`;
- do not invent HTML attributes for constructor-only JavaScript options.

### 5. Validation gates

Run all generic gates plus the active component's focused checks. Any failure keeps the row `started`.

Twig identity, no-Twig static HTML, and formatting:

```bash
set -euo pipefail
ECL_REF=v5.0.1
COMPONENT=animated-numbers # Replace with the active slug.
LOCAL_TWIG=(components/animated-numbers.html.twig) # Use every Twig path from the row.
UPSTREAM_TWIG=(src/components/animated-numbers/animated-numbers.html.twig)

test "${#LOCAL_TWIG[@]}" -eq "${#UPSTREAM_TWIG[@]}"
for index in "${!LOCAL_TWIG[@]}"; do
  test -f "${LOCAL_TWIG[$index]}"
  cmp -s "${LOCAL_TWIG[$index]}" \
    <(git -C europa-component-library show \
      "$ECL_REF:${UPSTREAM_TWIG[$index]}")
done

if rg -n '\{\{|\{%|\{#' "components/$COMPONENT.html"; then exit 1; fi
npx --no-install prettier --check "components/$COMPONENT.html" component-update.md
```

Never add Twig to the Prettier command. The array loop must compare every component-owned Twig file.

Use this structural balance, duplicate-ID, and standard ID-reference check. It does not understand component-specific `data-*` targets, so check those separately against tagged JavaScript and tests.

```bash
set -euo pipefail
COMPONENT=animated-numbers # Replace with the active slug.
export COMPONENT
node --input-type=module <<'NODE'
import { readFileSync } from 'node:fs';

const file = `components/${process.env.COMPONENT}.html`;
let html = readFileSync(file, 'utf8')
  .replace(/<!--[\s\S]*?-->/g, '')
  .replace(/<(script|style)\b[^>]*>[\s\S]*?<\/\1\s*>/gi, '');
const voids = new Set([
  'area',
  'base',
  'br',
  'col',
  'embed',
  'hr',
  'img',
  'input',
  'link',
  'meta',
  'param',
  'source',
  'track',
  'wbr',
]);
const stack = [];
for (const match of html.matchAll(/<\/?([A-Za-z][\w:-]*)\b[^>]*>/g)) {
  const token = match[0];
  const tag = match[1].toLowerCase();
  if (token.startsWith('</')) {
    const open = stack.pop();
    if (open !== tag) {
      throw new Error(
        `${file}: closing </${tag}> while <${open ?? 'nothing'}> was open`,
      );
    }
  } else if (!voids.has(tag) && !/\/\s*>$/.test(token)) {
    stack.push(tag);
  }
}
if (stack.length) throw new Error(`${file}: unclosed: ${stack.join(', ')}`);

const ids = [...html.matchAll(/\bid\s*=\s*(["'])(.*?)\1/gs)].map(
  (match) => match[2],
);
const duplicates = ids.filter((id, index) => ids.indexOf(id) !== index);
if (duplicates.length) {
  throw new Error(
    `${file}: duplicate ids: ${[...new Set(duplicates)].join(', ')}`,
  );
}
const known = new Set(ids);
const references =
  /(?:^|\s)(aria-activedescendant|aria-controls|aria-describedby|aria-details|aria-errormessage|aria-flowto|aria-labelledby|aria-owns|for|form|headers|list)\s*=\s*(["'])(.*?)\2/gs;
for (const match of html.matchAll(references)) {
  for (const id of match[3].trim().split(/\s+/).filter(Boolean)) {
    if (!known.has(id)) {
      throw new Error(`${file}: ${match[1]} references missing id "${id}"`);
    }
  }
}
console.log(`${file}: balanced; IDs and standard IDREFs valid`);
NODE
```

Verify all 15 non-default EC modes are present exactly as a set:

```bash
set -euo pipefail
COMPONENT=animated-numbers # Replace with the active slug.

diff -u \
  <(rg -o 'ecl-color-mode--[a-z-]+' assets/ecl-ec-color-modes.css | sort -u) \
  <(rg -o 'ecl-color-mode--[a-z-]+' "components/$COMPONENT.html" | sort -u)
```

Verify the files will actually ship while the large linked ECL repository will not:

```bash
set -euo pipefail
COMPONENT=animated-numbers # Replace with the active slug.
LOCAL_TWIG=(components/animated-numbers.html.twig) # Use every Twig path from the row.
FILES=("components/$COMPONENT.html" component-update.md "${LOCAL_TWIG[@]}")
npm pack --dry-run --json > /tmp/ecl-v5-mcp-pack.json
node --input-type=module - "${FILES[@]}" <<'NODE'
import { readFileSync } from 'node:fs';

const [{ files }] = JSON.parse(
  readFileSync('/tmp/ecl-v5-mcp-pack.json', 'utf8'),
);
const paths = files.map(({ path }) => path);
const packed = new Set(paths);
const missing = process.argv.slice(2).filter((path) => !packed.has(path));
if (missing.length) {
  throw new Error(`Missing from npm package: ${missing.join(', ')}`);
}
if (
  paths.some(
    (path) =>
      path === 'europa-component-library' ||
      path.startsWith('europa-component-library/'),
  )
) {
  throw new Error('The linked ECL repository would be included in the package');
}
NODE
```

Keep the package check's `LOCAL_TWIG` array identical to the validated local array above.

An npm warning that `.npmignore` is absent is expected; do not add one merely to suppress that warning. Finish with:

```bash
set -euo pipefail
COMPONENT=animated-numbers # Replace with the active slug.
LOCAL_TWIG=(components/animated-numbers.html.twig) # Keep identical to the validated array.
SCOPED_FILES=("components/$COMPONENT.html" component-update.md "${LOCAL_TWIG[@]}")

if rg -n '[[:blank:]]+$' \
  "components/$COMPONENT.html" \
  component-update.md; then exit 1; fi
npm test -- --runInBand --passWithNoTests
node --check assets/ecl-ec.js
node --check assets/ecl-esm-ec.js
git diff --check -- "components/$COMPONENT.html" component-update.md
git status --short -- "${SCOPED_FILES[@]}"
git diff --stat -- "${SCOPED_FILES[@]}"
git status --short
```

The whitespace diff check is deliberately scoped to authored HTML and the tracker; exact Twig is governed by `cmp` because upstream files may themselves contain trailing spaces. Git diff commands also ignore untracked files, which is why the explicit authored-file whitespace, Prettier, Twig identity, package, scoped status, and full `git status` checks are mandatory. Review the final scoped diff and every new file, and confirm only the active component plus this tracker changed during the pass.

### Stop instead of guessing when

- the pinned tag does not resolve to the recorded commit;
- tagged Twig, runtime, tests/snapshots, and story transformations contradict one another in a way that changes the recommended markup;
- a required selector or hook is missing from the pinned v5.0.1 assets;
- a supported branch cannot be rendered confidently from tagged evidence;
- accurate output requires changing another component's Twig or status;
- any validation gate fails and cannot be corrected within the active component.

Leave the active row `started` for a mechanical failure or mark it `blocked` for a user decision. Record concrete evidence and the exact next command or decision; never mark a row completed with unresolved TODOs.

## Next component handoff: `animated-numbers`

This is a prepared implementation brief, not a completed audit checkpoint. The row must still be changed to `started` before either missing file is created.

### Pinned facts and version fence

- Component-owned source inventory at `v5.0.1`: `.npmignore`, `README.md`, `animated-numbers.html.twig`, `animated-numbers.js`, `animated-numbers.scss`, `animated-numbers-print.scss`, `animated-numbers.story.js`, `animated-numbers.test.js`, `__snapshots__/animated-numbers.test.js.snap`, `demo/data.js`, and `package.json`.
- EC website inventory: `src/website/src/pages/ec/components/animated-numbers/` contains `docs/accessibility.md`, `docs/api.mdx`, `docs/code.mdx`, `docs/usage.md`, `ec_comp_animated_numbers.svg`, and `index.md`.
- Tagged Twig SHA-256: `2c38456d403cc971c2476861876c2dd90b0702bfbbef447e92ffd4778a7b3154`.
- Tagged Jest snapshot SHA-256: `05ea1dbb95f562bbeab6efe0611cea72232cedb4ca43eabc2294b818562682da`.
- The only component-owned Twig file is `animated-numbers.html.twig`. It imports `icon` and `link`; do not change or mark those separate rows completed. The local icon body is compatible. The local link supports the `inverted` branch used here, despite unrelated v5 drift.
- The linked `v5-dev` version is not release-compatible: it adds per-item sources, a Twig macro, branded source links, and nested source styling that are absent from v5.0.1 assets. At this baseline, sources are **global only**. Do not copy per-item `sources`, per-item `sources_label`, the macro, or branded source output.
- Manual JavaScript options such as `animationStyle`, `animationDuration`, and `animateOnVisible` do not create HTML configurations or data attributes.

Reproduce and verify the Twig digest with:

```bash
set -euo pipefail

git -C europa-component-library show \
  v5.0.1:src/components/animated-numbers/animated-numbers.html.twig \
  > /tmp/animated-numbers-v5.0.1.html.twig
printf '%s  %s\n' \
  2c38456d403cc971c2476861876c2dd90b0702bfbbef447e92ffd4778a7b3154 \
  /tmp/animated-numbers-v5.0.1.html.twig | shasum -a 256 -c -
```

The redirection is allowed only because the destination is `/tmp`. Create the project Twig with `apply_patch`, then compare it with that file.

### Required configuration ledger

Use a small number of named examples to cover all of these without a Cartesian product:

- [ ] Default multi-item component with counter color enabled. Across its items, cover category present/absent; icon absent; decorative icon; titled/accessible icon; prefix and suffix present/absent; prefix and suffix screen-reader labels present/absent; integer and decimal numeric values; description present/absent.
- [ ] Multiple global sources mixing a link and plain name, with `sources_label`. This covers the `ul`/`li` source shape.
- [ ] Minimal one-item component with `counter_color: false`, only a numeric value and no other item fields, a single plain source with no label, an extra class, a valued attribute, and a valueless attribute.
- [ ] An item with category/description but no value, so the optional value branch is genuinely covered rather than assumed from an absent items list.
- [ ] Border alone.
- [ ] Background alone. It must add `--with-background`, suppress `--counter-color`, omit primary icon color, and render a single source link as inverted.
- [ ] Background plus border, because their styling interaction differs from either option alone.
- [ ] Full width in the intended story form with both `full_width` and `with_background` true. Place it inside an outer `.ecl-container`; it must add an inner `.ecl-container`. Use items without sources, or correctly use inverted links.
- [ ] Items with no sources, sources with no items, and the tagged empty-input/root-only output. Label the latter as an edge-case contract example, not a recommended content configuration.
- [ ] No sources, one plain source, one linked source, and multiple mixed sources; source label both present and absent.
- [ ] One and multiple items. Story counts from one through eight only repeat the same `li` shape, so eight separate count examples are not required.
- [ ] Default mode plus all 15 non-default `ecl-color-mode--*` classes from `assets/ecl-ec-color-modes.css`, applied as compact one-item root examples. These are global EC classes passed through `extra_classes`, not an Animated numbers Twig parameter.
- [ ] Every root has `data-ecl-animated-numbers` and `data-ecl-auto-init="AnimatedNumbers"`; every rendered value has `data-ecl-animated-numbers-value`.

Interaction rules that must be visible in the output:

- `with_background` **or** `full_width` adds `ecl-animated-numbers--with-background` and forcibly disables `ecl-animated-numbers--counter-color`.
- `full_width` also adds `ecl-animated-numbers--full-width` and the inner `.ecl-container`.
- `border` adds `ecl-animated-numbers--border`; default `counter_color: true` adds `ecl-animated-numbers--counter-color`.
- Icon size is always `xl`. Primary icon color appears only when counter color remains enabled.
- A single source renders a link or span directly. Multiple sources render a list. Source links are inverted only when the actual `with_background` input is true.
- In v5.0.1, `full_width: true` alone visually implies background but computes link inversion from `with_background`. The story normalizes full width by setting both flags. Do not recommend a full-width-only linked-source example with a non-inverted link; document that tagged upstream inconsistency instead.

Runtime and accessibility rules:

- Put the final numeric text in initial HTML for no-JavaScript fallback. Put currency and units in prefix/suffix; the runtime parses the value by stripping everything except digits, dot, and minus.
- Prefix/suffix labels are screen-reader-only text for ambiguous symbols or abbreviations. Do not invent `aria-live`, IDs, or ARIA relationships absent from tagged Twig.
- Do not author `data-ecl-auto-initialized`; JavaScript adds it at runtime.
- The v5.0.1 runtime has no reduced-motion handling. Record that fact if useful, but do not invent markup or claim the example solves it.
- Tagged snapshots cover default, background, full width, border, extra class, and extra attributes. The local ledger must additionally cover the optional content and source branches above.

Focused Animated numbers checks:

```bash
set -euo pipefail

test "$(shasum -a 256 components/animated-numbers.html.twig | awk '{print $1}')" = \
  2c38456d403cc971c2476861876c2dd90b0702bfbbef447e92ffd4778a7b3154

for token in \
  ecl-animated-numbers--with-background \
  ecl-animated-numbers--full-width \
  ecl-animated-numbers--border \
  ecl-animated-numbers--counter-color; do
  rg -Fq "$token" components/animated-numbers.html
  rg -Fq "$token" assets/ecl-ec.css
done

for token in \
  data-ecl-animated-numbers-value \
  AnimatedNumbers; do
  rg -Fq "$token" components/animated-numbers.html
  rg -Fq "$token" assets/ecl-ec.js
  rg -Fq "$token" assets/ecl-esm-ec.js
done

node --input-type=module <<'NODE'
import { readFileSync } from 'node:fs';

const file = 'components/animated-numbers.html';
const html = readFileSync(file, 'utf8').replace(/<!--[\s\S]*?-->/g, '');
const tags = [...html.matchAll(/<[A-Za-z][\w:-]*\b[^>]*>/g)].map(
  (match) => match[0],
);
const attribute = (tag, name) => {
  const match = tag.match(
    new RegExp(`\\s${name}\\s*=\\s*(["'])(.*?)\\1`, 's'),
  );
  return match?.[2];
};
const hasAttribute = (tag, name) =>
  new RegExp(`\\s${name}(?=\\s|=|>)`).test(tag);
const classes = (tag) =>
  new Set((attribute(tag, 'class') ?? '').trim().split(/\s+/).filter(Boolean));

const roots = tags.filter((tag) => classes(tag).has('ecl-animated-numbers'));
if (!roots.length) throw new Error(`${file}: no Animated numbers roots found`);
for (const root of roots) {
  if (!/^<div\b/i.test(root)) throw new Error(`${file}: root is not a div`);
  if (!hasAttribute(root, 'data-ecl-animated-numbers')) {
    throw new Error(`${file}: root lacks data-ecl-animated-numbers`);
  }
  if (attribute(root, 'data-ecl-auto-init') !== 'AnimatedNumbers') {
    throw new Error(`${file}: root lacks the exact AnimatedNumbers auto-init`);
  }
}
const rootHooks = tags.filter((tag) =>
  hasAttribute(tag, 'data-ecl-animated-numbers'),
);
const autoInitHooks = tags.filter(
  (tag) => attribute(tag, 'data-ecl-auto-init') === 'AnimatedNumbers',
);
if (rootHooks.length !== roots.length || autoInitHooks.length !== roots.length) {
  throw new Error(`${file}: root hooks appear outside a component root`);
}

const values = tags.filter((tag) =>
  classes(tag).has('ecl-animated-number__value'),
);
if (!values.length) throw new Error(`${file}: no rendered values found`);
for (const value of values) {
  if (!/^<span\b/i.test(value)) throw new Error(`${file}: value is not a span`);
  if (!hasAttribute(value, 'data-ecl-animated-numbers-value')) {
    throw new Error(`${file}: value lacks its animation hook`);
  }
}
const valueHooks = tags.filter((tag) =>
  hasAttribute(tag, 'data-ecl-animated-numbers-value'),
);
if (valueHooks.length !== values.length) {
  throw new Error(`${file}: value hooks appear outside a value span`);
}
console.log(
  `${file}: ${roots.length} roots and ${values.length} values have exact hooks`,
);
NODE

if rg -P \
  'class="(?=[^"]*ecl-animated-numbers--with-background)(?=[^"]*ecl-animated-numbers--counter-color)' \
  components/animated-numbers.html; then exit 1; fi
```

At successful completion the tracker should say: `Current component: none`, `Last completed: animated-numbers`, `Next component: banner`; both Animated numbers file columns must contain their paths, its row must be `completed`, and no row may remain `started`.

## Component inventory

| Component           | HTML example                          | Twig template(s)                                                                                                            | Status        | Notes                                                                                                                                                                                                                                       |
| ------------------- | ------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| accordion           | `components/accordion.html`           | `components/accordion.html.twig`                                                                                            | **completed** | Completed 2026-07-14 against v5.0.1. Twig is exact; HTML covers native/open, named, sidebar, single-icon, structured content, extension hooks and all 15 non-default color modes.                                                           |
| add-to-calendar     | `components/add-to-calendar.html`     | `components/add-to-calendar.html.twig`                                                                                      | **completed** | Completed 2026-07-14 against v5.0.1. Twig is exact; HTML covers default, title-only, single-meta, action-only, full-width, extension hooks, live WebTools embeds and all 15 modes. Empty input is excluded due to an upstream markup bug.   |
| animated-numbers    | `components/animated-numbers.html`    | `components/animated-numbers.html.twig`                                                                                     | **completed** | Completed 2026-07-14 against v5.0.1. Twig is exact; HTML covers content/source branches, modifiers and interactions, hooks, edge output, accessibility icon states, and all 15 non-default color modes.                                     |
| banner              | `components/banner.html`              | `components/banner.html.twig`                                                                                               | **completed** | Completed 2026-07-14 against v5.0.1. Twig is exact; HTML covers image, video, no-media, content/link branches, modifiers, hooks, extension attributes, and all 15 modes.                                                                    |
| blockquote          | `components/blockquote.html`          | `components/blockquote.html.twig`                                                                                           | **completed** | Completed 2026-07-14 against v5.0.1. Twig is exact; HTML covers quote, language, picture, extension hooks, tagged empty output, and all 15 non-default color modes.                                                                         |
| breadcrumb          | `components/breadcrumb.html`          | `components/breadcrumb.html.twig`                                                                                           | **completed** | Completed 2026-07-14 against v5.0.1. Twig is exact; HTML covers static, edge, auto-init, ellipsis, item split, extension hooks, custom range/text options, and all 15 modes.                                                                |
| button              | `components/button.html`              | `components/button.html.twig`                                                                                               | **completed** | Updated for v5.0.1; Twig matches upstream and all supported variants are represented.                                                                                                                                                       |
| card                | `components/card.html`                | `components/card.html.twig`                                                                                                 | **completed** | Completed 2026-07-14 against v5.0.1. Twig is exact; HTML covers picture/content-block branches, extension hooks, zoom, edge outputs, runtime exclusions, and all 15 modes.                                                                  |
| carousel            | `components/carousel.html`            | `components/carousel.html.twig`                                                                                             | **completed** | Completed 2026-07-14 against v5.0.1. Twig is exact; HTML covers slides, labels, sizes, full-width, extension hooks, delegated banner media, edge output, and all 15 modes.                                                                  |
| category-filter     | `components/category-filter.html`     | `components/category-filter.html.twig`, `components/category-filter-items.html.twig`                                        | **completed** | Completed 2026-07-14 against v5.0.1. Twig is exact; HTML covers tree levels, parent/link branches, extension hooks, empty output, runtime exclusions, and all 15 modes.                                                                     |
| checkbox            | `components/checkbox.html`            | `components/checkbox-group.html.twig`, `components/checkbox-item.html.twig`                                                 | **completed** | Completed 2026-07-14 against v5.0.1. Twig is exact; HTML covers group/item branches, invalid/disabled/checked/helper/required/optional states, extension hooks, and all 15 modes.                                                           |
| content-block       | `components/content-block.html`       | `components/content-block.html.twig`                                                                                        | **completed** | Completed 2026-07-14 against v5.0.1. Twig is exact; HTML covers content/meta/list/link branches, extension hooks, runtime hooks, empty output, and all 15 modes.                                                                            |
| content-item        | `components/content-item.html`        | `components/content-item.html.twig`                                                                                         | **completed** | Completed 2026-07-14 against v5.0.1. Twig is exact; HTML covers picture/date/content branches, modifiers, hooks, extension attributes, empty output, and all 15 modes.                                                                      |
| date-block          | `components/date-block.html`          | `components/date-block.html.twig`                                                                                           | **completed** | Completed 2026-07-14 against v5.0.1. Twig is exact; HTML covers variants, date-time, month, extension hooks, empty output, no-runtime evidence, selectors, and all 15 modes.                                                                |
| datepicker          | `components/datepicker.html`          | `components/datepicker.html.twig`                                                                                           | **completed** | Completed 2026-07-14 against v5.0.1. Twig is exact; HTML covers root hooks, widths, states, optional attributes, runtime exclusions, selector evidence, and all 15 modes.                                                                   |
| description-list    | `components/description-list.html`    | `components/description-list.html.twig`                                                                                     | **completed** | Completed 2026-07-14 against v5.0.1. Twig is exact; HTML covers variants, runtime hooks and exclusions, content/type branches, extension hooks, empty output, and all 15 modes.                                                             |
| expandable          | `components/expandable.html`          | `components/expandable.html.twig`                                                                                           | **completed** | Completed 2026-07-14 against v5.0.1. Twig is exact; HTML covers content, labels, extension hooks, runtime hooks and exclusions, edge output, and all 15 non-default color modes.                                                            |
| fact-figures        | `components/fact-figures.html`        | `components/fact-figures.html.twig`                                                                                         | **completed** | Completed 2026-07-14 against v5.0.1. Twig is exact; HTML covers columns, item/source/link branches, modifiers, extension hooks, empty output, and all 15 non-default color modes.                                                           |
| featured-item       | `components/featured-item.html`       | `components/featured-item.html.twig`                                                                                        | **completed** | Completed 2026-07-14 against v5.0.1. Twig is exact; HTML covers content/media branches, link display variants, highlight/color interactions, extension hooks, edge output, and all 15 non-default color modes.                              |
| file                | `components/file.html`                | `components/file.html.twig`, `components/file-translations.html.twig`, `components/file-translation-item.html.twig`         | completed     |                                                                                                                                                                                                                                             |
| file-upload         | `components/file-upload.html`         | `components/file-upload.html.twig`                                                                                          | completed     | Completed 2026-07-15 against v5.0.1. Twig is exact; HTML covers states, extension hooks, runtime hooks/list output, empty optional fields, and all 15 non-default color modes.                                                              |
| form-group          | `components/form-group.html`          | `components/form-group.html.twig`                                                                                           | completed     | Completed 2026-07-15 against v5.0.1. Twig is exact; HTML covers wrapper/input branches, states, extension hooks, runtime hooks delegated to child inputs, edge output, and all 15 non-default color modes.                                  |
| gallery             | `components/gallery.html`             | `components/gallery.html.twig`, `components/gallery-item.html.twig`, `components/gallery-overlay.html.twig`                 | completed     | Completed 2026-07-15 against v5.0.1. Twig is exact; HTML covers media/source/grid/state/extension/runtime branches, empty output, and all 15 non-default color modes.                                                                       |
| highlight-box       | `components/highlight-box.html`       | `components/highlight-box.html.twig`                                                                                        | completed     | Completed 2026-07-15 against v5.0.1. Twig is exact; HTML covers title/body/icon/link branches, extension hooks, accessible icon output, excludes invalid no-title upstream output, and all 15 non-default color modes.                      |
| icon                | `components/icon.html`                | `components/icon.html.twig`                                                                                                 | completed     | Completed 2026-07-15 against v5.0.1. Twig is exact; HTML covers sizes, colors, transforms, accessibility, extension hooks, family/style variants, no runtime hooks, and all 15 non-default color modes.                                     |
| indicator           | `components/indicator.html`           | `components/indicator.html.twig`                                                                                            | completed     | Completed 2026-07-15 against v5.0.1. Twig is exact; HTML covers value/label/dot/runtime edge branches, extension hooks, runtime hooks and exclusions, and all 15 non-default color modes.                                                   |
| inpage-navigation   | `components/inpage-navigation.html`   | `components/inpage-navigation.html.twig`                                                                                    | completed     | Completed 2026-07-15 against v5.0.1. Twig is exact; HTML covers story layout, hooks, extension attributes, empty output, runtime states, upstream IDREF warning, and all 15 non-default color modes.                                        |
| label               | `components/label.html`               | `components/label.html.twig`                                                                                                | completed     | Completed 2026-07-15 against v5.0.1. Twig is exact; HTML covers all variants, extension hooks, empty output, no-runtime evidence, and all 15 non-default color modes.                                                                       |
| link                | `components/link.html`                | `components/link.html.twig`                                                                                                 | completed     | Completed 2026-07-15 against v5.0.1. Twig is exact; HTML covers plain, standalone/button variants, brand/inverted, icon/external/indicator branches, extension hooks, delegated indicator runtime hook, and all 15 non-default color modes. |
| list-illustration   | `components/list-illustration.html`   | `components/list-illustration.html.twig`, `components/list-illustration-item.html.twig`                                     | completed     | Completed 2026-07-15 against v5.0.1. Twig is exact; HTML covers image/icon/number variants, modifiers, extension hooks, no-runtime evidence, edge output, and all 15 non-default color modes.                                               |
| media-container     | `components/media-container.html`     | `components/media-container.html.twig`                                                                                      | completed     | Completed 2026-07-15 against v5.0.1. Twig is exact; HTML covers picture/video/embedded branches, captions, expandable/full-width/hooks/ratios, deprecated video input, and all 15 non-default color modes.                                  |
| mega-menu           | `components/mega-menu.html`           | `components/mega-menu.html.twig`, `components/mega-menu-item.html.twig`, `components/mega-menu-featured-item.html.twig`     | completed     | Completed 2026-07-15 against v5.0.1. Twig is exact; HTML covers menu levels, info/featured/container branches, modifiers, extension hooks, runtime hooks, edge output, and all 15 non-default color modes.                                  |
| menu                | `components/menu.html`                | `components/menu.html.twig`, `components/menu-item.html.twig`                                                               | completed     | Completed 2026-07-15 against v5.0.1. Twig is exact; HTML covers controls, link/current/child branches, extension hooks, runtime hooks, empty output, long menu shape, and all 15 non-default color modes.                                   |
| modal               | `components/modal.html`               | `components/modal.html.twig`                                                                                                | completed     | Completed 2026-07-15 against v5.0.1. Twig is exact; HTML covers variants, sizes, content/footer/body branches, extension hooks, runtime hooks, edge output, and all 15 non-default color modes.                                             |
| navigation-list     | `components/navigation-list.html`     | `components/navigation-list.html.twig`, `components/navigation-list-item.html.twig`                                         | completed     | Completed 2026-07-15 against v5.0.1. Twig is exact; HTML covers layout, border, variant, content, extension, dependency hook, empty-output, and all 15 non-default color modes.                                                             |
| news-ticker         | `components/news-ticker.html`         | `components/news-ticker.html.twig`                                                                                          | completed     | Completed 2026-07-15 against v5.0.1. Twig is exact; HTML covers item/link/icon/image/control/extension/runtime branches, empty output, and all 15 non-default color modes.                                                                  |
| notification        | `components/notification.html`        | `components/notification.html.twig`                                                                                         | completed     | Completed 2026-07-15 against v5.0.1. Twig is exact; HTML covers variants, optional content/link/close branches, extension hooks, runtime hooks, empty output, and all 15 non-default color modes.                                           |
| ordered-list        | `components/ordered-list.html`        | `components/ordered-list.html.twig`                                                                                         | not started   |                                                                                                                                                                                                                                             |
| page-header         | `components/page-header.html`         | `components/page-header.html.twig`, `components/page-header-expandable.html.twig`                                           | not started   |                                                                                                                                                                                                                                             |
| page-information    | `components/page-information.html`    | `components/page-information.html.twig`                                                                                     | not started   |                                                                                                                                                                                                                                             |
| page-summary        | missing                               | missing (`page-summary.html.twig`)                                                                                          | not started   |                                                                                                                                                                                                                                             |
| pagination          | `components/pagination.html`          | `components/pagination.html.twig`                                                                                           | not started   |                                                                                                                                                                                                                                             |
| picture             | `components/picture.html`             | `components/picture.html.twig`                                                                                              | not started   |                                                                                                                                                                                                                                             |
| popover             | `components/popover.html`             | `components/popover.html.twig`                                                                                              | not started   |                                                                                                                                                                                                                                             |
| quiz                | missing                               | missing (`quiz.html.twig`, `quiz-card.html.twig`)                                                                           | not started   |                                                                                                                                                                                                                                             |
| radio               | `components/radio.html`               | `components/radio-group.html.twig`, `components/radio-button.html.twig`                                                     | not started   |                                                                                                                                                                                                                                             |
| range               | `components/range.html`               | `components/range.html.twig`                                                                                                | not started   |                                                                                                                                                                                                                                             |
| rating-field        | `components/rating-field.html`        | `components/rating-field.html.twig`                                                                                         | not started   |                                                                                                                                                                                                                                             |
| search-form         | `components/search-form.html`         | `components/search-form.html.twig`                                                                                          | not started   |                                                                                                                                                                                                                                             |
| select              | `components/select.html`              | `components/select.html.twig`                                                                                               | not started   |                                                                                                                                                                                                                                             |
| separator           | `components/separator.html`           | `components/separator.html.twig`                                                                                            | not started   |                                                                                                                                                                                                                                             |
| site-footer         | `components/site-footer.html`         | `components/site-footer-ec.html.twig`, `components/site-footer-ec-section.html.twig`, `components/site-footer-eu.html.twig` | not started   |                                                                                                                                                                                                                                             |
| site-header         | `components/site-header.html`         | `components/site-header.html.twig`, `components/site-header-language-switcher.html.twig`                                    | not started   |                                                                                                                                                                                                                                             |
| skip-link           | missing                               | missing (`skip-link.html.twig`)                                                                                             | not started   |                                                                                                                                                                                                                                             |
| slogan-ticker       | missing                               | missing (`slogan-ticker.html.twig`)                                                                                         | not started   |                                                                                                                                                                                                                                             |
| social-media-follow | `components/social-media-follow.html` | `components/social-media-follow.html.twig`                                                                                  | not started   |                                                                                                                                                                                                                                             |
| spinner             | `components/spinner.html`             | `components/spinner.html.twig`                                                                                              | not started   |                                                                                                                                                                                                                                             |
| splash-page         | missing                               | missing (`splash-page.html.twig`)                                                                                           | not started   |                                                                                                                                                                                                                                             |
| spotlight           | `components/spotlight.html`           | `components/spotlight.html.twig`                                                                                            | not started   |                                                                                                                                                                                                                                             |
| table               | `components/table.html`               | `components/table.html.twig`                                                                                                | not started   |                                                                                                                                                                                                                                             |
| tabs                | `components/tabs.html`                | `components/tabs.html.twig`                                                                                                 | not started   |                                                                                                                                                                                                                                             |
| tag                 | `components/tag.html`                 | `components/tag.html.twig`, `components/tag-set.html.twig`                                                                  | not started   |                                                                                                                                                                                                                                             |
| text-area           | `components/text-area.html`           | `components/text-area.html.twig`                                                                                            | not started   |                                                                                                                                                                                                                                             |
| text-input          | `components/text-input.html`          | `components/text-input.html.twig`                                                                                           | not started   |                                                                                                                                                                                                                                             |
| text-media          | missing                               | missing (`text-media.html.twig`)                                                                                            | not started   |                                                                                                                                                                                                                                             |
| timeline            | `components/timeline.html`            | `components/timeline.html.twig`, `components/timeline-set.html.twig`                                                        | not started   |                                                                                                                                                                                                                                             |
| tooltip             | missing                               | n/a (no upstream Twig template)                                                                                             | not started   | HTML is authored by the upstream story.                                                                                                                                                                                                     |
| unordered-list      | `components/unordered-list.html`      | `components/unordered-list.html.twig`                                                                                       | not started   |                                                                                                                                                                                                                                             |
| video               | `components/video.html`               | `components/video.html.twig`                                                                                                | not started   |                                                                                                                                                                                                                                             |
