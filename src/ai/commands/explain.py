import typer
from ai.llm.ollama_client import OllamaClient
from ai.utils.stream import stream_output
from ai.utils.files import read_file
from ai.core.prompt_builder import build_explain_prompt

def explain(file: str = typer.Option(None, "-f"), no_stream: bool = False):

    client = OllamaClient()

    content = read_file(file)
    prompt = build_explain_prompt(content)

    result = client.generate(prompt, no_stream)

    if no_stream:
        print(result)
    else:
        stream_output(result)
