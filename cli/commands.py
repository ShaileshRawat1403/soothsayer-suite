import typer
from pathlib import Path
from agents.base_flow import run_agent_flow
from rag.md_loader import load_markdown_chunks

cli_app = typer.Typer(help="Soothsayer CLI – Modular Agent Commands")

@cli_app.command("ask")
def ask_command(
    query: str = typer.Option(..., help="Your query or question"),
    file: Path = typer.Option(..., exists=True, help="Path to markdown file"),
    test_mode: bool = typer.Option(True, help="Run in test mode (no LLM call)")
):
    """Ask a question using Soothsayer Agent."""
    try:
        chunks = load_markdown_chunks(file_path=str(file))
        input_data = {
            "query": query,
            "chunks": chunks,
            "test_mode": test_mode
        }
        result = run_agent_flow(input_data)
        typer.echo(result)
    except Exception as e:
        typer.secho(f"[ERROR] {str(e)}", fg=typer.colors.RED)
