import pytest

import api_methods
import api_requests
from helpers import WebdriverFactory
from pages.login_page import LoginPage
from pages.constructor_page import ConstructorPage
from pages.profile_page import ProfilePage
from pages.order_list_page import OrderListPage


@pytest.fixture(scope="function")
def create_and_login_user(driver, requests_object):
    user = api_methods.register_new_user_and_return_login_password()
    login_page = LoginPage(driver)
    login_page.login(user[0], user[1])

    yield driver

    headers = {"Authorization": user[2]}
    requests_object.delete_user(headers)

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome"
    )

@pytest.fixture(scope='function')
def driver(request):
    browser = request.config.getoption("--browser")
    driver = WebdriverFactory.get_webdriver(browser)
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def constructor_page(create_and_login_user):
    page = ConstructorPage(create_and_login_user)
    page.timeout = 10
    return page

@pytest.fixture(scope='function')
def login_page(driver):
    page = LoginPage(driver)
    page.timeout = 10
    return page

@pytest.fixture(scope='function')
def profile_page(create_and_login_user):
    page = ProfilePage(create_and_login_user)
    page.timeout = 10
    return page

@pytest.fixture(scope='function')
def order_list_page(create_and_login_user):
    page = OrderListPage(create_and_login_user)
    page.timeout = 10
    return page

@pytest.fixture(scope="function")
def requests_object():
    return api_requests.RequestsApi()
