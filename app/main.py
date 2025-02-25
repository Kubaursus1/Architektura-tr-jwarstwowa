from flask import Flask, request, Response
from repository import UsersRepository
from controllers import UserController

app = Flask(__name__)


@app.get('/users')
def get_users() -> list:
    controller = UserController(UsersRepository())
    users = controller.get_all_users()
    return users


@app.get('/users/<int:id>')
def get_user(id:int) -> dict:
    controller = UserController(UsersRepository())
    user = controller.get_one_user(id)
    return user


@app.post('/users')
def post_user() -> Response:
    user = request.json
    controller = UserController(UsersRepository())
    user_response = controller.post_user({"firstName": user["firstName"], "lastName": user["lastName"],
                                          "birthYear": user["birthYear"], "group": user["group"]})
    return user_response


@app.patch('/users/<int:id>')
def patch_user(id):
    user = request.json
    controller = UserController(UsersRepository())
    user_response = controller.patch_user(id, user)
    return user_response


@app.delete('/users/<int:id>')
def delete_user(id: int) -> Response:
    controller = UserController(UsersRepository())
    user_response = controller.delete_user(id)
    return user_response


if __name__ == '__main__':
    app.run()
