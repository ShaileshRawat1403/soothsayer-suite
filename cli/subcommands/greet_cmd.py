import typer

app = typer.Typer(help="Greeting commands")

@app.command("hello")
def hello(name: str = typer.Option(..., "--name", "-n", help="Your name")):
    """Say hello to someone."""
    print(f"Hello, {name}!")
