---
name: shape
description: Turns a vague idea into a spec with done conditions. Shows a first-draft hypothesis, then applies the planning and strategy tools the situation calls for. Use this first, before `design` or any code, for any new app or product idea, even when the user lists features or a stack or calls it small ("I want to build something like...", "help me flesh out this idea", "plan this product", "이런 거 만들고 싶은데", "앱 하나 만들고 싶어", "아이디어 구체화해 줘", "기획해 줘"). Do not use for changes to existing work that are already clear.
---

# shape

Reply and write documents in the user's language.

## Purpose
Turn an idea into one spec that says what gets built, what does not, and when it counts as done. This catches misread requirements and missed edge cases before they become code.

## Input
- The user's idea (one line is enough).
- The repository, if one exists.

## Output
- `docs/specs/<YYYY-MM-DD>-<topic>.md`
  - Goal, non-goals, what counts as failure
  - Done conditions, one per line: `D<n>. <condition> — <how verified>`. Example: `D3. The briefing panel scrolls to the end at 1366×768 — browser check`
  - Separate user decisions `[decision]` from agent judgment `[judgment]`
- Last line: a size call and one line naming the next step.

## Steps
0. **Scan an existing repo first.** Relevant files, callers, naming and folder conventions, test and lint commands. Put this in at most 5 lines at the top of the spec. If the idea has nothing to do with the current folder, ask where its documents should go before writing any file.
1. **Look outward first.** Before writing the draft, run a real web search. If the search tool is listed but not loaded, load it first. Search for every named technology, company, or product the user mentioned, and for 3-5 real alternatives people use today. If a name returns nothing, change the wording (maker, language, related project, date) and check official docs, package registries, GitHub, release notes, and recent news before saying it was not found. Read what users praise and complain about in reviews or forums for the closest alternatives. Go deeper with `research --competitive` when the decision needs it. Skip only for a company-internal tool with no alternatives. A small or personal app still has alternatives, so search.
2. **Show a draft first, in this form.** Mark each line as found, not found, or guessed, and link what was found. A claim that something does not exist is never "found": write "not found in <what was searched>". `Today they use` needs links. It may be guessed only when no search tool exists, and the draft must say so.
   - **For:** one specific kind of person
   - **When:** the situation that triggers the need
   - **Today they use:** the real alternatives found, including doing nothing
   - **Gap:** what those do not do, with evidence
   - **Our answer:** one sentence naming the difference from the closest alternative
   - **Scene:** one concrete use, in order, with named people: who does what, who receives what, and what happens if someone stops. Build it from the user's own example when there is one.
   - **Must be true:** the riskiest assumption
   Ask what is wrong, starting with the scene. Reacting to a draft is easier than answering an empty question.
3. **Pick the tools yourself.** Read [toolkit.md](references/toolkit.md), name what is blocking the idea, and pick only tools that could change a decision. Keep each to one table or list. Stop when the next tool would not change anything. Order them: understand the problem, generate options, choose, then stress-test. Say the plan in one line and start; the user can redirect it. If the idea is already clear, skip to step 5.
4. **Run each chosen tool.** Read only that tool's file, fill it from what you know and what the user says, and show one table or list. Ask what is wrong before the next tool. Mark assumptions. A tool that changed no decision is dropped from the spec.
5. **Call the size in one line** (the user can change it).
   - One file, obvious fix → fix it, then `check`
   - Small change → `revise`
   - Project, including any new app → `spec` → `plan` → `build` and `check` per stage. Name `review` only when a decision is hard to reverse, such as payments, personal data, or data deletion.
6. **Settle edge cases.** For a project, settle only those that change a product decision and leave the rest to `spec`. Go through empty values, boundaries, no permission, network or external service failure, and doing it twice. Ask, one at a time, only about those that change how the product feels or who it hurts. Set the rest as `[judgment]` defaults in one short list the user can overrule.
7. **Write the spec** in the [one-page form](references/decide.md). For a project, write only the user's decisions and product-level done conditions; `spec` writes the behavior rules. Give every done condition a verification method. A condition with no way to verify is not a condition. If the riskiest assumption is about demand, put its no-product test first and mark it to run before `plan`. Skip this for internal tools or when real users already asked for it.

## Do not
- Write code, design, or split work into tasks (that is `plan`).
- Invoke the next skill yourself. Only name it in one line.
- Bundle several questions in one message.
- Ask the user which tool or framework to use. Ask only about the idea, one question at a time.
- Run every tool, or fill a framework just to fill it.
- Record as `[decision]` anything the user did not say.
- Ask the user what running something would answer. Prototype and show the result instead. Ask the user only about taste and direction.
