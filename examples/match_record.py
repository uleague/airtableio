import sys

sys.path.append("../")

from airtableio import Airtable
import asyncio

TOKEN = ""
APP_ID = ""

my_airtable = Airtable(TOKEN, APP_ID)


async def call_4():
    try:
        result = await my_airtable.get_record_by_field(
            "Users", field_name="captain_discord", field_value="254"
        )
        print(result)
    except Exception:
        raise


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(call_4())

    loop.run_forever()
