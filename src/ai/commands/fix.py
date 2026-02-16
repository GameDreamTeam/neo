from ai.llm.ollama_client import OllamaClient
from ai.utils.files import read_file
from ai.utils.stream import stream_output
from ai.core.prompt_builder import build_fix_messages

def fix(file: str):

    client = OllamaClient()

    content = read_file(file)

    messages = build_fix_messages(content)

    stream_output(client.chat(messages, False))

