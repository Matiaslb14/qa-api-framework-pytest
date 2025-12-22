import pytest
from src.clients.jsonplaceholder_client import JsonPlaceholderClient


@pytest.fixture
def api_client():
    return JsonPlaceholderClient()