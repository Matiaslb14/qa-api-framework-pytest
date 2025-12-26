import pytest
from src.models.user import User
from src.utils.data_loader import load_json


data = load_json("testdata/users.json")
VALID_USER_IDS = data["valid_user_ids"]


@pytest.mark.parametrize("user_id", VALID_USER_IDS)
def test_user_contract_multiple(api_client, user_id):
    response = api_client.get_user(user_id)
    assert response.status_code == 200

    user = User.model_validate(response.json())
    assert user.id == user_id
