import typer
from ai.llm.ollama_client import OllamaClient
from ai.utils.stream import stream_output
from ai.utils.files import read_file
from ai.core.prompt_builder import build_summarize_prompt

def summarize(
    file: str = typer.Option(..., "-f"),
    no_stream: bool = typer.Option(False, "--no-stream"),
):

    client = OllamaClient()

    content = read_file(file)
    prompt = build_summarize_prompt(content)

    result = client.generate(prompt, no_stream)

    if no_stream:
        print(result)
    else:
        stream_output(result)