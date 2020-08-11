import logging
import os
from http import HTTPStatus

import aiohttp

from .exceptions import AirtableAPIError

LOG = logging.getLogger('airtable')

API_URL = "https://api.airtable.com/v0/{app_id}/{table_name}"


async def make_request(session, token, method, app_id, table_name, data=None, **kwargs):
    LOG.debug('Make request: "%s" with data: "%r', method, data)

    url = Methods.api_url(app_id=app_id, table_name=table_name)
    
    req = compose_data(data)
    headers = {
        "Authorization": "Bearer {}".format(token)
    }
    method = method.lower()

    if method == "post":
        try:
            async with session.post(url, data=req, headers=headers **kwargs) as response:
                return await response.json()
        except aiohttp.ClientError as e:
            raise AirtableAPIError(f"aiohttp client throws an error: {e.__class__.__name__}: {e}")
    elif method == "get":
        try:
            async with session.get(url, headers=headers, **kwargs) as response:
                result = await response.json()
                LOG.debug("Got result from get query: {}".format(result))
                return result
        except aiohttp.ClientError as e:
            raise AirtableAPIError(f"aiohttp client throws an error: {e.__class__.__name__}: {e}")
    elif method == "put":
        try:
            async with session.put(url, data=req, headers=headers **kwargs) as response:
                return await response.json()
        except aiohttp.ClientError as e:
            raise AirtableAPIError(f"aiohttp client throws an error: {e.__class__.__name__}: {e}")
    


def compose_data(params=None):
    """
    Prepare request data
    :param params:
    :return:
    """
    data = aiohttp.formdata.FormData(quote_fields=False)
    
    if params:
        for key, value in params.items():
            data.add_field(key, str(value))

    return data


class Methods:

    GET_RECORDS = "get"

    @staticmethod
    def api_url(app_id, table_name):
        """
        Generate API URL with included token and method name
        :param token:
        :param method:
        :return:
        """
        return API_URL.format(app_id=app_id, table_name=table_name)