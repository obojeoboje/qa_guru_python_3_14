from pytest_voluptuous import S
import requests
from requests import Response
from schemas import user

base_url = "https://reqres.in/"


def test_create_user():
    create_user: Response = requests.post(
        url=f"{base_url}api/users",
        json=
        {
            "name": "Aleksandr",
            "job": "QA Automation",
        }
    )
    assert create_user.status_code == 201
    assert create_user.json()["name"] == "Aleksandr"
    assert create_user.json()["job"] == "QA Automation"
    assert S(user.create_single_user) == create_user.json()
    assert len(create_user.json()) == 4


def test_update_user():
    create_user: Response = requests.post(
        url=f"{base_url}api/users",
        json=
        {
            "name": "Aleksandr",
            "job": "QA Automation",
        }
    )
    update_user: Response = requests.put(
        url=f"{base_url}api/users/2",
        json=
        {
            "name": "Alexander",
            "job": "QA Automation"
        }
    )
    assert update_user.status_code == 200
    assert S(user.update_single_user) == update_user.json()
    assert update_user.json()["name"] == "Alexander"
    assert update_user.json()["job"] == "QA Automation"


def test_register_user():
    registrate_user: Response = requests.post(
        url=f"{base_url}api/register",
        json=
        {
            "email": "eve.holt@reqres.in",
            "password": "qwerty"
        }
    )
    assert registrate_user.status_code == 200
    assert S(user.register_single_user) == registrate_user.json()
    assert registrate_user.json()["token"] is not None


def test_login_user():
    login_user: Response = requests.post(
        url=f"{base_url}api/login",
        json=
        {
            "email": "eve.holt@reqres.in",
            "password": "qwerty"
        }
    )
    assert login_user.status_code == 200
    assert S(user.login_single_user_successful) == login_user.json()
    assert len(login_user.json()["token"]) == 17


def test_delete_user():
    create_user: Response = requests.post(
        url=f"{base_url}api/users",
        json=
        {
            "name": "Aleksandr",
            "job": "QA Automation",
        }
    )
    delete_user: Response = requests.delete(
        url=f"{base_url}api/users/2",
    )
    assert delete_user.status_code == 204