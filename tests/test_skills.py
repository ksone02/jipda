"""SKILL.md 형식 검사. 스킬이 0개여도 통과한다."""

import json
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_SECTIONS = ["Purpose", "Input", "Output", "Steps", "Do not"]
MAX_WORDS = 1500
EXPECTED_SKILLS: list[str] = ["shape", "plan", "build", "check", "review", "research", "experiment", "handoff", "guard", "diagnose", "design", "copy", "unslop", "docs", "setup"]


def skill_dirs() -> list[Path]:
    return sorted(p.parent for p in (ROOT / "skills").glob("*/SKILL.md"))


def split_frontmatter(text: str) -> tuple[dict[str, str], str]:
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return {}, text
    try:
        end = lines.index("---", 1)
    except ValueError:
        return {}, text
    meta: dict[str, str] = {}
    key = None
    for line in lines[1:end]:
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if m:
            key, value = m.group(1), m.group(2).strip()
            meta[key] = "" if value in (">", "|", ">-", "|-") else value
        elif key and line.startswith((" ", "\t")):
            meta[key] = (meta[key] + " " + line.strip()).strip()
    return meta, "\n".join(lines[end + 1 :])


def read(d: Path) -> tuple[dict[str, str], str]:
    return split_frontmatter((d / "SKILL.md").read_text(encoding="utf-8"))


def body(name: str) -> str:
    return read(ROOT / "skills" / name)[1]


SKILLS = skill_dirs()
ids = [d.name for d in SKILLS]


@pytest.mark.parametrize("d", SKILLS, ids=ids)
def test_frontmatter(d):
    meta, _ = read(d)
    assert meta.get("name") == d.name
    assert meta.get("description")
    assert "disable-model-invocation" not in meta


@pytest.mark.parametrize("d", SKILLS, ids=ids)
def test_sections_in_order(d):
    _, text = read(d)
    heads = [h.strip() for h in re.findall(r"^## (.+)$", text, re.M)]
    found = [h for h in heads if h in REQUIRED_SECTIONS]
    assert found == REQUIRED_SECTIONS


@pytest.mark.parametrize("d", SKILLS, ids=ids)
def test_length(d):
    _, text = read(d)
    assert len(text.split()) <= MAX_WORDS


@pytest.mark.parametrize("d", SKILLS, ids=ids)
def test_links_resolve(d):
    _, text = read(d)
    for target in re.findall(r"\]\(([^)\s]+)\)", text):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        path = target.split("#")[0]
        assert (d / path).resolve().exists(), f"{d.name}: broken link {target}"


@pytest.mark.parametrize("d", SKILLS, ids=ids)
def test_subagent_model_named(d):
    _, text = read(d)
    for para in re.split(r"\n\s*\n", text):
        if "subagent" in para.lower():
            assert re.search(r"light|standard|strong|rules/models\.md", para), para[:80]


@pytest.mark.parametrize("d", SKILLS, ids=ids)
def test_description_says_when_not_to_trigger(d):
    assert "Do not use" in read(d)[0]["description"]


@pytest.mark.parametrize("name", ["build", "review"])
def test_costly_skills_confirm_first(name):
    head = body(name).split("## Steps")[1].split("1. ")[0]
    assert "confirmation" in head


@pytest.mark.parametrize("name", ["plan", "build", "design", "check", "research"])
def test_flow_skills_trigger_on_the_work_not_the_words(name):
    d = read(ROOT / "skills" / name)[0]["description"]
    assert "even if the user did not ask" in d or "without being asked" in d


def test_expected_skills_present():
    assert set(EXPECTED_SKILLS) <= {d.name for d in SKILLS}


def test_plugin_manifest():
    plugin = json.loads((ROOT / ".claude-plugin/plugin.json").read_text())
    market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
    assert plugin["name"] == "jipda"
    assert market["plugins"][0]["source"] == "./"


# --- 스킬별 내용 검사 (Task 9~12) ---


def test_check_fallback_phrase():
    assert "External checker unavailable, verified internally" in body("check")


