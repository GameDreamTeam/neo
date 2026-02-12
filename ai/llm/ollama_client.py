import time
from typing import List, Dict, Generator
from ollama import chat
from ai.llm.base import BaseLLMClient
from ai.config import load_config


class OllamaClient(BaseLLMClient):

    def __init__(self):
        config = load_config()
        self.model = config["model"]
        self.temperature = config["temperature"]

    def complete(self, messages: List[Dict]) -> str:
        try:
            response = chat(
                model=self.model,
                messages=messages,
                stream=False,
                # options={
                #     "temperature": self.temperature
                # }
            )
            return response["message"]["content"]

        except Exception as e:
            raise RuntimeError(f"Ollama request failed: {e}")

    def stream(self, messages: List[Dict]) -> Generator[str, None, None]:
        try:
            stream = chat(
                model=self.model,
                messages=messages,
                stream=True,
                # options={
                #     "temperature": self.temperature
                # }
            )

            for chunk in stream:
                if "message" in chunk:
                    yield chunk["message"]["content"]

        except Exception as e:
            raise RuntimeError(f"Ollama streaming failed: {e}")
