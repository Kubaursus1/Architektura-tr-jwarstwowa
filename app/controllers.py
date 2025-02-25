from flask import Response

from repository import UsersRepository


class UserController:
    def __init__(self, repository: UsersRepository) -> None:
        self.repository = repository

    def get_all_users(self) -> list:
        return self.repository.get_all_users()

    def get_one_user(self, user_id: int) -> dict:
        return self.repository.get_one_user(user_id)

    def post_user(self, user: dict) -> Response:
        return self.repository.post_user(user)

    def patch_user(self, user_id: int, user: dict) -> Response:
        return self.repository.patch_user(user_id, user)

    def delete_user(self, id: int) -> Response:
        return self.repository.delete_user(id)


