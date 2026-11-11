---
name: review
description: Reviews a plan or design from a domain expert's perspective and sorts findings into three tiers. Use only on an explicit request for expert review ("get expert feedback on this", "전문가 검토해 줘", "전문가 피드백 돌려 줘"). Do not use for casual "take a look" questions or automatically right after writing a document.
---

# review

Reply and write documents in the user's language.

## Purpose
Get findings only a domain expert would think of. This is expensive, so use it in two places before building: right after planning and right after design. After development, use it only when results differ from expectations.

## Input
- Role name (optional): `quant`, `web`, `data-research`, or a new domain.
- Target: spec or plan path. If absent, the most recent file in `docs/plans/`, then `docs/specs/`.

## Output
- Report (chat): first line names the chosen role, then Tier 1 findings and fixes, then Tier 2 questions (number, evidence, cost).
- The corrected spec or plan.

## Steps
If the user did not invoke this with a slash, first say "Running expert review with N reviewers" in one line and get confirmation.

1. **Pick the role.** With a name, use that file under [roles/](references/roles/). Otherwise pick from the target and state it in the first line (the user can change it). With no matching file, write 3 roles with must-check items on the spot and ask at the end whether to save them.
2. **Use one reviewer by default.** Give one subagent (standard model) all role sections of the chosen file at once. The prompt is [reviewer-prompt.md](references/reviewer-prompt.md), with the domain name as the role name. Start one reviewer per role in parallel only for hard-to-reverse structural decisions, decisions involving real money or user data, or when the user asks for several. Use the strong model for hard-to-reverse structural decisions ([models.md](../../rules/models.md)). If an external checker is configured and useful, add one more by passing the same prompt and target path to `ext.py checker` (see "Calling external models" in [models.md](../../rules/models.md)). On `STATUS: off`, skip it; on `unavailable` or `banned`, skip it and add the line `External checker unavailable, verified internally (<reason>)` to the report.
3. **Collect and filter.** Discard findings without evidence and Tier 3 (taste). Merge duplicates.
4. **Verify findings.** Confirm with code, data, or calculation. Discard wrong ones with evidence.
5. **Handle by tier** ([review-layers.md](../../rules/review-layers.md)). Fix Tier 1 in the target document; ask Tier 2 in one message; without an answer, do not change them.
6. One line for the next step (`plan` after spec review, `build` after plan review).

## Do not
- Change implementation code (documents only).
- Review at every step.
- Pre-judge in role prompts ("don't flag this").
- Ask Tier 2 findings one by one.
- Apply unverified findings as fact.
