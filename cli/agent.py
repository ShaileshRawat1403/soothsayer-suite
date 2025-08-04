"""Command-line wrapper for the Soothsayer agent CLI.

This module simply exposes the agent's Typer application from
``cli.subcommands.agent`` so that it can be invoked as a module via
``python -m cli.agent``.
"""

from cli.subcommands.agent import agent_app as app


if __name__ == "__main__":
    app()

