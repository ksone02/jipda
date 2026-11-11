---
name: setup
description: jipda의 선택 기능을 켜고 꺼요. 외부 검사기·검색기, 브라우저 도구, 모델 등급, 상시 원칙을 묻고 사용자 설정 파일에 저장해요. "jipda 세팅해 줘", "외부 모델 연결해 줘"라고 할 때만 써요. 스킬 사용법 질문이나 프로젝트 설정 이야기에는 쓰지 않아요.
---

# setup

## 목적
아무것도 설정하지 않아도 jipda는 돌아가요. 이 스킬은 쓰고 싶은 사람만 외부 도구와 모델을 연결하게 해 줘요. 설정은 저장소가 아니라 사용자 컴퓨터에 남아서 플러그인을 업데이트해도 유지돼요.

## 입력
- 없음. 이 컴퓨터에 설치된 도구를 직접 찾아요.

## 산출물
- `~/.config/jipda/config.json` (`JIPDA_CONFIG`로 바꿀 수 있어요).
- 선택하면 `~/.claude/CLAUDE.md`의 상시 원칙 블록.

## 실행 순서
1. **지금 상태를 봐요.** `python3 <이 스킬 폴더>/../../scripts/ext.py status`와 `command -v codex aside agent-browser`를 돌려요. 설정 파일이 있으면 읽어서 바꾸지 않은 값은 그대로 둬요.
2. **하나씩 물어요.** 설치된 것을 먼저 보기로 보여 주고, 모두 "안 씀"을 고를 수 있어요.
   - 외부 검사기: `check`와 `review`가 독립 검사에 써요.
   - 외부 검색기: `research`가 넓게 훑을 때 써요.
   - 브라우저 도구: `agent-browser`(권장, Apache-2.0, 여러 운영체제), ego lite(macOS 앱, 앱 소스 비공개), 안 씀. 화면 측정 스크립트는 agent-browser나 playwright가 있어야 돌아요.
   - 모델 등급: 기본값 유지 또는 `light`, `standard`, `strong` 이름 지정.
   - 상시 원칙 설치 여부.
3. **외부 도구를 켜면 알려요.** 코드와 프롬프트가 그 도구로 나간다는 것과 [data-safety.md](../../rules/data-safety.md)의 거르기 규칙을 한 줄로 말해요.
4. **설정을 써요.** 고른 것만 JSON으로 저장해요. `{workdir}`는 허용된 파일 사본만 든 임시 폴더, `{output}`은 답을 쓸 파일, `{prompt}`는 프롬프트예요. `{prompt}`가 없으면 표준 입력으로 줘요.
   ```json
   {
     "checker": {"cmd": ["codex", "exec", "--skip-git-repo-check", "-s", "read-only", "-C", "{workdir}", "-o", "{output}", "-"]},
     "searcher": {"cmd": ["aside", "-m", "<모델 이름>", "{prompt}"]},
     "browser": "agent-browser",
     "models": {"light": "haiku", "standard": "sonnet", "strong": "opus"}
   }
   ```
5. **상시 원칙을 골랐으면** `python3 <이 스킬 폴더>/../../scripts/always.py install`을 돌려요.
6. **확인해요.** `ext.py status`를 다시 돌려 결과를 보여 줘요.

## 하지 않는 것
- 사용자가 고르지 않은 도구 켜기.
- 묻지 않고 도구 설치하기. 설치가 필요하면 명령을 알려 줘요.
- API 키나 토큰을 설정 파일에 쓰기.
- 저장소 안에 개인 설정 쓰기.
