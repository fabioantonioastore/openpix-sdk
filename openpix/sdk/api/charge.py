import uuid
from datetime import date
from typing import Any, AsyncIterator

from . import API
from openpix.utils.http import HTTPClient


class ChargeAPI(API):
    def __init__(self, *, url: str, headers: dict[str, Any]) -> None:
        super().__init__(url=url, headers=headers)

    async def get_image_qr_code(self, *, correlation_id: str, size: int = 1024) -> str:
        async with HTTPClient(base_url=self._url, headers=self._headers) as http_client:
            endpoint = f"charge/brcode/image/{correlation_id}?size={size}"
            return await http_client.get(url=endpoint, headers=self._headers)


    async def get_encoded_qr_code(self, *, encode: str = "base64", correlation_id: str, size: int = 1024) -> dict[str, Any]:
        async with HTTPClient(base_url=self._url, headers=self._headers) as http_client:
            endpoint = f"charge/brcode/image/{correlation_id}?size={size}"
            return await http_client.get(url=endpoint, headers=self._headers)

    async def delete(self, *, correlation_id: str) -> dict[str, Any]:
        async with HTTPClient(base_url=self._url, headers=self._headers) as http_client:
            endpoint = f"charge/{correlation_id}"
            return await http_client.delete(url=endpoint, headers=self._headers)

    async def edit_expiration_date(self, *, correlation_id: str, expires_date: str | date) -> dict[str, Any]:
        if isinstance(expires_date, date):
            expires_date = str(expires_date)
        async with HTTPClient(base_url=self._url, headers=self._headers) as http_client:
            endpoint = f"charge/{correlation_id}"
            payload = {
                "expiresDate": expires_date
            }
            return await http_client.patch(url=endpoint, headers=self._headers, json=payload)

    async def get(self, *, correlation_id: str) -> dict[str, Any]:
        async with HTTPClient(base_url=self._url, headers=self._headers) as http_client:
            endpoint = f"charge/{correlation_id}"
            response = await  http_client.get(url=endpoint, headers=self._headers)
            return response["charge"]

    async def get_list(self, *, start: str, end: str, status: str, customer_correlation_id: str, subscription_correlation_id) -> list[dict[str, Any]]:
        async with HTTPClient(base_url=self._url, headers=self._headers) as http_client:
            endpoint = "charge?"
            if start:
                endpoint += f"start={start}&"
            if end:
                endpoint += f"end={end}&"
            if status:
                endpoint += f"status={status}&"
            if customer_correlation_id:
                endpoint += f"customer={customer_correlation_id}&"
            if subscription_correlation_id:
                endpoint += f"subscription={subscription_correlation_id}&"

            response = await http_client.get(url=endpoint, headers=self._headers)
            return response["charge"]

    async def stream_get_list(self, *, start: str, end: str, customer_correlation_id: str, subscription_correlation_id: str) -> AsyncIterator:
        async with HTTPClient(base_url=self._url, headers=self._headers) as http_client:
            endpoint = "charge?"
            if start:
                endpoint += f"start={start}&"
            if end:
                endpoint += f"end={end}&"
            if customer_correlation_id:
                endpoint += f"customer={customer_correlation_id}&"
            if subscription_correlation_id:
                endpoint += f"subscription={subscription_correlation_id}&"

            yield http_client.stream_get(url=endpoint, headers=self._headers, json_path="charge")

    async def create(self, *, value: int, return_existing: bool = True) -> dict[str, Any]:
        async with HTTPClient(base_url=self._url, headers=self._headers) as http_client:
            endpoint = f"charge?return_existing={return_existing}"
            payload = {
                "value": value,
                "correlationID": str(uuid.uuid4()),
            }
            print(payload)
            response = await http_client.post(url=endpoint, headers=self._headers, json=payload)
            return response["charge"]

    async def get_refund(self, *, correlation_id: str) -> list[dict[str, Any]]:
        async with HTTPClient(base_url=self._url, headers=self._headers) as http_client:
            endpoint = f"charge/{correlation_id}/refund"
            return await http_client.get(url=endpoint, headers=self._headers)

    async def stream_get_refund(self, *, correlation_id: str) -> AsyncIterator:
        async with HTTPClient(base_url=self._url, headers=self._headers) as http_client:
            endpoint = f"charge/{correlation_id}/refund"
            yield http_client.get(url=endpoint, headers=self._headers)