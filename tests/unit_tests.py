import pytest
from app import app, users_database, calculate_age, get_users, get_user, post_user, patch_user, delete_user


def test_get_all_users():
    assert get_users() == users_database


def test_get_one_user():
    id = 2
    assert get_user(id) == {"id": id,
                            "firstName": users_database[id]["firstName"],
                            "lastName": users_database[id]["lastName"],
                            "age": users_database[id]["age"],
                            "group": users_database[id]["group"]}


def test_post_user():
    user = {
        "firstName": "Kuba",
        "lastName": "Niczyporuk",
        "birthYear": 2009,
        "group": "user"
    }
    with app.test_request_context(json=user):
        post_user()
    assert any(u["firstName"] == "Kuba" and u["lastName"] == "Niczyporuk" and u["group"] == "user" for u in users_database.values() if u is not None)


def test_patch_user():
    id = 2
    user_data = {"firstName": "New_name"}
    with app.test_request_context(json=user_data):
        patch_user(id)
    assert users_database[id]["firstName"] == "New_name"


def test_delete_user():
    id = 1
    delete_user(id)
    assert users_database[id] is None
