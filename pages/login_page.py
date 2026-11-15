import allure

import data

from locators.constructor_page_locators import ConstructorPageLocators
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step('Переходи в раздел "Восстановить пароль"')
    def go_to_reset_password(self):
        self.element_is_not_visible(ConstructorPageLocators.modal_window)
        self.click_element(ConstructorPageLocators.profile_button)
        self.click_element(LoginPageLocators.forgot_password_button)
        return self.find_element_with_wait(LoginPageLocators.recover_password_title).is_displayed()

    @allure.step('Добавляем email в разделе восстановления пароля и нажимаем "Восстановить"')
    def enter_email_and_recover_password(self):
        self.element_is_not_visible(ConstructorPageLocators.modal_window)
        self.click_element(ConstructorPageLocators.profile_button)
        self.click_element(LoginPageLocators.forgot_password_button)
        self.add_text(LoginPageLocators.email_field, data.email)
        self.click_element(LoginPageLocators.recover_button)
        return self.find_element_with_wait(LoginPageLocators.code_from_email_field).is_displayed()

    @allure.step('Нажимаем на кнопку "показать/скрыть" пароль в разделе восстановления пароля')
    def click_hide_unhide_button(self):
        self.element_is_not_visible(ConstructorPageLocators.modal_window)
        self.enter_email_and_recover_password()
        self.element_is_not_visible(ConstructorPageLocators.modal_window)
        self.click_element(LoginPageLocators.hide_unhide_password_button)

        return self.find_element_with_wait(LoginPageLocators.new_password_field_active)

