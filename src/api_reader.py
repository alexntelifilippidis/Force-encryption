from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List
from logger import get_logger

T = TypeVar("T")  # dataclass type for API response

class APIReader(ABC, Generic[T]):
    """Abstract base class for API readers with optional debug logging."""

    def __init__(self, debug: bool = False):
        self.debug = debug
        self.logger = get_logger(self.__class__.__name__, debug=self.debug)
        self.logger.info(f"Initialized APIReader for {self.__class__.__name__}")
        self.logger.debug(f"{self.__class__.__name__} debug logging enabled")

    @property
    @abstractmethod
    def base_url(self) -> str:
        pass

    @property
    @abstractmethod
    def resource(self) -> str:
        pass

    @abstractmethod
    def fetch(self) -> List[T]:
        pass