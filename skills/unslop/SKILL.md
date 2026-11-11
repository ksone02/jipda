---
name: unslop
description: Removes the AI feel from prose. Korean is fixed by the Korean rules, with long text finished by humanize-korean when installed; English by the English rules. Use for "remove the AI feel", "make this sound human", "AI 티 빼 줘", "사람이 쓴 것처럼 고쳐 줘". Do not use for writing new text or changing content.
---

# unslop

Reply in the user's language and keep the text in its original language.

## Purpose
Make READMEs, reports, docs, and reply drafts read as human-written. Keep the meaning; change only the expression.

## Input
- A file path or pasted text. If its place (Notion, README, screen, reply) is unknown, infer from content and state it in one line.

## Output
- The edited text (edit the file if given a file), and a 3-5 line summary of changes.

## Steps
1. **Decide language and place.**
2. **Edit by the rules.**
   - Korean: [writing-ko.md](../../rules/writing-ko.md). Tone by place, plain words, meaning and unit of numbers.
   - English: [writing-en.md](../../rules/writing-en.md). Structure first (staged emphasis, set rhythms, inflation, chat residue, explaining what the reader knows).
3. **Finish long Korean text.** Over 500 characters, call `humanize-korean:humanize-korean` with the Skill tool to polish last. If not installed, skip and say so in one line.
4. **Confirm the meaning held.** Compare with the original: no number, proper noun, quote, link, code, or claim is lost or changed.

## Do not
- Add content or change claims.
- Insert facts or stock phrases absent from the original.
- Edit code blocks, quotes, or numbers.
