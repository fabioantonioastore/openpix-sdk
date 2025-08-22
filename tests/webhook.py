from test import TEST_APP_ID, run
from openpix import OpenPix
from openpix.utils.enums import WebHookEvents


webhook = OpenPix(app_id=TEST_APP_ID).webhook


async def main():
    response = await webhook.create(
        name="hello",
        event=WebHookEvents.CHARGE_CREATED,
        url="https://church-app-backend-ajbu.onrender.com/webhook",
        authorization=TEST_APP_ID,
        is_active=True
    )
    print(response)


if __name__ == "__main__":
    run(main())