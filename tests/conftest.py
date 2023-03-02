import pytest
from dotenv import load_dotenv
from selene.support.shared import browser

from tests.test_demoshop_authorize import API_URL
from utils.base_session import BaseSession


load_dotenv()

@pytest.fixture(scope="session")
def login():
    authorization = BaseSession(API_URL)
    response = authorization.post("/login", json={"Email": "obojealexander@gmail.com", "Password": "123456"},
                                  allow_redirects=False)
    authorization_cookie = response.cookies.get("NOPCOMMERCE.AUTH")

    browser.open("/Themes/DefaultClean/Content/images/logo.png")

    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": authorization_cookie})
    browser.open("")