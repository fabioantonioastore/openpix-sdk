import os
from asyncio import run

from dotenv import load_dotenv

from openpix import OpenPix

load_dotenv()
TEST_APP_ID = os.getenv("TEST_APP_ID")

openpix = OpenPix(app_id=TEST_APP_ID)
charge = openpix.charge


async def main() -> None:
    pass

if __name__ == "__main__":
    run(main())