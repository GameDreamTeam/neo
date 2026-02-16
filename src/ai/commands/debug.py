import typer
from ai.llm.ollama_client import OllamaClient
from ai.utils.stream import stream_output
from ai.utils.files import read_file
from ai.utils.input import read_stdin

from ai.core.prompt_builder import build_debug_messages

def debug(file: str = typer.Option(None, "-f")):

    client = OllamaClient()

    content = read_stdin()

    if not content and file:
        content = read_file(file)

    messages = build_debug_messages(content)

    stream_output(client.chat(messages, False))
