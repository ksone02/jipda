# NOTICE

이 저장소의 일부 문장과 절차는 아래 저장소를 참고하거나 옮겨 와 고쳤어요. 파일마다 어디서 왔는지는 아래 "파일별 출처"에 적었어요.

| 저장소 | 저작권 | 라이선스 |
|---|---|---|
| obra/superpowers | Copyright (c) 2025 Jesse Vincent | MIT |
| mattpocock/skills | Copyright (c) 2026 Matt Pocock | MIT |
| addyosmani/agent-skills | Copyright (c) 2025 Addy Osmani | MIT |
| cursor/plugins (pstack), michael-denyer/pstack-claude | Copyright (c) 2026 Lauren Tan; port (c) 2026 Michael Denyer | MIT |
| toss/apps-in-toss-harness | Copyright (c) 2026 Viva Republica, Inc. | BSD-3-Clause |
| toss/es-toolkit, toss/react-simplikit | Copyright (c) 2024, 2025 Viva Republica, Inc. | MIT |
| toss/apps-in-toss-unity-sdk | Viva Republica, Inc. | 라이선스 파일 없음. 훅 아이디어만 참고하고 문장은 옮기지 않았어요 |
| pbakaus/impeccable | 저장소 LICENSE 기준(저작권자 이름 미표기) | Apache-2.0 |
| leonxlnx/taste-skill | Copyright (c) 2026 Leonxlnx | MIT |
| Nutlope/hallmark | Copyright (c) 2026 Hallmark contributors | MIT |
| heydamir/unslop | Damir Sokolovsky | CC BY 4.0 |
| blader/humanizer | Copyright (c) 2025 Siqi Chen | MIT |
| github/spec-kit | Copyright (c) GitHub, Inc. | MIT |
| garrytan/gstack | Copyright (c) 2026 Garry Tan | MIT |
| EveryInc/compound-engineering-plugin | Copyright (c) 2025 Every | MIT |

humanize-korean(epoko77-ai/im-not-ai)은 코드를 옮기지 않고 설치된 것을 불러 써요.

## 파일별 출처

| 파일 | 출처 |
|---|---|
| `rules/always.md` | obra/superpowers verification-before-completion, cursor/plugins pstack principles. |
| `rules/models.md` | obra/superpowers subagent-driven-development Model Selection. |
| `rules/review-layers.md` | toss/apps-in-toss-harness render-rules, Nutlope/hallmark Floor·Reflex·Finish, obra/superpowers subagent-driven-development. |
| `rules/ui.md` | pbakaus/impeccable craft-floor·modes, Nutlope/hallmark Floor, leonxlnx/taste-skill. |
| `rules/writing-en.md` | blader/humanizer (MIT), based on Wikipedia "Signs of AI writing". |
| `rules/writing-ko.md` | toss/apps-in-toss-harness ux-writing. |
| `skills/build/SKILL.md` | obra/superpowers subagent-driven-development (MIT). |
| `skills/check/SKILL.md` | obra/superpowers verification-before-completion·receiving-code-review, pstack prove-it-works·interrogate, github/spec-kit analyze., obra/superpowers finishing-a-development-branch. |
| `skills/copy/SKILL.md` | toss/apps-in-toss-harness ux-writing (BSD-3). |
| `skills/design/SKILL.md` | pbakaus/impeccable, leonxlnx/taste-skill, Nutlope/hallmark, toss/apps-in-toss-harness design. |
| `skills/design/references/operate-mode.md` | pbakaus/impeccable Operate mode (Apache-2.0), 사용자 대시보드 작업 경험. |
| `skills/diagnose/SKILL.md` | mattpocock/skills diagnosing-bugs (MIT), obra/superpowers systematic-debugging (MIT). |
| `skills/diagnose/references/techniques.md` | obra/superpowers systematic-debugging (root-cause-tracing, defense-in-depth, condition-based-waiting, find-polluter). |
| `skills/docs/SKILL.md` | garrytan/gstack document-generate, document-release (MIT). Diátaxis 분류를 참고했어요. |
| `skills/experiment/SKILL.md` | pstack hillclimb·principle-explain-the-number·benchmark-checklist (MIT). |
| `skills/finish/SKILL.md` | obra/superpowers finishing-a-development-branch. |
| `skills/guard/SKILL.md` | garrytan/gstack careful·guard, toss/apps-in-toss-unity-sdk PreToolUse 훅. |
| `skills/handoff/SKILL.md` | pstack pause-safely·session-pickup·show-me-your-work (MIT), addyosmani/agent-skills documentation-and-adrs (MIT). |
| `skills/plan/SKILL.md` | obra/superpowers writing-plans, toss/es-toolkit pr-review. |
| `skills/research/SKILL.md` | mattpocock/skills research, pstack swarm(각도 나누기). |
| `skills/review/SKILL.md` | garrytan/gstack plan reviews, EveryInc/compound-engineering-plugin, pstack interrogate, toss/apps-in-toss-harness render-rules. |
| `skills/shape/SKILL.md` | mattpocock/skills grill-me, obra/superpowers brainstorming, toss/apps-in-toss-harness plan, pstack in-your-own-words. |
| `skills/shape/references/ideation.md` | toss/apps-in-toss-harness plan/references/ideation.md (BSD-3). |
| `skills/unslop/SKILL.md` | blader/humanizer (MIT), epoko77-ai/im-not-ai(humanize-korean) 호출, toss/apps-in-toss-harness ux-writing. |
| `skills/design/references/anti-slop.md`, `skills/design/references/design-tokens.md` | heydamir/unslop (CC BY 4.0). 절차를 줄이고 jipda design 흐름에 맞게 합쳤어요. |
| `skills/design/references/landing.md` | leonxlnx/taste-skill 2.5.1 (MIT)의 규칙을 키트 없이 쓸 수 있게 줄여 옮겼어요. |
| `skills/revise/SKILL.md` | pstack blast-radius, mattpocock/skills wait-what. |
