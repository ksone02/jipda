---
name: design
description: Builds or heavily reworks dashboard, tool, and landing screens. Measures in a real browser at three widths and critiques screenshots. Always use this first before writing UI code, even mid-feature and even if the user did not ask. Do not use for tiny tweaks or for change requests on an existing screen's details (that is `revise`).
---

# design

Reply and write documents in the user's language.

## Purpose
Build screens that do not look AI-made and are actually easy to use. Verify with measurement and screenshots, not by eye.

## Input
- The request (screen to build or rework) and the project.
- `features.md` in the spec folder, if the screen is listed there.
- `--landing`: for landing and intro pages.

## Output
- UI code changes.
- Measurement report `.measure/report.json` and 3 screenshots.
- Report: Tier 1 violations fixed, Tier 2 questions, measured `fail` results.

## Steps
1. **Decide the screen type.**
   - With `--landing`: if the optional landing kit skill `taste-skill:design-taste-frontend` is available, use it and then do only steps 4-6 here; otherwise follow [landing.md](references/landing.md).
   - Otherwise use the dashboard and tool approach ([operate-mode.md](references/operate-mode.md)).
2. **Read the project first.** Follow existing tokens, components, and `DESIGN.md`. To study reference sites, name `research --competitive` in one line. For a project's first screen, show 2-3 directions (mainly information layout) side by side and let the user pick. Later screens follow that choice.
3. **Build.** If `features.md` lists this screen, build every listed state and use its exact messages. Follow [ui.md](../../rules/ui.md) Tier 1 from the start. When reworking an AI-looking screen, run the process in [anti-slop.md](references/anti-slop.md); when building new, avoid its signs. Fill the space left by removed decoration with real content and hierarchy. For copy, use [writing-ko.md](../../rules/writing-ko.md) on Korean screens and [writing-en.md](../../rules/writing-en.md) otherwise.
4. **Measure.** Run `python3 <this skill folder>/../../scripts/measure.py <url or file>`. Exit code 3 means no measuring tool: measure the same items with any available browser tool. Widths are 1440x900, 1366x768, 390x844. Every `fail` is Tier 1. For a non-web app, use the screen-capture command in `features.md` at the app's device sizes instead; with no command, report the screen as not measured.
5. **Critique the screenshots.** Open all three with Read, critique in the order of [critique.md](references/critique.md), and fix the 3 biggest problems. Repeat steps 4-5 at most 3 times. A problem visible in a screenshot is real no matter what the code says.
6. **Sort by tier.** Report Tier 1 fixes; ask Tier 2 (`UI-R`) together ([review-layers.md](../../rules/review-layers.md)).

## Do not
- Do copy-only edits (that is `copy`).
- Change feature or data logic.
- Say "responsive checked" without measuring.
- Overwrite an existing design system with new tokens.
- Keep fixing past 3 rounds (report what remains as a list).
