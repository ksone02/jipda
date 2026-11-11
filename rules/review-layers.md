# The three tiers of findings

Every review (`review`, `check`, `build` task review, `design` critique) sorts findings into three tiers.

## Format of one finding
- What / why it is wrong / what to change / evidence (paper, reference, calculation, execution result).
- Discard findings with no evidence or that are vague ("more robust", "room for improvement").

## Tier 1: hard
- Wrong, harmful to users or data, or fails a done condition.
- Fix right away and report what was fixed. If it cannot be fixed, the work is not done.

## Tier 2: recommended
- Better if fixed.
- Ask together once: number, evidence, and fix cost on one line each. Fix only the numbers the user picks.
- Without an answer, proceed without fixing.

Example:
```
Pick what to fix (numbers; none leaves them as is).
1. No hint on an empty list — new users get stuck on the first screen — 10 min
2. Table numbers are not right-aligned — digits are hard to compare — 5 min
```

## Tier 3: free
- Taste and character (accent color, roundness, subtle tone). Do not flag.

## Rules for reviewers
- No over-flagging: if it is not Tier 1 or 2, do not write it.
- Do not pre-judge when assigning review ("don't flag this"). The main session judges after results arrive.
