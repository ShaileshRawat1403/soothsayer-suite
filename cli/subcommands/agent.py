"""Typer application for the Soothsayer agent subcommands."""

from pathlib import Path
import typer

# Create Typer application for agent commands
agent_app = typer.Typer(help="Soothsayer Agent Commands")


@agent_app.callback()
def agent_cli() -> None:
    """Entry point for agent-related commands."""
    # The callback ensures that ``question`` is exposed as a subcommand so that
    # the CLI can be invoked as ``python -m cli.agent question ...``.
    return


@agent_app.command("question")
def ask_question(
    file: Path = typer.Option(
        ..., "--file", "-f", exists=True, file_okay=True, readable=True,
        help="Path to markdown file",
    ),
    test_mode: bool = typer.Option(
        True, "--test-mode", help="Run in test mode (no LLM call)",
    ),
    query: str = typer.Argument(..., help="Your query or question"),
) -> str:
    """Ask a question using the Soothsayer Agent."""
    try:
        # Import heavy dependencies lazily so that ``--help`` works even when
        # optional packages are missing.
        from rag.md_loader import load_markdown_chunks
        from agents.base_flow import run_agent_flow

        file_path = file.resolve()
        load_markdown_chunks(file_path=str(file_path))

        input_data = {
            "query": query,
            "file_path": str(file_path),
            "test_mode": test_mode,
        }

        result = run_agent_flow(input_data)
        output = (
            result.get("formatted_output")
            if isinstance(result, dict)
            else None
        )
        if output:
            typer.secho(output, fg=typer.colors.GREEN)
        else:
            output = "[No formatted output]"
            typer.secho(output, fg=typer.colors.YELLOW)
        return output
    except Exception as exc:  # pragma: no cover - handle runtime errors
        error_msg = f"[ERROR] {exc}"
        typer.secho(error_msg, fg=typer.colors.RED)
        return error_msg


__all__ = ["agent_app"]
