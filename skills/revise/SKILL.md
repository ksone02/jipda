---
name: revise
description: Use this first, before editing, whenever the user asks to change work that already exists, covering behavior, code structure, or design, one item or many at once ("change this, this, and that", "restructure this", "fix the design like this", "이거 바꿔 줘", "여기 수정해 줘", "구조 좀 정리해 줘", "디자인 이렇게 고쳐 줘"). Do not use for one obvious one-line edit such as a single rename or color, for new features, or for bugs with unknown causes.
---

# revise

Reply in the user's language.

## Purpose
Handle change requests cheaply, without misreading them or breaking something else.

## Input
- The request, often several changes in one message.

## Output
- The edits.
- One table: `# | changed (file:line) | verification result`.

## Steps
1. **List the items.** Split the request into numbered lines: `what changes → desired result`. Include small items mixed into a multi-item request. Ask about ambiguous items only, together in one message. Start the clear ones right away.
2. **Find what it can break.** Before each behavior or structure edit, search for what uses the thing being changed (`grep`, callers, shared styles), then check what search misses: API or JSON shapes, stored data, config and flags, code that reads the same value elsewhere. If the request asserts something about existing code, treat it as unconfirmed until you see it. Name the one fact the change is safe because of and prove it with one small run. Skip this step for text-only or purely visual items.
3. **Make each item's smallest edit, by kind.**
   - Behavior: add one test for the changed behavior.
   - Code structure: keep behavior the same. Existing tests passing is the bar; with none, run the changed path once.
   - Design: measure only the changed screen with `python3 <this skill folder>/../../scripts/measure.py <url or file>` and look at the screenshots. Follow [ui.md](../../rules/ui.md) Tier 1.
4. **Verify once at the end.** Run the full test command once after all items, not after each one.
5. **Report the table.** Mark any safety fact you could not prove as `unproven` in its row. If a spec exists and an item changes a decision in it, edit that line.

**When the user repeats an item or says it missed,** do not edit yet. Say it back differently, in plain words and the user's own terms: `expected / actual now` in one line. Confirm it first.

## Do not
- Change anything outside the listed items, or tidy along the way.
- Use delegated agents, separate reviews, or plan documents.
- Rerun the full tests after every item.
- Report an item as done without its verification result.
