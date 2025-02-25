from unittest.mock import Mock, call

from _pytest.fixtures import fixture

from app.controllers import UserController
from app.repository import UsersRepository


@fixture
def repository() -> Mock:
    return Mock(UsersRepository)


@fixture
def controller(repository: Mock) -> UserController:
    return UserController(repository=repository)


def test_get_all_users_controller(controller: UserController, repository: Mock) -> None:
    controller.get_all_users()
    expected = call()
    assert expected in repository.get_all_users.mock_calls


def test_get_one_user_controller(controller: UserController, repository: Mock) -> None:
    user_id = 3
    controller.get_one_user(user_id)
    expected = call(user_id)
    assert expected in repository.get_one_user.mock_calls


def test_post_user(controller: UserController, repository: Mock) -> None:
    user = {
        "firstName": "aaa",
        "lastName": "bbb",
        "birthYear": 1990,
        "group": "user"
    }
    controller.post_user(user)
    expected = call(user)
    assert expected in repository.post_user.mock_calls


def test_patch_user(controller: UserController, repository: Mock) -> None:
    user_id = 0
    user = {"firstName": "Kuba", "group": "admin"}
    controller.patch_user(user_id, user)
    expected = call(user_id, user)
    assert expected in repository.patch_user.mock_calls


def test_delete_user(controller: UserController, repository: Mock) -> None:
    user_id = 1
    controller.delete_user(user_id)
    expected = call(user_id)
    assert expected in repository.delete_user.mock_calls
