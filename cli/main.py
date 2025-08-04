# cli/main.py

import typer
from cli.subcommands.agent import agent_app

app = typer.Typer(help="Soothsayer CLI")

# Register the 'agent' group
app.add_typer(agent_app, name="agent")

if __name__ == "__main__":
    app()
