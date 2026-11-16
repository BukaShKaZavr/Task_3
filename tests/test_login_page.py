import allure
import data
import urls


class TestLoginPage:

    @allure.title('Позитивная проверка перехода к окну восстановления пароля по кнопке "Восстановить пароль"')
    def test_go_to_recovery_password_page(self, login_page):
        login_page.go_to_url(urls.base_url)
        login_page.go_to_reset_password()
        assert login_page.recover_password_title_visible()

    @allure.title('Позитивная проверка ввода почты и нажатие по кнопке "Восстановить"')
    def test_enter_email(self, login_page):
        login_page.go_to_url(urls.base_url)
        login_page.put_email_to_email_field()
        login_page.click_recover_password_button()
        assert login_page.code_from_email_field_visible()

    @allure.title('Позитивная проверка нажатия по кнопке "показать/скрыть пароль", проверка что поле стало активным и подсвечивается')
    def test_click_hide_unhide_password(self, login_page):
        login_page.go_to_url(urls.base_url)
        login_page.click_hide_unhide_button()
        active_field = login_page.wait_for_password_field_border_colour(data.password_border_colour)
        assert active_field.is_displayed()
        assert data.password_border_colour in active_field.value_of_css_property('border')
