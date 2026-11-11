---
name: check
description: Verifies done conditions one by one by running them, then closes the work. For large or risky changes an independent checker looks too. Use before reporting a feature or phase with a spec as done, even if the user did not ask ("is it all done?", "wrap this up", "다 됐는지 검증해 줘", "마무리해 줘"). Do not use for small fixes or a single test run.
---

# check

Reply and write documents in the user's language.

## Purpose
Catch missing work and wrong logic by comparison and execution, not opinion, and close the work cleanly once it passes. This is a cheap check meant to run often.

## Input
- Spec path. If absent, the most recent file in `docs/specs/`.
- With no spec at all (small work), derive 3-5 done conditions from the request, write them at the top, and continue. Do not stop.
- Scope: by default, from the branch's base commit to now.
- Progress log `docs/progress/` (if any).
- `features.md` and `qa.md` in the folder named after the spec (if any).

## Output
- Report (chat): first line names the checker (`Checker: direct comparison`, external checker, internal checker, or the fallback phrase), a done-condition table (`D<n> | pass/fail/cannot verify | evidence`), findings in tiers, and the full test and lint result line. With `qa.md`, the table lists the `D<n>` conditions and every row that did not pass, and the results are saved in `qa.md`.
- When everything passes, the close-out: decisions that differed from the plan (the log's `Decision:` lines), parked findings (`Parked:` lines), remaining risks.

## Steps
1. **Compare it yourself.** Run each done condition's verification method exactly and record the result. Do not reuse earlier results. Cannot verify is not a pass. **With `qa.md`,** the product-level `D<n>` conditions and every QA row are the done conditions. With a staged plan, cover only the current stage's `D<n>` and the rows linked to its rules. Cover `auto` rows with one full test run, matched by test name. Reuse a `screen` or `human` row's result only if the code behind its rule has not changed since its evidence commit. Write results and evidence to `qa.md`, add a row with link `-` for anything unexpected, and update its first line. Save this before asking the user anything, even when rows remain open. A `screen` row passes only on a rendered screen (a screenshot or measurement), not a simulated DOM. A `human` row stays `needs human` until a person confirms it. Run every `screen` row in this step's way and step 2's way. It never becomes `needs human`; if it cannot run, keep it `unchecked` with the reason in Note.
2. **Measure if there is a UI.** Check the `fail` list and screenshots from `python3 <this skill folder>/../../scripts/measure.py <url>`. Exit code 3 means no measuring tool: measure the same items with any available browser tool or mark them cannot verify. Add `--dark` to measure dark mode. For a non-web app, run the screen-capture command in `features.md` and read the screenshots; with no command, mark them cannot verify. Tier 1 violations are defined in [ui.md](../../rules/ui.md).
3. **Use an independent checker only when large or risky.** Only when the change, counted with `git diff --numstat <base commit> -- . ':!docs' ':!*lock*' | awk '{f++; n+=$1+$2} END {print f+0, n+0}'`, exceeds 5 files or 200 lines (added+deleted), touches payments, auth, data deletion, or data migration, or the user asks. Past that count it is required unless the user says to skip it; do not excuse it as low risk. Otherwise skip step 4 and write `Checker: direct comparison` as the report's first line. When used, pass the [independent-checker.md](references/independent-checker.md) prompt and changed files to `ext.py checker`, with the rule table from `features.md` added to the done conditions if it exists. See "Calling external models" in [models.md](../../rules/models.md).
4. **If the external checker is absent or fails, go internal.** On `STATUS: off`, add no phrase; on `unavailable` or `banned`, write `External checker unavailable, verified internally (<reason>)` as the report's first line. Start a new subagent with the same prompt. Use a different tier from the builder (strong model if the builder was standard, otherwise standard model), and do not pass the main conversation or the builder's reasoning ([models.md](../../rules/models.md)).
5. **Verify every finding.** Read the code or run it. Keep what is right; discard what is wrong, with evidence.
6. **Handle by tier.** Fix Tier 1 and restart from step 1; ask about Tier 2 together ([review-layers.md](../../rules/review-layers.md)).
7. **Close when all pass.** Do not report until `qa.md` shows this run's results on every row in scope and its first line matches them. With `features.md`, compare the results to its exit conditions and list any `needs human` rows as what remains. Run the full test and lint commands and attach the result line, delete the scratch files that exist (`.git/jipda/`, `.measure/`), say which remain if deletion is blocked, and report the log's `Decision:` and `Parked:` lines. If the user made decisions, suggest recording them with `handoff decide` in one line.

## Do not
- Add features or change the design.
- Ask for permission for each external send (the script does the filtering).
- Pass something on "should work" without running it.
- Apply a checker's findings without verifying them.
- Omit the first-line phrase after a fallback.
- Commit, push, merge, open a PR, or deploy unasked. If not done, just say what remains.
