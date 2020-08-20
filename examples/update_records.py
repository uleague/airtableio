import sys

sys.path.append("../")

from airtableio import Airtable
import asyncio

TOKEN = ""
APP_ID = ""

my_airtable = Airtable(TOKEN, APP_ID)

field_obj = {
        "status": "finished"
    }


async def call_5():
    try:
        record = await my_airtable.get_record_by_field('Tournaments', 'tournament_name', 'das')
        record_id = record['records'][0]['id']
        result = await my_airtable.update_records('Tournaments', {'records': [{"id": record_id, "fields": field_obj}]})
        print(result)
    except Exception:
        raise


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(call_5())

    loop.run_forever()
