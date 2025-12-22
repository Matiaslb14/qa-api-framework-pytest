def test_get_user_success(api_client):
    response = api_client.get_user(1)

    assert response.status_code == 200
    data = response.json()

    assert data["id"] == 1
    assert "username" in data
