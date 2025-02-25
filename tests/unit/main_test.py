from flask import Flask

from app.main import app, get_users, get_user, post_user, patch_user, delete_user
from repository import UsersRepository


def test_flask_app_is_flask_instance() -> None:
    assert isinstance(app, Flask)


def test_get_all_users() -> None:
    assert get_users() == [{"id": id,
                            "firstName": user["firstName"],
                            "lastName": user["lastName"],
                            "age": user["age"],
                            "group": user["group"]} for id, user in UsersRepository.users_database.items()]


def test_get_one_user():
    id = 2
    assert get_user(id) == {"id": id,
                            "firstName": UsersRepository.users_database[id]["firstName"],
                            "lastName": UsersRepository.users_database[id]["lastName"],
                            "age": UsersRepository.users_database[id]["age"],
                            "group": UsersRepository.users_database[id]["group"]}


def test_post_user():
    user = {
        "firstName": "Kuba",
        "lastName": "Niczyporuk",
        "birthYear": 2009,
        "group": "admin"
    }
    with app.test_request_context(json=user):
        post_user()
    assert any(u["firstName"] == "Kuba" and u["lastName"] == "Niczyporuk" and u["group"] == "admin" for u in
               UsersRepository.users_database.values() if u is not None)


def test_patch_user():
    id = 2
    user_data = {"firstName": "New_name"}
    with app.test_request_context(json=user_data):
        patch_user(id)
    assert any(user_data[k] == UsersRepository.users_database[id][k] for k in user_data.keys() if k is not None)


def test_delete_user():
    id = 1
    delete_user(id)
    assert UsersRepository.users_database[id] is None
