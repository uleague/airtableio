import pytest

from airtableio import Airtable
from . import TOKEN, APP_ID

pytestmark = pytest.mark.asyncio

@pytest.yield_fixture(name='airtable')
async def airtable_fixture(event_loop):
    """ Client fixture """
    _airtable = Airtable(TOKEN, APP_ID, loop=event_loop)
    yield _airtable
    await _airtable.close()

async def test_airtable_get_records(airtable: Airtable, event_loop):
    result = await airtable.get_records(table_name="Users")
    assert isinstance(result, dict) is True

async def test_airtable_get_record(airtable: Airtable, event_loop):
    result = await airtable.get_record(table_name="Users", record_id="appr0UwxHpgfeIC4z")
    assert isinstance(result, dict) is True

# async def test_airtable_create_records(airtable: Airtable, event_loop):
#     result = await airtable.get_record(table_name="Users", record_id="appr0UwxHpgfeIC4z")
#     assert isinstance(result, dict) is True