from abc import ABC, abstractmethod
from typing import List, Dict, Generator


class BaseLLMClient(ABC):

    @abstractmethod
    def complete(self, messages: List[Dict]) -> str:
        pass

    @abstractmethod
    def stream(self, messages: List[Dict]) -> Generator[str, None, None]:
        pass
