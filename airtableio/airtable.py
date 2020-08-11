import datetime
import typing

from . import Client, api

class Airtable(Client):
    async def get_fields(self, table_name):
        result = await self.request(api.Methods.GET_RECORDS, table_name=table_name)
        return result