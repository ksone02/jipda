---
name: experiment
description: Raises one metric through repeated experiments. Fixes the measuring harness first, measures every change, keeps or reverts it, and logs everything. Use for "improve this metric", "run experiments", "이 지표 올려 줘", "실험 돌려 줘". Do not use for a single analysis or backtest run.
---

# experiment

Reply and write documents in the user's language.

## Purpose
Remove "seems better" from research that raises one number, such as alpha search or model performance tuning. Do not keep fake improvements from leakage or overfitting.

## Input
- Metric, target value, repository under experiment.

## Output
- A measuring harness (script) and proof of its sensitivity.
- Attempt log `docs/experiments/<topic>/decision.tsv` (format in [decision-log.md](references/decision-log.md)).
- One commit per kept change.
- Report: baseline → final (difference and unit), attempts (kept/reverted), one line per kept change, what to try next.

## Steps
1. **Write the goal.** Metric definition, target, current value (baseline), noise size (spread of 3 runs of the same setup). Do not loosen the target later.
2. **Build and freeze the harness.**
   - Run a change known to work and one known not to, proving the harness detects the difference.
   - Add leakage and overfitting checks: future information, selecting and reporting on the evaluation window, chance given attempts, out-of-sample windows.
   - After proof, do not change the harness. If you must, do it in a separate commit and remeasure the baseline.
3. **Open the log.** Read it before each attempt.
4. **One change at a time.** Give the hypothesis a concrete reason ("removing X reduces Z because of Y"). Delegate attempts to a subagent (standard model if only described, light model if the code is fixed, [models.md](../../rules/models.md)); the main session supervises and logs.
5. **Measure and decide.** Measure before and after with the frozen harness and run regression tests. Keep and commit only when it beats noise and tests pass (`git add` only changed files). Otherwise revert fully. Log one line either way.
6. **Do not stop at the first plateau.** After several failures in a row, change direction, combine near misses, or reread the source. Do not quit while cheap attempts remain.
7. Stop and report when the target is reached or remaining attempts are not worth their cost.

## Do not
- Survey literature (that is `research`).
- Stack several changes before measuring.
- Declare improvement from reading code alone.
- Lower the target to pass.
- Send competition or external data to external models ([data-safety.md](../../rules/data-safety.md)).
