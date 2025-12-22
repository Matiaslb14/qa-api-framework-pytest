from src.models.post import Post


def test_get_posts_returns_list(api_client):
    response = api_client.get_posts()
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

    # valida contrato del primer elemento
    Post.model_validate(data[0])
