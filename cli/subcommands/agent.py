"""Typer application for the Soothsayer agent subcommands."""

from pathlib import Path

import typer


agent_app = typer.Typer(help="Soothsayer Agent Commands")


@agent_app.callback()
def agent_cli() -> None:
    """Entry point for agent-related commands."""
    # This function ensures the ``question`` command is exposed as a subcommand
    # so that the CLI is invoked as ``python -m cli.agent question ...``.
    pass


@agent_app.command("question")
def ask_question(
    query: str = typer.Argument(..., help="Your query or question"),
    file: Path = typer.Option(
        ..., exists=True, file_okay=True, readable=True, help="Path to markdown file"
    ),
    test_mode: bool = typer.Option(True, help="Run in test mode (no LLM call)"),
):
    """Ask a question using the Soothsayer Agent."""
    try:
        # Import heavy dependencies lazily so that ``--help`` works even when
        # optional packages are missing.
        from agents.base_flow import run_agent_flow
        from rag.md_loader import load_markdown_chunks

        file_path = str(file.resolve())
        chunks = load_markdown_chunks(file_path=file_path)

        input_data = {
            "query": query,
            "chunks": chunks,
            "test_mode": test_mode,
            "file_path": file_path,
        }

        result = run_agent_flow(input_data)
        if isinstance(result, dict) and "formatted_output" in result:
            typer.secho(result["formatted_output"], fg=typer.colors.GREEN)
        else:
            typer.secho("[No formatted output]", fg=typer.colors.YELLOW)
    except Exception as e:
        typer.secho(f"[ERROR] {e}", fg=typer.colors.RED)


__all__ = ["agent_app"]

