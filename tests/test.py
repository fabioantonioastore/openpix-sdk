import asyncio

from openpix.utils.http import HTTPClient


async def main() -> None:
    async with HTTPClient(base_url="https://google.com") as http_client:
        print(await http_client.get())


if __name__ == "__main__":
    asyncio.run(main())
