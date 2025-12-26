from src.models.user import User


def test_user_contract(api_client):
    response = api_client.get_user(1)
    assert response.status_code == 200

    data = response.json()

    user = User.model_validate(data)  # valida estructura + tipos
    assert user.id == 1
