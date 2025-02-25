from app.repository import UsersRepository


def test_get_all_users_repository() -> None:
    users = UsersRepository().get_all_users()
    assert users == [{"id": id,
                      "firstName": user["firstName"],
                      "lastName": user["lastName"],
                      "age": user["age"],
                      "group": user["group"]} for id, user in UsersRepository.users_database.items()]


def test_get_one_user_repository() -> None:
    user_id = 2
    user = UsersRepository().get_one_user(user_id)
    assert user == {"id": user_id,
                    "firstName": UsersRepository.users_database[user_id]["firstName"],
                    "lastName": UsersRepository.users_database[user_id]["lastName"],
                    "age": UsersRepository.users_database[user_id]["age"],
                    "group": UsersRepository.users_database[user_id]["group"]}


def test_post_user() -> None:
    user = {
        "firstName": "aaa",
        "lastName": "bbb",
        "birthYear": 1990,
        "group": "user"
    }
    UsersRepository().post_user(user)
    assert any(u["firstName"] == "aaa" and u["lastName"] == "bbb" and u["group"] == "user"
               for u in UsersRepository.users_database.values() if u is not None)


def test_patch_user() -> None:
    user_id = 0
    user = {"firstName": "Kuba", "group": "admin"}
    UsersRepository().patch_user(user_id, user)
    assert any(user[k] == UsersRepository.users_database[user_id][k] for k in user.keys() if k is not None)


def test_delete_user() -> None:
    user_id = 1
    UsersRepository().delete_user(user_id)
    assert UsersRepository.users_database[user_id] is None
