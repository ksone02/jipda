---
name: copy
description: Collects all UI text, checks it against writing principles, shows before and after, and changes only what is approved. Use for "polish the UI copy", "review error messages", "화면 문구 다듬어 줘", "에러 메시지 점검해 줘". Do not use for changing one string to given text.
---

# copy

Reply and write documents in the user's language.

## Purpose
Make buttons, hints, and error messages simple and accurate. Change strings only, never layout.

## Input
- Target screen or folder. If absent, all UI code in the project.

## Output
- A proposal table and edits for approved items.

## Steps
1. **Collect everything.** Scan UI code and string files for user-visible text and table it.
2. **Check by principle.** For Korean UI, compare against the "문구 원칙" section and tone table in [writing-ko.md](../../rules/writing-ko.md). For other languages apply the same principles: the user is the subject, errors give cause and next step, buttons say what happens, tone is consistent. Mark principles with no violation as "pass".
3. **Propose before and after.** Table format:

   ```
   Screen | Location (file:line) | Original | Proposed | What changed
   ```
4. **Change only what is approved.** Apply only the numbers the user picks.
5. If the screen's look must change too, name `design` in one line.

## Do not
- Change layout, colors, or components.
- Edit before approval.
- Change the meaning of numbers, proper nouns, or legal text.
