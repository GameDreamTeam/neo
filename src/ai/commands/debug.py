import typer
from ai.llm.ollama_client import OllamaClient
from ai.utils.stream import stream_output
from ai.utils.files import read_file
from ai.utils.input import read_stdin
from ai.core.prompt_builder import build_debug_messages

def debug(
    file: str = typer.Option(None, "-f"),
    no_stream: bool = typer.Option(False, "--no-stream"),
):

    client = OllamaClient()

    content = read_stdin()

    if not content and file:
        content = read_file(file)

    if not content:
        raise typer.BadParameter("Provide pipe input or -f file")

    messages = build_debug_messages(content)

    result = client.chat(messages, no_stream)

    if no_stream:
        print(result)
    else:
        stream_output(result)