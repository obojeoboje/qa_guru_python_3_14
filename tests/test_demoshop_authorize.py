import os

import allure
from allure_commons._allure import step
from dotenv import load_dotenv
from selene import have
from selene.support.shared import browser

load_dotenv()
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')
API_URL = os.getenv('API_URL')
WEB_URL = os.getenv('WEB_URL')

browser.config.base_url = WEB_URL

def test_login_through_api(login):
    with step("Verify successful authorization"):
        browser.all(".account").first.should(have.text(os.getenv('LOGIN'))).click()

def test_search_negative_result(login):
    with allure.step("Negitive search"):
        browser.element('.search-box [value="Search store"]').click()
        browser.element('.search-box [value="Search store"]').type('negative test').press_enter()
        browser.element('.result').should(have.text('No products were found that matched your criteria.'))

def test_watch_profile(login):
    with allure.step("Check info in profile"):
        browser.all(".account").first.should(have.text(os.getenv('LOGIN'))).click()
        # browser.element(".account").should(have.text(os.getenv('LOGIN'))).click()
        browser.element('#FirstName').should(have.value('Alexander'))
        browser.element('#LastName').should(have.value('Oboje'))
        browser.element('#Email').should(have.value(os.getenv('LOGIN')))
        browser.element('[checked="checked"]#gender-male')

def test_watch_page_change_password(login):
    with allure.step("Check text buttion in change password"):
        browser.all(".account").first.should(have.text(os.getenv('LOGIN'))).click()
        browser.element('[href="/customer/changepassword"]').should(have.text('Change password')).click()
        browser.element('[for="OldPassword"]').should(have.text('Old password:'))
        browser.element('[for="NewPassword"]').should(have.text('New password:'))
        browser.element('[for="ConfirmNewPassword"]').should(have.text('Confirm password:'))

def test_logout(login):
    with allure.step("Check logout"):
        browser.element('.ico-logout').click()
        browser.element('.ico-login').should(have.text('Log in'))
