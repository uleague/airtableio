import sys
sys.path.append('../')

from airtableio import Airtable
import asyncio

TOKEN = ""
APP_ID = ""

my_airtable = Airtable(TOKEN, APP_ID)

async def call():
    result = await my_airtable.get_records("Users")
    print(result)

async def call_2():
    try:
        result = await my_airtable.get_record("Tournaments", "recbiNDRedrp89Bwm")
        print(result)
    except Exception:
        raise

async def call_3():
    try:
        data = {"records": [
                {
                "fields": {
                    "captain_discord": "API_TEST",
                    "participant_name": "API",
                    "tournament_id": 111,
                    "challonge_id": 123
                }
                },
                {
                "fields": {
                    "captain_discord": "API_TEST2",
                    "participant_name": "API2",
                    "tournament_id": 111,
                    "challonge_id": 124
                }
                }
            ]
        }
        result = await my_airtable.create_records("Users", data)
        print(result)
    except Exception:
        raise

if __name__=="__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(call())
    loop.create_task(call_2())
    loop.create_task(call_3())

    loop.run_forever()
