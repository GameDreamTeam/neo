import typer
from ai.commands.ask import ask
from ai.commands.chat import chat

no_stream = False

app = typer.Typer()

app.command()(ask)
app.command()(chat)

if __name__ == "__main__":
    app()
