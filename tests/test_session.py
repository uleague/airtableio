import aiohttp
import pytest

from airtableio.client import Client
from . import TOKEN, APP_ID

try:
    from asynctest import CoroutineMock, patch
except ImportError:
    from unittest.mock import AsyncMock as CoroutineMock, patch  # type: ignore


class TestAiohttpSession:
    @pytest.mark.asyncio
    async def test_create_bot(self):
        client = Client(token=TOKEN, app_id=APP_ID)

        assert client._session is None
        assert isinstance(client._connector_init, dict)
        assert all(key in {"limit", "ssl", "loop"} for key in client._connector_init)
        assert isinstance(client._connector_class, type)
        assert issubclass(client._connector_class, aiohttp.TCPConnector)

        assert client._session is None

        assert isinstance(client.session, aiohttp.ClientSession)
        assert client.session == client._session