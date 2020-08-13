import sys

sys.path.append("../")

from airtableio import Airtable
import asyncio

TOKEN = ""
APP_ID = ""

my_airtable = Airtable(TOKEN, APP_ID)

field_obj = {
    "fields": {
        "captain_discord": "API_TEST",
        "participant_name": "API",
        "tournament_id": 111,
        "challonge_id": 123,
    }
}


async def call_3():
    try:
        data = {"records": [field_obj for i in range(11)]}
        result = await my_airtable.create_records("Users", data)
        print(result)
    except Exception:
        raise


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(call_3())

    loop.run_forever()
