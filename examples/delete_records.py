import sys

sys.path.append("../")

from airtableio import Airtable
import asyncio

TOKEN = ""
APP_ID = ""

my_airtable = Airtable(TOKEN, APP_ID)


async def call_4():
    try:
        data = {"records": ["recbiNDRedrp89Bwm", "recATHcQE1yQDQwyH"]}
        result = await my_airtable.delete_records("Users", data=data)
        print(result)
    except Exception:
        raise


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(call_4())

    loop.run_forever()
