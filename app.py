from flask import Flask, request, Response
from datetime import datetime

app = Flask(__name__)

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


def find_first_free_id():
    for id in users_database:
        if users_database[id] is None:
            return id
    return len(users_database)


def calculate_age(birth_year):
    current_year = datetime.now().year
    return current_year - birth_year


@app.get('/users')
def get_users():
    return users_database


@app.get('/users/<int:id>')
def get_user(id:int):
    user = users_database[id]
    return {
        "id": id,
        "firstName": user["firstName"],
        "lastName": user["lastName"],
        "age": user["age"],
        "group": user["group"]
    }


@app.post('/users')
def post_user():
    user = request.json
    if user["group"] not in ["user", "premium", "admin"]:
        return Response(status=400)
    id = find_first_free_id()
    users_database[id] = {
        "firstName": user["firstName"],
        "lastName": user["lastName"],
        "age": calculate_age(user["birthYear"]),
        "group": user["group"]
    }
    return Response(status=201)


@app.patch('/users/<int:id>')
def patch_user(id):
    if id not in users_database or users_database[id] is None:
        return Response(status=404)
    user_data = request.json
    user = users_database[id]
    if "firstName" in user_data:
        user["firstName"] = user_data["firstName"]
    elif "lastName" in user_data:
        user["lastName"] = user_data["lastName"]
    elif "birthYear" in user_data:
        user["birthYear"] = user_data["birthYear"]
    elif "group" in user_data:
        if user_data["group"] != "user" or "premium" or "admin":
            return Response(status=400)
        user["group"] = user_data["group"]
    return Response(status=204)


@app.delete('/users/<int:id>')
def delete_user(id):
    if id not in users_database or users_database[id] is None:
        return Response(status=404)
    users_database[id] = None
    return Response(status=204)


if __name__ == '__main__':
    app.run()
