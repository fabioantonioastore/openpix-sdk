from asyncio import run

from openpix import OpenPix


TEST_APP_ID = "Q2xpZW50X0lkX2Y3MGRlMzhmLTRmMzgtNGZiNC05NWMxLTBlNjI0NjM0MTEyZjpDbGllbnRfU2VjcmV0X0VLdWg4U01kdENyeE5KSVpGWWQrVE1zWWtndFhyOXQ5dkJZNXhUSTRTSUk9"

openpix = OpenPix(app_id=TEST_APP_ID)
charge = openpix.charge


async def main() -> None:
    await charge.create(value=1000)
    print(charge)

if __name__ == "__main__":
    run(main())