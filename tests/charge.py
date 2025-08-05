from asyncio import run

from openpix import OpenPix
from test import TEST_APP_ID
from openpix.entities import Customer


charge = OpenPix(app_id=TEST_APP_ID).charge
customer = Customer(
    name="John Doe",
    email="johndoe@gmail.com"
)


async def main():
    response = await charge.create(value=1000, customer=customer)
    correlation_id = response["correlationID"]
    print(response)
    response = await charge.get(correlation_id=correlation_id)
    print(response)


if __name__ == "__main__":
    run(main())