import typer
from ai.commands.ask import ask
from ai.commands.chat import chat
from ai.commands.summarize import summarize
from ai.commands.explain import explain

no_stream = False

app = typer.Typer()

app.command()(ask)
app.command()(chat)
app.command()(summarize)
app.command()(explain)

if __name__ == "__main__":
    app()
