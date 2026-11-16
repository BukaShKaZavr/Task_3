import allure
import data
import urls
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step('Переходим в раздел "Восстановить пароль"')
    def go_to_reset_password(self):
        self.go_to_profile_menu()
        self.click_element(LoginPageLocators.forgot_password_button)

    @allure.step('Смотрим на заголовок "Восстановить пароль"')
    def recover_password_title_visible(self):
        return self.find_element_with_wait(LoginPageLocators.recover_password_title).is_displayed()

    @allure.step('Добавляем email в разделе восстановления пароля')
    def put_email_to_email_field(self):
        self.go_to_profile_menu()
        self.click_element(LoginPageLocators.forgot_password_button)
        self.add_text(LoginPageLocators.email_field, data.email)

    @allure.step('Нажимаем "Восстановить"')
    def click_recover_password_button(self):
        self.click_element(LoginPageLocators.recover_button)

    @allure.step('Смотрим на поле "Введите код из письма"')
    def code_from_email_field_visible(self):
        return self.find_element_with_wait(LoginPageLocators.code_from_email_field).is_displayed()

    @allure.step('Нажимаем на кнопку "показать/скрыть" пароль в разделе восстановления пароля')
    def click_hide_unhide_button(self):
        self.wait_for_modal_window_to_disappear()
        self.put_email_to_email_field()
        self.click_recover_password_button()
        self.wait_for_modal_window_to_disappear()
        self.click_element(LoginPageLocators.hide_unhide_password_button)

    @allure.step('Ожидаем, пока рамка вокруг поля пароля подсветится нужным цветом')
    def wait_for_password_field_border_colour(self, border_colour):
        password_border = self.find_element_with_wait(LoginPageLocators.new_password_field_active)
        self.wait.until(lambda d: border_colour in password_border.value_of_css_property('border'))
        return password_border

    @allure.step('Логин пользователя')
    def login(self, email, password):
        self.go_to_url(urls.base_url)
        self.go_to_profile_menu()
        self.add_text(LoginPageLocators.login_email, email)
        self.add_text(LoginPageLocators.login_password, password)
        self.click_element(LoginPageLocators.login_button)
        self.wait_for_modal_window_to_disappear()

