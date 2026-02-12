import typer
from ai.commands.ask import ask

app = typer.Typer()

app.command()(ask)

if __name__ == "__main__":
    app()
