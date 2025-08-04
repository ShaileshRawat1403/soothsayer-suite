import typer
from pathlib import Path
from agents.base_flow import run_agent_flow
from rag.md_loader import load_markdown_chunks

cli_app = typer.Typer(help="Soothsayer Agent Commands")  # 👈 required by main.py

@cli_app.command("ask")
def ask_command(
    query: str = typer.Option(..., help="Your query or question"),
    file: Path = typer.Option(..., exists=True, help="Path to markdown file"),
    test_mode: bool = typer.Option(True, help="Run in test mode (no LLM call)")
):
    """Ask a question using Soothsayer Agent."""
    try:
        chunks = load_markdown_chunks(file_path=str(file))  # ✅ Explicit keyword

        input_data = {
            "query": query,
            "chunks": chunks,
            "test_mode": test_mode
        }

        result = run_agent_flow(input_data)

        # ✅ FIX: This block must be indented under `try`
        if isinstance(result, dict) and "formatted_output" in result:
            typer.secho(result["formatted_output"], fg=typer.colors.GREEN)
        else:
            typer.secho("[No formatted output]", fg=typer.colors.YELLOW)

    except Exception as e:
        typer.secho(f"[ERROR] {str(e)}", fg=typer.colors.RED)
