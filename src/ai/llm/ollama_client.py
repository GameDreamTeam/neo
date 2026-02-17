from typing import List, Dict, Generator
from ollama import chat, generate
from ai.llm.base import BaseLLMClient
from ai.config import load_config


class OllamaClient(BaseLLMClient):

    def __init__(self):
        config = load_config()
        self.model = config["model"]
        self.temperature = config["temperature"]

    def chat(self, messages, no_stream):

        try:
            should_stream = not no_stream

            response = chat(
                model=self.model,
                messages=messages,
                stream=should_stream,
                options={
                    "temperature": self.temperature
                }
            )

            if should_stream:

                def generator():
                    for chunk in response:
                        if "message" in chunk:
                            yield chunk["message"]["content"]

                return generator()

            return response["message"]["content"]

        except Exception as e:
            raise RuntimeError(f"Ollama request failed: {e}")


    def generate(self, prompt: str, no_stream):

        try:
            should_stream = not no_stream

            response = generate(
                model=self.model,
                prompt=prompt,
                stream=should_stream,
                options={
                    "temperature": self.temperature
                }
            )

            # STREAM MODE
            if should_stream:

                def generator():
                    for chunk in response:
                        if "response" in chunk:
                            yield chunk["response"]

                return generator()

            # NON-STREAM MODE
            return response["response"]

        except Exception as e:
            raise RuntimeError(f"Ollama request failed: {e}")

