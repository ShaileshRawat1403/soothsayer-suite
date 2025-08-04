from pathlib import Path

import cli.subcommands.agent as agent_module


def test_ask_question_returns_output_and_passes_test_mode(monkeypatch):
    captured = {}

    def fake_run_agent_flow(data):
        captured["data"] = data
        return {"formatted_output": "### answer\n[TEST MODE] example"}

    monkeypatch.setattr(agent_module, "run_agent_flow", fake_run_agent_flow)

    result = agent_module.ask_question("What?", Path("docs/sample.md"), test_mode=True)

    assert "[TEST MODE]" in result
    assert captured["data"]["test_mode"] is True


def test_ask_question_handles_missing_output(monkeypatch):
    def fake_run_agent_flow(data):
        return {}

    monkeypatch.setattr(agent_module, "run_agent_flow", fake_run_agent_flow)

    result = agent_module.ask_question("What?", Path("docs/sample.md"), test_mode=True)

    assert result == "[No formatted output]"
