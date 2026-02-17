from abc import ABC, abstractmethod
from typing import List, Dict, Generator


class BaseLLMClient(ABC):

    @abstractmethod
    def chat(self, messages: List[Dict], no_stream) -> str | Generator[str, None, None]:
        pass

    @abstractmethod
    def generate(self, prompt: str, no_stream) -> str | Generator[str, None, None]:
        pass
