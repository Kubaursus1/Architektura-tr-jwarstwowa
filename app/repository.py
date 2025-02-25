from datetime import datetime

from flask import Response


def find_first_free_id():
    for id in UsersRepository.users_database:
        if UsersRepository.users_database[id] is None:
            return id
    return len(UsersRepository.users_database)


def calculate_age(birth_year):
    current_year = datetime.now().year
    return current_year - birth_year


class UsersRepository:
    users_database = {
        0: {
            "firstName": "John",
            "lastName": "Doe",
            "age": 35,
            "group": "user"
        },
        1: {
            "firstName": "Jane",
            "lastName": "Smith",
            "age": 40,
            "group": "premium"
        },
        2: {
            "firstName": "Robert",
            "lastName": "Brown",
            "age": 50,
            "group": "admin"
        },
        3: {
            "firstName": "Emily",
            "lastName": "Davis",
            "age": 30,
            "group": "user"
        }
    }

    def get_all_users(self) -> list:
        users = []
        for id, user in UsersRepository.users_database.items():
            users.append({
                "id": id,
                "firstName": user["firstName"],
                "lastName": user["lastName"],
                "age": user["age"],
                "group": user["group"]
            })
        return users

    def get_one_user(self, id: int) -> dict:
        user = UsersRepository.users_database[id]
        return {"id": id,
                "firstName": user["firstName"],
                "lastName": user["lastName"],
                "age": user["age"],
                "group": user["group"]}

    def post_user(self, user: dict) -> Response:
        if user["group"] not in ["user", "premium", "admin"]:
            return Response(status=400)
        id = find_first_free_id()
        UsersRepository.users_database[id] = {
            "firstName": user["firstName"],
            "lastName": user["lastName"],
            "age": calculate_age(user["birthYear"]),
            "group": user["group"]
        }
        return Response(status=201)

    def patch_user(self, id: int, user: dict) -> Response:
        if id not in UsersRepository.users_database or UsersRepository.users_database[id] is None:
            return Response(status=404)
        db_user = UsersRepository.users_database[id]
        if "firstName" in user:
            db_user["firstName"] = user["firstName"]
        elif "lastName" in user:
            db_user["lastName"] = user["lastName"]
        elif "birthYear" in user:
            db_user["birthYear"] = user["birthYear"]
        elif "group" in user:
            if user["group"] != "user" or "premium" or "admin":
                return Response(status=400)
            db_user["group"] = user["group"]
        return Response(status=204)

    def delete_user(self, id: int) -> Response:
        if id not in UsersRepository.users_database or UsersRepository.users_database[id] is None:
            return Response(status=404)
        UsersRepository.users_database[id] = None
        return Response(status=204)
