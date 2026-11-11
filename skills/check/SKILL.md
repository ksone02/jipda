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

## Output
- Report (chat): first line names the checker (`Checker: direct comparison`, external checker, internal checker, or the fallback phrase), a done-condition table (`D<n> | pass/fail/cannot verify | evidence`), findings in tiers, and the full test and lint result line.
- When everything passes, the close-out: decisions that differed from the plan (the log's `Decision:` lines), parked findings (`Parked:` lines), remaining risks.

## Steps
1. **Compare it yourself.** Run each done condition's verification method exactly and record the result. Do not reuse earlier results. Cannot verify is not a pass.
2. **Measure if there is a UI.** Check the `fail` list and screenshots from `python3 <this skill folder>/../../scripts/measure.py <url>`. Exit code 3 means no measuring tool: measure the same items with any available browser tool or mark them cannot verify. Tier 1 violations are defined in [ui.md](../../rules/ui.md).
3. **Use an independent checker only when large or risky.** Only when the change, counted with `git diff --numstat <base commit> | awk '{f++; n+=$1+$2} END {print f+0, n+0}'`, exceeds 5 files or 200 lines (added+deleted), touches payments, auth, data deletion, or data migration, or the user asks. Otherwise skip step 4 and write `Checker: direct comparison` as the report's first line. When used, pass the [independent-checker.md](references/independent-checker.md) prompt and changed files to `ext.py checker`. See "Calling external models" in [models.md](../../rules/models.md).
4. **If the external checker is absent or fails, go internal.** On `STATUS: off`, add no phrase; on `unavailable` or `banned`, write `External checker unavailable, verified internally (<reason>)` as the report's first line. Start a new subagent with the same prompt. Use a different tier from the builder (strong model if the builder was standard, otherwise standard model), and do not pass the main conversation or the builder's reasoning ([models.md](../../rules/models.md)).
5. **Verify every finding.** Read the code or run it. Keep what is right; discard what is wrong, with evidence.
6. **Handle by tier.** Fix Tier 1 and restart from step 1; ask about Tier 2 together ([review-layers.md](../../rules/review-layers.md)).
7. **Close when all pass.** Run the full test and lint commands and attach the result line, delete scratch files (`.git/jipda/`, `.measure/`), and report the log's `Decision:` and `Parked:` lines. If the user made decisions, suggest recording them with `handoff decide` in one line.

## Do not
- Add features or change the design.
- Ask for permission for each external send (the script does the filtering).
- Pass something on "should work" without running it.
- Apply a checker's findings without verifying them.
- Omit the first-line phrase after a fallback.
- Commit, push, merge, open a PR, or deploy unasked. If not done, just say what remains.
