# jipda

[English](README.md) | 한국어

개발과 연구를 같이 하는 사람을 위한 Claude Code 스킬 묶음이에요. 이름은 "짚다"에서 왔어요. 하나씩 짚어 확인하고 나아가요.

- 슬래시 없이 말로 해도 스킬이 뜨고, 구현 흐름의 스킬은 말하지 않아도 작업 시작 전에 떠요. 작은 수정에는 뜨지 않게 설명에 조건을 적었고, 하위 에이전트를 쓰는 `build`와 `review`는 시작 전에 확인받아요.
- 피드백은 두 종류예요. 싼 대조 검사는 자주, 비싼 전문가 검토는 기획 직후와 설계 직후에만 해요.
- 외부 도구 없이 Claude Code만으로 돌아가요. 외부 검사기, 검색기는 `/jipda:setup`으로 원할 때만 켜요.

## 설치

```text
/plugin marketplace add ksone02/jipda
/plugin install jipda@jipda
```

내려받은 저장소로 설치하려면 첫 줄의 `ksone02/jipda` 대신 그 폴더 경로를 넣어요.

### 상시 원칙 (선택, 권장)

스킬을 부르지 않아도 지킬 원칙 7줄을 `~/.claude/CLAUDE.md`에 넣어요. 넣기 전에 [rules/always.md](rules/always.md)를 읽어 보세요.

```sh
python3 scripts/always.py install   # 넣기 (두 번 해도 하나만 남아요)
python3 scripts/always.py remove    # 빼기 (블록 바깥은 그대로)
```

## 스킬

| 스킬 | 하는 일 |
|---|---|
| `shape` | 초안을 먼저 보여 주고, 상황에 맞는 기획·전략 도구를 알아서 적용해 명세로 만들어요 |
| `spec` | 기준이 되는 기능 명세서와 QA 체크리스트를 표로 만들고, 규칙이 바뀌면 영향받는 곳을 보여 줘요 |
| `plan` | 명세를 실행해 볼 수 있는 단계로 나누고 위험한 것부터 배치해요 |
| `build` | 계획대로 구현해요. 작은 계획은 직접, 크거나 위험한 작업만 하위 에이전트로 해요 |
| `revise` | 이미 만든 것의 동작, 구조, 디자인 수정 요청을 여러 개 한 번에 가볍게 처리해요 |
| `check` | 완료 조건을 대조하고 실행으로 증명한 뒤 작업을 닫아요. 크거나 위험한 변경만 독립 검사해요 |
| `review` | 분야 전문가 관점으로 검토해요. 기본 한 명, 되돌리기 어려운 결정만 여러 명이에요 (퀀트, 웹, 데이터 연구) |
| `research` | 조사 계획 → 넓게 → 방향 고르기 → 깊게 → 파일 하나. `--competitive`는 경쟁사·레퍼런스 분석이에요 |
| `experiment` | 지표 하나를 반복 실험으로 올려요. 시도마다 기록하고 남기거나 되돌려요 |
| `handoff` | 멈추기, 이어 가기, 결정 기록 |
| `guard` | 위험한 명령 앞에서 확인을 묻는 훅을 켜고 꺼요 (기본 꺼짐) |
| `diagnose` | 실패하는 확인 장치부터 만드는 버그 진단 |
| `design` | 대시보드·도구·랜딩 화면을 세 폭으로 재며 만들어요 |
| `copy` | 화면 문구를 모아 점검하고 승인한 것만 고쳐요 |
| `setup` | 외부 검사기·검색기, 브라우저 도구, 모델 등급, 상시 원칙을 골라 켜요 |
| `docs` | 코드를 읽고 문서를 쓰거나, 문서와 코드가 어긋난 곳을 고쳐요 |
| `unslop` | 글의 AI 티를 지워요. 한국어 긴 글은 humanize-korean으로 마무리해요 |

부를 때는 `/jipda:<스킬> <인자>`예요. 예: `/jipda:research 파이썬 백테스트 라이브러리 비교`.

## 선택 도구

전부 없어도 돌아가요. `/jipda:setup`으로 켜고, 설정은 `~/.config/jipda/config.json`에 남아요.

| 도구 | 쓰는 곳 | 없으면 |
|---|---|---|
| 외부 검사기(예: `codex`) | `check`, `review` | 내부 하위 에이전트가 독립 조건을 지켜 검사해요 |
| 외부 검색기(예: `aside`) | `research` | 내부 하위 에이전트가 검색해요 |
| `agent-browser` 또는 playwright | `design`, `check`의 화면 측정 | 쓸 수 있는 브라우저 도구로 같은 항목을 재요 |
| taste-skill(랜딩 키트, 약 39MB) | `design --landing` | jipda 내장 랜딩 규칙을 써요 |
| humanize-korean | `unslop` | 그 단계를 건너뛰고 알려 줘요 |

외부로 보내는 파일은 [scripts/safe_files.py](scripts/safe_files.py)가 걸러요. 데이터 폴더, `.env`, 데이터 파일, 큰 파일, 키가 든 파일은 빠져요. 프로젝트 `CLAUDE.md`에 "외부 AI 금지" 같은 문구가 있으면 외부 모델을 쓰지 않아요.

## 개발

```sh
uv sync
uv run pytest                                # 스크립트와 스킬 형식 시험. agent-browser나 playwright가 있으면 화면 측정 시험까지 돌아요
claude --plugin-dir . plugin details jipda   # 스킬 목록과 토큰 비용
```

## 라이선스

MIT. 참고한 저장소와 저작권은 [NOTICE.md](NOTICE.md)에 있어요. `skills/design/references/`의 `anti-slop.md`와 `design-tokens.md`는 CC BY 4.0이에요.
