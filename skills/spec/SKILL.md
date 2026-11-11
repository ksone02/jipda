---
name: spec
description: Writes a decided project's feature spec, the single source of truth, and its QA checklist as tables, then keeps them in sync when rules change. Use after `shape` on project-size work, or when the user asks ("write the feature spec", "make a QA sheet", "update the spec for this rule", "기능 명세서 써 줘", "QA 시트 뽑아 줘", "이 규칙 바뀌었어, 명세 반영해 줘"). Do not use for small changes or when what to build is still undecided (that is `shape`).
---

# spec

Reply and write documents in the user's language.

## Purpose
Say exactly how the product must behave in one place, and give verification a checklist tied to it, so a changed rule shows what else must change. `features.md` is the source of truth. If `qa.md` disagrees with it, `qa.md` is wrong.

## Input
- A `shape` document, notes, or existing code. If absent, the most recent file in `docs/specs/`.
- For a change: the rule that changed, in the user's words.

## Output
- `docs/specs/<YYYY-MM-DD>-<topic>/features.md`: what must happen. Formats: [formats.md](references/formats.md).
- `docs/specs/<YYYY-MM-DD>-<topic>/qa.md`: whether it happens now.
- The `shape` document, shortened (step 5).
- Last line: blocking open questions, if any, and one line naming the next step.

## Steps
If the documents already exist and a rule changed, go to **When a rule changes**.

1. **Read the sources.** Mark each rule's source: `decision` (the user said it), `judgment` (the agent proposed it), or `current` (read from existing code).
2. **Write `features.md`.** Everything except the summary is a table, and each row is one line. If a cell needs a line break, split the row. Fill only sections that apply.
3. **Test the rules against each other.** Find contradictions, one condition with two actions, and rules that depend on something undecided. Fix what the sources settle. An item with a safe default, such as a length limit, becomes a `judgment` rule, not a question. Put only the rest in open questions, naming the feature each one blocks.
4. **Close the gaps.** For every P0 feature, cover permission, duplicate action, network failure, and boundary values. A type that cannot occur gets one row with the action `n/a` and why. Ask, one at a time, only about `judgment` rules the user has never seen and that would change a QA result. Leave the rest as `judgment`.
5. **Make `features.md` the only home for behavior.** Move rules and behavior-level done conditions out of the `shape` document and leave a link. Keep the goal, reasons, risks, and product-level `D<n>` conditions there, such as a store release or a user trial.
6. **Write `qa.md` from the rules.** One row checks one thing. Depth follows priority: P0 every case, P1 the main flow and failures, P2 one row. Choose cases by rule type: number ranges by boundary values, condition combinations by a decision table, status changes by state transitions. Add a row only if it could fail for a different reason than the rows before it. All results start as `unchecked`.
7. **Check the links.** Every rule of a non-excluded feature has a QA row, every QA link names a rule or `D<n>` that exists, and every feature has a priority. Fix misses on the spot.

**When a rule changes** (also a message, screen, screen state, or added feature; a purely visual change does not come here):
1. Find the ID in `features.md`, or add new `F`, `R`, and `Q` rows for an added feature. Then find every QA row linked to it and every rule it contradicts or depends on. Show that list before editing. If a contradiction needs a decision, ask it first.
2. Edit the rules, add a change-log row (date, what changed, changed IDs, why), and update the affected QA rows. Set every QA row linked to a changed rule to `unchecked` and clear its evidence, even if the row's text did not change.
3. Never reuse or renumber an ID.

## Do not
- Write how to implement it (that is `plan`) or design screens (that is `design`).
- Put results, implementation status, or evidence in `features.md`.
- Copy a rule's full text into `qa.md`. Write only that situation's expected value.
- Add rows to look thorough.
- Add a feature the sources do not name. Put it in open questions instead.
- Mark as `decision` anything the user did not say.
- Invoke the next skill yourself. Only name it in one line.
