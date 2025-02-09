import pytest
from app import app


@pytest.fixture
def client():
    return app.test_client()


def test_get_all_users_code(client):
    response = client.get("/users")
    assert response.status_code == 200


def test_get_one_user_code(client):
    response = client.get("/users/3")
    assert response.status_code == 200


def test_post_user_code(client):
    user = {
        "firstName": "aaa",
        "lastName": "bbb",
        "birthYear": 1990,
        "group": "user"
    }
    response = client.post("/users", json=user)
    assert response.status_code == 201


def test_patch_user_code(client):
    user = {"firstName": "New_name"}
    response = client.patch("/users/1", json=user)
    assert response.status_code == 204


def test_delete_user_code(client):
    response = client.delete("/users/3")
    assert response.status_code == 204
