from abc import ABC, abstractmethod
from typing import Any, AsyncIterator


class AbstractHTTPClient(ABC):
    @abstractmethod
    def __init__(self, *, base_url: str = "", headers: dict[str, Any] = None) -> None:
        pass

    @abstractmethod
    async def request(
        self,
        *,
        method: str,
        url: str,
        headers: dict[str, Any] = None,
        json: dict[str, Any] = None,
    ) -> AsyncIterator:
        pass

    @abstractmethod
    async def get(self, *, url: str, headers: dict[str, Any] = None) -> Any:
        pass

    @abstractmethod
    async def post(
        self, *, url: str, headers: dict[str, Any] = None, json: dict[str, Any] = None
    ) -> Any:
        pass

    @abstractmethod
    async def put(
        self, *, url: str, headers: dict[str, Any] = None, json: dict[str, Any] = None
    ) -> Any:
        pass

    @abstractmethod
    async def patch(
        self, *, url: str, headers: dict[str, Any] = None, json: dict[str, Any] = None
    ) -> Any:
        pass

    @abstractmethod
    async def delete(self, *, url: str, headers: dict[str, Any] = None) -> Any:
        pass

    @abstractmethod
    async def stream(
        self,
        *,
        method: str,
        url: str,
        json_path: str,
        headers: dict[str, Any] = None,
        json: dict[str, Any] = None,
    ) -> Any:
        pass

    @abstractmethod
    async def stream_get(
        self, *, url: str, json_path: str, headers: dict[str, Any]
    ) -> Any:
        pass

    @abstractmethod
    async def stream_post(
        self,
        *,
        url: str,
        json_path: str,
        headers: dict[str, Any] = None,
        json: dict[str, Any] = None,
    ) -> Any:
        pass

    @abstractmethod
    async def stream_put(
        self,
        *,
        url: str,
        json_path: str,
        headers: dict[str, Any] = None,
        json: dict[str, Any] = None,
    ) -> Any:
        pass

    @abstractmethod
    async def stream_patch(
        self,
        *,
        url: str,
        json_path: str,
        headers: dict[str, Any] = None,
        json: dict[str, Any] = None,
    ) -> Any:
        pass

    @abstractmethod
    async def stream_delete(
        self, *, url: str, json_path: str, headers: dict[str, Any] = None
    ) -> Any:
        pass

    @abstractmethod
    async def close(self) -> None:
        pass

    @abstractmethod
    async def __aenter__(self) -> "AbstractHTTPClient":
        pass

    @abstractmethod
    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        pass

    def __repr__(self) -> str:
        return f"{self.__name__}()"
