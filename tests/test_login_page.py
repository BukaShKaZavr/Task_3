import allure
from selenium.webdriver.support.wait import WebDriverWait
import data
import urls


class TestLoginPage:

    @allure.title('Позитивная проверка перехода к окну восстановления пароля по кнопке "Восстановить пароль"')
    def test_go_to_recovery_password_page(self, login_page):
        login_page.go_to_url(urls.base_url)
        assert login_page.go_to_reset_password()

    @allure.title('Позитивная проверка ввода почты и нажатие по кнопке "Восстановить"')
    def test_enter_email(self, login_page):
        login_page.go_to_url(urls.base_url)
        assert login_page.enter_email_and_recover_password()

    @allure.title('Позитивная проверка нажатия по кнопке "показать/скрыть пароль", проверка что поле стало активным и подсвечивается')
    def test_click_hide_unhide_password(self, login_page):
        login_page.go_to_url(urls.base_url)
        active_field = login_page.click_hide_unhide_button()
        WebDriverWait(login_page.driver, 5).until(
            lambda driver: data.password_border_colour in active_field.value_of_css_property('border'))
        assert active_field.is_displayed()
        assert data.password_border_colour in active_field.value_of_css_property('border')
