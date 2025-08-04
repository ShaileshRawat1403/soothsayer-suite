codex/update-ask_question-function-output-handling
import typer
from pathlib import Path

from rag.md_loader import load_markdown_chunks

try:
    from agents.base_flow import run_agent_flow
except Exception:  # pragma: no cover - fallback for missing optional deps
    run_agent_flow = None  # type: ignore


app = typer.Typer(help="Agent-related commands")
agent_app = app


@app.command("question")
"""Agent subcommands for the CLI."""

import typer
from pathlib import Path

from agents.base_flow import run_agent_flow
from rag.md_loader import load_markdown_chunks


agent_app = typer.Typer(help="Agent-related commands")


@agent_app.command("question")
main
def ask_question(
    query: str = typer.Argument(..., help="Your query or question"),
    file: Path = typer.Option(
        ..., exists=True, file_okay=True, readable=True, help="Path to markdown file"
    ),
    test_mode: bool = typer.Option(True, help="Run in test mode (no LLM call)"),
):
    """Ask a question using Soothsayer Agent."""
    try:
        file_path = str(file.resolve())
        load_markdown_chunks(file_path=file_path)

        input_data = {
            "query": query,
            "file_path": file_path,
            "test_mode": test_mode,
        }

        result = run_agent_flow(input_data)

        if isinstance(result, dict) and "formatted_output" in result:
            output = result["formatted_output"]
            typer.secho(output, fg=typer.colors.GREEN)
        else:
            output = "[No formatted output]"
            typer.secho(output, fg=typer.colors.YELLOW)

        return output

    except Exception as e:
 codex/update-ask_question-function-output-handling
        error_msg = f"[ERROR] {e}"
        typer.secho(error_msg, fg=typer.colors.RED)
        return error_msg

        typer.secho(f"[ERROR] {e}", fg=typer.colors.RED)


__all__ = ["agent_app"]

main
