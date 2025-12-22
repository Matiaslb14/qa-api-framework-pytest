import pytest


@pytest.mark.skip(reason="JSONPlaceholder does not support real user creation")
def test_create_user_not_supported(api_client):
    pass
