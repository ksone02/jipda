# Document formats

Write headings, column names, and values in the user's language. IDs stay `F`, `S`, `R`, `Q`. Column order is fixed. Cells never contain line breaks.

## features.md, in this order

**Summary:** one paragraph and a link to the `shape` document. This is the only prose.

**Open questions**
`Question | Blocks`
`Blocks` is a feature ID or `-`. A question that blocks a P0 or P1 feature stops `plan`.

**Change log**
`Date | What changed | Changed IDs | Why`

**Scope and verification**
`Item | Value`
Rows: in scope, out of scope, exit conditions, test environments, test command, command to prepare test data and accounts, command to launch the app and capture a screen. Write `plan fills this` for a command that does not exist yet.

**Features**
`ID | Feature | Priority | Purpose | Scenario | Screens | Screen states`
- Priority is `P0`, `P1`, `P2`, or `excluded`.
- Scenario is one concrete use with named people, using `→` between steps.
- Screens and screen states apply only when the feature has a screen. Otherwise write `-`.

**Screens** (only with a UI)
`ID | Screen | Type | Entered from | Condition | Goes to`

**Rules**, sorted by feature
`ID | Feature | Type | Condition | Action | Message | Source | Verify`
- Feature is a feature ID, or `common` for rules across features: permissions, data exposure, calculations, external service failures, legal requirements.
- Type: `normal`, `exposure`, `permission`, `duplicate`, `network`, `boundary`, `validation`, or another short word that fits.
- Message is the exact text the user sees, or `-`.
- Source: `decision`, `judgment`, or `current`.
- Verify: `auto`, `screen` (browser, simulator, or device, with an agent looking at it), or `human`.

## qa.md

First line, written by `check`: `Last check: <date> | pass <n> | fail <n> | unchecked <n> | needs human <n>`

`ID | Link | Situation | Expected | Result | Evidence | Note`
- Link is a rule ID or `D<n>`. Use `-` for an exploratory row added when testing found something unexpected.
- Situation combines the starting state and the action. For an automated row, add the test name once it exists.
- Result: `unchecked`, `pass`, `fail`, or `needs human`. With more than one test environment, use one result column per environment instead.
- A `human` rule stays `needs human` until a person confirms it. An agent never passes it.
- A `screen` rule is run by an agent and never becomes `needs human`. If it cannot run, keep `unchecked` and give the reason in Note.
- Evidence is the commit and that row's own test name or screenshot path. Example: `268e974 storage.test.js "blocked storage keeps the item until reload"`. A bare test command or a file name alone is not evidence.
- For a failed row, Note holds the actual result and how to reproduce it.
