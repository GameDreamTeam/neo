import typer
from ai.commands.ask import ask
from ai.commands.chat import chat
from ai.commands.debug import debug
from ai.commands.fix import fix
from ai.commands.summarize import summarize
from ai.commands.explain import explain

app = typer.Typer()

app.command()(ask)
app.command()(chat)
app.command()(summarize)
app.command()(explain)
app.command()(debug)
app.command()(fix)

if __name__ == "__main__":
    app()
