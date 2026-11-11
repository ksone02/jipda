import json
import subprocess
import sys
from pathlib import Path

import pytest

import measure

FIX = Path(__file__).resolve().parent / "fixtures"


def run(page, out):
    if not measure.agent_browser() and measure.load_playwright() is None:
        pytest.skip("no browser tool")
    p = subprocess.run([sys.executable, str(Path(measure.__file__)), str(FIX / page), "--out", str(out)],
                       capture_output=True, text=True, timeout=120)
    assert p.returncode == 0, p.stderr
    return json.loads(p.stdout)


def test_overflow_detected(tmp_path):
    report = run("overflow.html", tmp_path)
    assert "horizontal overflow @390x844" in report["fail"]


def test_clean_page(tmp_path):
    report = run("clean.html", tmp_path)
    assert report["fail"] == []
    assert [v["size"] for v in report["viewports"]] == ["1440x900", "1366x768", "390x844"]
    assert all(Path(v["screenshot"]).exists() for v in report["viewports"])


def test_no_browser_tool_returns_3(monkeypatch, capsys):
    monkeypatch.setattr(measure, "agent_browser", lambda: None)
    monkeypatch.setattr(measure, "load_playwright", lambda: None)
    assert measure.main([str(FIX / "clean.html")]) == 3
    assert "agent-browser" in capsys.readouterr().err