def test_build_statuses():
    b = body("build")
    assert all(s in b for s in ("done", "concerned", "blocked", "needs context"))


def test_build_retry_cap():
    assert "3 fix rounds" in body("build")


def test_shape_done_format():
    assert re.search(r"D\d+\. .+ — ", body("shape"))


def test_roles_format():
    roles = sorted((ROOT / "skills/review/references/roles").glob("*.md"))
    assert [r.stem for r in roles] == ["data-research", "quant", "web"]
    for r in roles:
        t = r.read_text(encoding="utf-8")
        heads = len(re.findall(r"^## ", t, re.M))
        assert heads >= 3 and t.count("Must check:") == heads, r.name


def test_experiment_tsv_header():
    header = "id\thypothesis\tchange\tbefore\tafter\tdelta\ttests\tverdict\tnote"
    log = (ROOT / "skills/experiment/references/decision-log.md").read_text(encoding="utf-8")
    assert header in body("experiment") or header in log


def test_research_fallback_phrase():
    assert "External searcher unavailable, researched internally" in body("research")


def test_design_viewports():
    b = body("design")
    assert all(s in b for s in ("1440x900", "1366x768", "390x844", "at most 3 times"))


def test_design_landing_delegates():
    assert "references/landing.md" in body("design") and "taste-skill:design-taste-frontend" in body("design")


def test_unslop_calls_humanize():
    assert "humanize-korean:humanize-korean" in body("unslop")


def test_copy_table_header():
    assert "Screen | Location (file:line) | Original | Proposed | What changed" in body("copy")


def test_docs_modes_and_verification():
    b = body("docs")
    assert all(s in b for s in ("--audit", "Reference", "How-to", "Explanation", "Tutorial", "not run", "writing-ko.md"))


def test_handoff_sections():
    b = body("handoff")
    for s in ("## Goal", "## In progress", "## Verified", "## Current state", "## Next", "## Key files", "## Decisions"):
        assert s in b or s.replace("## ", "") in b


def test_guard_state_path():
    assert "jipda-guard.on" in body("guard")


def test_ext_calls_have_bash_timeout():
    models = (ROOT / "rules/models.md").read_text(encoding="utf-8")
    assert "--timeout 540" in models and "600000" in models
    for name in ("check", "research", "review"):
        assert "Calling external models" in body(name), name


def test_review_uses_skill_relative_ext():
    b = body("review")
    assert "`ext.py checker`" in b and "External checker unavailable, verified internally" in b


def test_scratch_inside_git_dir():
    for name in ("build", "check"):
        assert ".git/jipda" in body(name) and ".jipda/" not in body(name).replace(".git/jipda/", ""), name


def test_build_direct_by_default():
    b = body("build")
    assert "main session doing it directly" in b and "independent tasks" in b and "review-all.diff" in b
    assert "always gets one final review" in b and "never defer it to `check`" in b and "real money or production data" in b


def test_review_one_reviewer_by_default():
    assert "one reviewer by default" in body("review")


def test_check_independent_only_when_big_or_risky():
    b = body("check")
    assert "only when large or risky" in b and "Checker: direct comparison" in b and "git diff --numstat" in b


def test_no_vendor_model_or_tool_names_in_skills():
    for d in SKILLS:
        if d.name == "setup":
            continue
        for f in d.rglob("*.md"):
            low = f.read_text(encoding="utf-8").lower()
            for word in ("haiku", "sonnet", "opus", "deepseek", "aside", "codex", "playwright"):
                assert word not in low, f"{f}: {word}"


def test_setup_keeps_config_outside_repo():
    b = body("setup")
    assert "~/.config/jipda/config.json" in b and "agent-browser" in b


@pytest.mark.parametrize("d", SKILLS, ids=ids)
def test_replies_in_users_language(d):
    assert "user's language" in read(d)[1]


@pytest.mark.parametrize("d", SKILLS, ids=ids)
def test_body_is_english(d):
    allowed = {"unslop", "copy"}  # 한국어 규칙 파일의 절 이름을 가리키는 스킬
    if d.name not in allowed:
        assert not re.search(r"[가-힣]", read(d)[1]), d.name
