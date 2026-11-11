# Model tiers and external tools

Skills speak in tiers, not model names: **light model**, **standard model**, **strong model**.

## Division of work

| Work | First choice | If absent or failing |
|---|---|---|
| Wide search, reading sources | Configured external searcher | Light model subagent |
| Comparison checks, execution checks, rebuttal | Configured external checker | Subagent under the independence conditions |
| Expert role review | Standard model (strong model for big design calls) | — |
| Shaping, design, synthesis | Main session | — |
| Repeated implementation | Tier table below | — |

## Calling external models
External tools are off by default. Enable them with `/jipda:setup`.
- Command: `python3 <plugin folder>/scripts/ext.py <checker|searcher> --root <repo> --timeout 540 --prompt-file <prompt> [files...]`. The plugin folder is two levels above the skill folder.
- Call the Bash tool with `timeout: 600000`. The script must finish first for the `STATUS:` line to survive.
- Independent calls may run together.
- `STATUS: off` means not configured. Go internal with no phrase.
- On `STATUS: unavailable` or `banned`, go internal and write the fallback phrase below as the result's first line.

## Tier table
The cheapest model can use 2-3x the turns on multi-step work, so total cost may be higher.
- **Light model**: transcription and tests when the plan has all the code, one-file mechanical edits, search.
- **Standard model**: implementing from a description, multiple files, minimum tier for every reviewer.
- **Strong model**: design judgment, or escalation after more than 3 stuck fix rounds.

## Picking the actual model
1. If `models` (`light`, `standard`, `strong`) in `ext.py status` has a value, use that name.
2. Otherwise in Claude Code: light model = `haiku`, standard model = `sonnet`, strong model = `opus`.
3. Where subagent models cannot be chosen, use the session model.
- When you can choose, always set the Agent tool's `model`. Omit it and the subagent inherits the expensive session model.

## Independence conditions for internal verification
- A new subagent that does not inherit the main conversation.
- Give only done conditions and outputs, not the builder's reasoning.
- A different tier from the builder (strong model if the builder was standard).

## Fallback first lines
- `External checker unavailable, verified internally`
- `External searcher unavailable, researched internally`
- Add the reason in parentheses (not installed, usage limit, timeout, project bans external AI).

## Browser
To drive a screen directly, prefer the tool set as `browser` in `ext.py status`; otherwise use any available browser tool.
