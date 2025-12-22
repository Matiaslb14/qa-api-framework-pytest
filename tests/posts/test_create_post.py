from src.models.post import Post


def test_create_post_success(api_client):
    payload = {
        "userId": 1,
        "title": "QA API Framework",
        "body": "Creating a post via automated test"
    }

    response = api_client.create_post(payload)
    assert response.status_code == 201

    data = response.json()

    # JSONPlaceholder suele devolver un id (ej: 101)
    assert "id" in data

    Post.model_validate(data)
