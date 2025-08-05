from typing import Any, AsyncIterator

from .api import API
from openpix.utils.enums import WebHookEvents
from openpix.utils.http import HTTPClient


class WebHookAPI(API):
    def __init__(self, *, url: str, headers: dict[str, Any]) -> None:
        super().__init__(url=url, headers=headers)

    async def create(self, *, name: str, event: WebHookEvents, url: str, authorization: str, is_active: bool) -> dict[str, Any]:
        async with HTTPClient(base_url=self._url, headers=self._headers) as http_client:
            endpoint = "webhook"
            payload = {
                "name": name,
                "event": event,
                "url": url,
                "authorization": authorization,
                "isActive": is_active
            }
            return await http_client.post(url=endpoint, json=payload)

    async def delete(self, *, webhook_id: str) -> dict[str, Any]:
        async with HTTPClient(base_url=self._url, headers=self._headers) as http_client:
            endpoint = f"webhook/{webhook_id}"
            return await http_client.delete(url=endpoint)

    async def get_list(self, *, url: str) -> list[dict[str, Any]]:
        async with HTTPClient(base_url=self._url, headers=self._headers) as http_client:
            endpoint = f"webhook/{url}"
            return await http_client.get(url=endpoint)

    async def stream_get_list(self, *, url: str) -> AsyncIterator:
        async with HTTPClient(base_url=self._url, headers=self._headers) as http_client:
            endpoint = f"webhook/{url}"
            yield http_client.get(url=endpoint)

    async def get_ip_list(self) -> list[dict[str, Any]]:
        async with HTTPClient(base_url=self._url, headers=self._headers) as http_client:
            endpoint = f"webhook/ips"
            return await http_client.get(url=endpoint)

    async def stream_get_ip_list(self) -> AsyncIterator:
        async with HTTPClient(base_url=self._url, headers=self._headers) as http_client:
            endpoint = "webhook/ips"
            yield http_client.get(url=endpoint)
