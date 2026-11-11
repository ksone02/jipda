---
name: diagnose
description: Diagnoses bugs and performance regressions with unknown causes. Builds a check that fails only on this bug before fixing anything. Use when a cause must be found ("there's an error", "why isn't this working", "it got slow", "에러 나", "왜 안 되지", "갑자기 느려졌어"). Do not use for obvious typos or one-line fixes.
---

# diagnose

Reply and write documents in the user's language.

## Purpose
Stop burning time on repeated guess-and-fix. Once you have a check that fails red, the cause is almost found.

## Input
- The symptom (error text, how to reproduce, since when).

## Output
- A check (failing test or script), one paragraph on the cause (file:line evidence), a minimal fix, and the check passing after the fix.

## Steps
1. **Build the check first.** It must fail only on this bug. Try the easy ones first.
   1. A failing test calling that spot
   2. A curl script against the running server
   3. Run the CLI with fixed input and diff against good output
   4. A browser script driving the screen
   5. Save real requests or events and replay them
   6. A temporary rig running part of the system
   7. 1,000 random inputs to catch intermittent errors
   8. `git bisect run` between a good and a bad commit
   9. Same input to old and new versions, compared
   10. If only a human can trigger it, a script guiding the clicks
2. **Refine the check.** Faster (drop needless setup), sharper (check the symptom itself), more deterministic (fix time and seeds).
3. **Form a hypothesis.** Trace back to where the symptom first goes wrong ([techniques.md](references/techniques.md), root-cause tracing).
4. **Make one minimal fix.** It is fixed only when the check and all existing tests pass.
5. **After two failures on the same premise,** write the premise down and verify it directly ([core.md](../../rules/core.md)).
6. Keep the check as a test and report.

## Do not
- Do unrelated cleanup or refactoring.
- Fix without a check and say "seems fixed".
- Call a guard that hides the symptom a root-cause fix.
- Leave secrets in output (replace with `<REDACTED>`).
