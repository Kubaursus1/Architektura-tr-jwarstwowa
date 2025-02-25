import pytest
from app.main import app
from flask.testing import FlaskClient


@pytest.fixture
def client() -> FlaskClient:
    return app.test_client()


def test_get_all_users_code(client: FlaskClient) -> None:
    response = client.get("/users")
    assert response.status_code == 200


def test_get_one_user_code(client: FlaskClient):
    response = client.get("/users/3")
    assert response.status_code == 200


def test_post_user_code(client: FlaskClient):
    user = {
        "firstName": "aaa",
        "lastName": "bbb",
        "birthYear": 1990,
        "group": "user"
    }
    response = client.post("/users", json=user)
    assert response.status_code == 201


def test_patch_user_code(client: FlaskClient):
    user = {"firstName": "New_name"}
    response = client.patch("/users/1", json=user)
    assert response.status_code == 204


def test_delete_user_code(client: FlaskClient):
    response = client.delete("/users/3")
    assert response.status_code == 204
