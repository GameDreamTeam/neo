import typer
from ai.llm.ollama_client import OllamaClient
from ai.utils.stream import stream_output
from ai.utils.files import read_file
from ai.utils.input import read_stdin


def ask(
    question: str = typer.Argument(...),
    file: str = typer.Option(None, "-f"),
    no_stream: bool = typer.Option(False, "--no-stream"),
):
    client = OllamaClient()

    piped_input = read_stdin()
    if piped_input:
        question += f"\n\nInput:\n{piped_input}"

    if file:
        content = read_file(file)
        question += f"\n\nFile:\n{content}"

    if no_stream:
        output = client.generate(question, no_stream)
        print(output)
    else:
        stream_output(client.generate(question, no_stream))
