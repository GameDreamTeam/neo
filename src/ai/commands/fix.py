import typer
from ai.llm.ollama_client import OllamaClient
from ai.utils.stream import stream_output
from ai.utils.files import read_file
from ai.core.prompt_builder import build_fix_messages


def fix(
    file: str = typer.Argument(...),
    no_stream: bool = typer.Option(False, "--no-stream"),
):

    client = OllamaClient()

    content = read_file(file)
    messages = build_fix_messages(content)

    result = client.chat(messages, no_stream)

    if no_stream:
        print(result)
    else:
        stream_output(result)