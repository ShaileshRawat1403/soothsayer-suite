@app.command("question")
def ask_question(
    query: str = typer.Argument(..., help="Your query or question"),
    file: Path = typer.Option(..., exists=True, file_okay=True, readable=True, help="Path to markdown file"),
    test_mode: bool = typer.Option(True, help="Run in test mode (no LLM call)")
):
    """Ask a question using Soothsayer Agent."""
    try:
        file_path = str(file.resolve())
        chunks = load_markdown_chunks(file_path=file_path)

        input_data = {
            "query": query,
            "chunks": chunks,
            "test_mode": test_mode,
            "file_path": file_path
        }

        result = run_agent_flow(input_data)
        if isinstance(result, dict) and "formatted_output" in result:
            typer.secho(result["formatted_output"], fg=typer.colors.GREEN)
        else:
            typer.secho("[No formatted output]", fg=typer.colors.YELLOW)

    except Exception as e:
        typer.secho(f"[ERROR] {e}", fg=typer.colors.RED)
