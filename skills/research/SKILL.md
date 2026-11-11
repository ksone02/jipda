---
name: research
description: Confirms a research plan first, scans widely, then digs into primary sources only for the chosen directions and delivers one sourced file. Use without being asked when a decision needs evidence or reference sites need studying ("research this", "compare these", "find papers", "조사해 줘", "비교해 줘", "논문 찾아 줘"). Do not use for a fact one official doc lookup answers.
---

# research

Reply and write documents in the user's language.

## Purpose
Prevent shallow research, tunnel vision on one term, and wasted tokens. Research exists to make a decision, so write the decision first.

## Input
- The research question and the decision it serves (ask once if unknown).

## Output
- `docs/research/<YYYY-MM-DD>-<topic>.md`
  - `## Decision`: the decision this research serves
  - `## Findings`: a source link for every claim
  - `## Certain / estimated`
  - `## Implications`: effect on the decision
- In chat, a summary of about 5 lines only.

## Steps
1. **Write a research plan and get confirmation** ([brief-template.md](references/brief-template.md)). Decision, what is already known, findings that would change the decision, 4-6 angles (synonyms, adjacent fields, other languages, opposing views, primary source types). Readable in a minute.
2. **Scan widely.** Write a prompt file per angle. If an external searcher is configured, run them together with `ext.py searcher` (see "Calling external models" in [models.md](../../rules/models.md)); on `STATUS: off`, go to step 3. The result is a sourced map: main branches, representative sources, gaps.
3. **If the external searcher is absent or fails, go internal.** Give the same angles to light model subagents ([searcher-prompt.md](references/searcher-prompt.md)). On `unavailable` or `banned`, write `External searcher unavailable, researched internally (<reason>)` as the first line of the result ([models.md](../../rules/models.md)).
4. **Let the user choose direction.** Show the map; the user picks branches to pursue.
5. **Go deep.** Primary sources, not summaries: paper bodies and citation chains, official docs, source code, repositories. A standard model subagent or the main session does this. Stop when new sources add nothing new.
6. **Write the result file.** Only a summary goes to the main conversation.

## Do not
- Run experiments or change code (experiments are `experiment`).
- Put data values or personal information in search queries ([data-safety.md](../../rules/data-safety.md)).
- Cite links you did not read.
- Go deep without a confirmed research plan.
