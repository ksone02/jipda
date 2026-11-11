---
name: build
description: Implements a plan document and reviews the result. Small plans are done directly; only large or risky tasks go to subagents. Use this first, even if the user did not ask, when implementing work that has a plan document ("build it", "next step", "ㅇㅋ 만들자", "다음 단계 진행해"). Do not use for small fixes with no plan.
---

# build

Reply and write documents in the user's language.

## Purpose
Implement to plan and catch mistakes through review. Small plans stay in the main session to save cost; only large or risky tasks are delegated.

## Input
- Plan path. If absent, the most recent file in `docs/plans/`.
- Spec (the path in the plan's header).

## Output
- Commits (one per task).
- Progress log `docs/progress/<YYYY-MM-DD>-<topic>.md`. Format: [progress-log.md](references/progress-log.md).

## Steps
If the user did not invoke this with a slash and some tasks will be delegated, first say "Implementing N tasks with agents" in one line and get confirmation.

1. **Open the progress log first.** Do not redo tasks with a `T<n>: complete` line. After compaction, trust this file and `git log` over memory.
2. **Choose how to implement.** Default is the main session doing it directly: write the test, see it fail, implement, see it pass, commit per task. Delegate only when independent tasks are numerous enough to fill the main context, one task changes several files in different areas, or the task is hard to reverse if wrong, such as code touching real money or production data. When delegating, send small same-shape edits together. Steps 3-6 apply only to delegated tasks.
3. **Start implementer subagents.** Always set the Agent tool's `model` per the tier table in [models.md](../../rules/models.md) (light model if the plan contains all the code, standard model if it only describes it). Give the brief as a file in the [implementer-brief.md](references/implementer-brief.md) format (`.git/jipda/brief-T<n>.md`). Scratch files live in `.git/` so they cannot be committed by accident.
4. **Take the status report.** Implementers answer with one of four.
   - `done`: tests pass
   - `concerned`: done but doubtful somewhere (says where)
   - `blocked`: could not do it (why)
   - `needs context`: information missing (what)
   On `blocked` or `needs context`, the main session answers and continues the same implementer. Do not fix it directly (contexts mix and review gets skipped).
5. **Review per task.** Run `mkdir -p .git/jipda && git diff <start commit>..HEAD > .git/jipda/review-T<n>.diff`, then give a reviewer subagent (standard model or better, [task-reviewer.md](references/task-reviewer.md)) the brief, report, and diff paths. Get both verdicts: does it match the spec, and is the quality fine. Handle results with the tiers in [review-layers.md](../../rules/review-layers.md).
6. **At most 3 fix rounds.** Send remaining Tier 1 findings back to the implementer. After 3 rounds, stop, log remaining findings as "parked + reason", and report them together. From the 4th attempt use one tier up.
7. **Directly implemented work always gets one final review.** Never skip it for a small plan and never defer it to `check`. Run `git diff <start commit>..HEAD > .git/jipda/review-all.diff` and give one reviewer subagent (standard model, [task-reviewer.md](references/task-reviewer.md)) the spec, plan, and diff paths. The main session fixes Tier 1 findings, at most 3 rounds.
8. Log a completion line per task. When all are done, name `check` in one line.

## Do not
- Add features not in the plan.
- Skip the final review because the work was done directly.
- Drop test-first or per-task commits when implementing directly.
- Take outward actions other than commits (push, deploy, PR).
- Start a subagent without setting a model (it inherits the expensive session model, [models.md](../../rules/models.md)).
- Pre-judge for reviewers ("don't flag this").
- Move on while Tier 1 findings remain.
- Mark done on an implementer's "tests pass" alone (run the test command yourself).
