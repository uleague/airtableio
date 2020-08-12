import datetime
from typing import Text, Dict

from . import Client, api

class Airtable(Client):
    """
    Main class for interacting with Airtable API.

    :param Client: :class: Client
    """
    async def get_records(self, table_name: Text) -> Dict:
        """
        Method to List Table records.

        :param table_name: Text
        :return: Records 
        :rtype: Dict
        """
        result = await self.request(api.Methods.GET_RECORDS, table_name=table_name)
        return result
    
    async def get_record(self, table_name: Text, record_id: Text) -> Dict:
        """
        Method to Retrieve a Table record.

        :param table_name: Text
        :param record_id: Text
        :return: Record
        :rtype: Dict
        """
        result = await self.request(api.Methods.GET_RECORD, table_name=table_name, record_id=record_id)
        return result
    
    async def create_records(self, table_name: Text, data: Dict) -> Dict:
        """
        Method to Create Teable records.

        :param data: Dict
        :return: Inserted records
        :rtype: Dict
        """
        result = await self.request(api.Methods.CREATE_RECORDS, table_name=table_name, data=data)
        return result