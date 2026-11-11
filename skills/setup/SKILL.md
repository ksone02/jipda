---
name: setup
description: Turns jipda's optional features on or off. Asks about external checkers and searchers, browser tools, model tiers, and standing principles, then saves them to the user's config file. Use only for "set up jipda", "connect external models", "jipda 세팅해 줘", "외부 모델 연결해 줘". Do not use for skill usage questions or project settings.
---

# setup

Reply in the user's language.

## Purpose
jipda runs with no setup at all. This skill lets those who want it connect external tools and models. Settings stay on the user's machine, not in the repository, and survive plugin updates.

## Input
- None. Detect tools installed on this machine.

## Output
- `~/.config/jipda/config.json` (override with `JIPDA_CONFIG`).
- If chosen, the standing principles block in `~/.claude/CLAUDE.md`.

## Steps
1. **See the current state.** Run `python3 <this skill folder>/../../scripts/ext.py status` and `command -v codex aside agent-browser`. If a config exists, read it and keep values you do not change.
2. **Ask one at a time.** Offer installed tools first; "none" is always available.
   - External checker: used by `check` and `review` for independent checks.
   - External searcher: used by `research` for wide scans.
   - Browser tool: `agent-browser` (recommended, Apache-2.0, multi-platform), ego lite (macOS app, closed-source app), or none. The screen-measuring script needs agent-browser or playwright.
   - Model tiers: keep defaults or name `light`, `standard`, `strong`.
   - Whether to install the standing principles.
3. **Warn when enabling an external tool.** Say in one line that code and prompts go to that tool, and name the filtering rules in [data-safety.md](../../rules/data-safety.md).
4. **Write the config.** Save only what was chosen, as JSON. `{workdir}` is a temp folder holding only allowed file copies, `{output}` is the file for the answer, `{prompt}` is the prompt. Without `{prompt}`, the prompt goes to stdin.
   ```json
   {
     "checker": {"cmd": ["codex", "exec", "--skip-git-repo-check", "-s", "read-only", "-C", "{workdir}", "-o", "{output}", "-"]},
     "searcher": {"cmd": ["aside", "-m", "<model name>", "{prompt}"]},
     "browser": "agent-browser",
     "models": {"light": "haiku", "standard": "sonnet", "strong": "opus"}
   }
   ```
5. **If standing principles were chosen,** run `python3 <this skill folder>/../../scripts/always.py install`.
6. **Confirm.** Run `ext.py status` again and show the result.

## Do not
- Enable tools the user did not pick.
- Install tools without asking. If installation is needed, give the command.
- Put API keys or tokens in the config file.
- Write personal settings inside the repository.
