import pytest

from airtableio import Airtable
from . import TOKEN, APP_ID

pytestmark = pytest.mark.asyncio


@pytest.yield_fixture(name='airtable')
async def bot_fixture(event_loop):
    """ Client fixture """
    _airtable = Airtable(TOKEN, APP_ID, loop=event_loop)
    yield _airtable
    await _airtable.close()

async def test_get_records(airtable: Airtable, event_loop):
    result = await airtable.get_fields(table_name="Users")
    assert isinstance(result, dict) is True