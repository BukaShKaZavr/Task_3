import pytest

import api_methods
import api_requests
import urls
from helpers import WebdriverFactory
from locators.constructor_page_locators import ConstructorPageLocators
from locators.login_page_locators import LoginPageLocators
from pages.login_page import LoginPage
from pages.constructor_page import ConstructorPage
from pages.profile_page import ProfilePage
from pages.order_list_page import OrderListPage


@pytest.fixture(scope="function")
def create_and_login_user(driver, requests_object):
    user = api_methods.register_new_user_and_return_login_password()
    login_page = LoginPage(driver)
    login_page.go_to_url(urls.base_url)
    login_page.element_is_not_visible(ConstructorPageLocators.modal_window)
    login_page.click_element(ConstructorPageLocators.profile_button)
    login_page.add_text(LoginPageLocators.login_email, user[0])
    login_page.add_text(LoginPageLocators.login_password, user[1])
    login_page.click_element(LoginPageLocators.login_button)
    login_page.element_is_not_visible(ConstructorPageLocators.modal_window)

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
