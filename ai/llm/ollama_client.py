from typing import List, Dict, Generator
from ollama import chat, generate
from ai.llm.base import BaseLLMClient
from ai.config import load_config


class OllamaClient(BaseLLMClient):

    def __init__(self):
        config = load_config()
        self.model = config["model"]
        self.temperature = config["temperature"]

    def chat(self, messages: List[Dict], no_stream) -> str | Generator[str, None, None]:
        try:
            print("hello")
            shouldStream = not no_stream
            response = chat(
                model=self.model,
                messages=messages,
                stream=shouldStream,
                # options={
                #     "temperature": self.temperature
                # }
            )
            if shouldStream:
                for chunk in response:
                  if "message" in chunk:
                    yield chunk["message"]["content"]
            else: return response["message"]["content"]

        except Exception as e:
            raise RuntimeError(f"Ollama request failed: {e}")

    def generate(self, prompt: str, no_stream) -> str | Generator[str, None, None]:
        try:
            shouldStream = not no_stream
            response = generate(
                model=self.model,
                prompt=prompt,
                stream=shouldStream,
                # options={
                #     "temperature": self.temperature
                # }
            )
            if shouldStream:
                for chunk in response:
                    print(chunk["response"])
            else: return response["response"]

        except Exception as e:
            raise RuntimeError(f"Ollama request failed: {e}")
