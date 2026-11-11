# jipda

English | [한국어](README.ko.md)

A Claude Code skill set for people who both build software and do research. The name comes from the Korean word *jipda* (짚다), to check things one by one before moving on.

- Skills trigger from plain language, and implementation-flow skills trigger before the work starts even if you do not ask. Descriptions exclude small fixes, and `build` and `review` confirm before using subagents.
- Feedback comes in two kinds: cheap verification often, and expensive expert review only right after planning and design.
- Runs on Claude Code alone. External checkers and searchers are opt-in through `/jipda:setup`.
- Instructions are in English. Replies and documents follow your language.

## Install

```text
/plugin marketplace add ksone02/jipda
/plugin install jipda@jipda
```

To install from a local clone, replace `ksone02/jipda` on the first line with its folder path.

Then, optionally, run `/jipda:setup` to choose external tools, a browser tool, model tiers, and the standing principles.

### Standing principles (optional, recommended)

Puts 6 lines in `~/.claude/CLAUDE.md` that hold even when no skill runs. Read [rules/always.md](rules/always.md) first.

```sh
python3 scripts/always.py install   # add (running it twice keeps one copy)
python3 scripts/always.py remove    # remove (text outside the block is untouched)
```

## Skills

| Skill | What it does |
|---|---|
| `shape` | Turns a vague idea into a spec with done conditions, through questions |
| `plan` | Splits a spec into task units, riskiest first |
| `build` | Implements a plan. Small plans directly; only large or risky tasks go to subagents |
| `check` | Verifies done conditions by running them, then closes the work. Independent checks only for large or risky changes |
| `review` | Expert-perspective review. One reviewer by default, several only for hard-to-reverse decisions (quant, web, data research) |
| `research` | Research plan → wide scan → choose direction → deep read → one sourced file |
| `experiment` | Raises one metric through repeated experiments, logging and keeping or reverting each attempt |
| `handoff` | Pause, resume, record decisions |
| `guard` | Turns on or off a hook that asks before dangerous commands (off by default) |
| `diagnose` | Bug diagnosis that starts with a failing check |
| `design` | Builds dashboard, tool, and landing screens, measured at three widths |
| `copy` | Collects and reviews UI copy, changing only what you approve |
| `setup` | Chooses external checkers and searchers, browser tool, model tiers, and standing principles |
| `docs` | Writes docs from the code, or fixes where docs drift from it |
| `unslop` | Removes the AI feel from prose. Long Korean text is finished with humanize-korean when installed |

Invoke with `/jipda:<skill> <args>`, for example `/jipda:research compare Python backtesting libraries`.

## Optional tools

Everything works without these. Enable them with `/jipda:setup`; settings live in `~/.config/jipda/config.json`.

| Tool | Used by | Without it |
|---|---|---|
| External checker (e.g. `codex`) | `check`, `review` | An internal subagent checks under independence conditions |
| External searcher (e.g. `aside`) | `research` | Internal subagents search |
| `agent-browser` or playwright | Screen measurement in `design`, `check` | Measures the same items with any available browser tool |
| taste-skill (landing kit, about 39MB) | `design --landing` | Uses jipda's built-in landing rules |
| humanize-korean | `unslop` | Skips that step and says so |

[scripts/safe_files.py](scripts/safe_files.py) filters files sent externally: data folders, `.env`, data files, large files, and files containing keys are excluded. If a project's `CLAUDE.md` says something like "no external AI", external models are not used.

## Development

```sh
uv sync
uv run pytest                                # scripts and skill format; also screen measurement if agent-browser or playwright is available
claude --plugin-dir . plugin details jipda   # skill list and token cost
```

## License

MIT. Sources and copyrights are in [NOTICE.md](NOTICE.md). `anti-slop.md` and `design-tokens.md` in `skills/design/references/` are CC BY 4.0.
