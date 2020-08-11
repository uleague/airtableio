from airtableio import Airtable

TOKEN = ""
APP_ID = ""

my_airtable = Airtable(TOKEN, APP_ID)

try:
    result = my_airtable.get_fields("Users")
    print(result)
except Exception:
    raise

