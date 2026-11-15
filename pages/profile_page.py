import allure
from locators.constructor_page_locators import ConstructorPageLocators
from locators.login_page_locators import LoginPageLocators
from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage


class ProfilePage(BasePage):

    @allure.step('Переходим в "Личный кабинет"')
    def go_to_profile(self):
        self.click_element(ConstructorPageLocators.profile_button)
        return self.find_element_with_wait(ProfilePageLocators.profile_page_description).is_displayed()

    @allure.step('Переходи в раздел "История заказов" в "Личном кабинете"')
    def go_to_order_history(self):
        self.click_element(ConstructorPageLocators.profile_button)
        self.click_element(ProfilePageLocators.order_history_button)
        return self.find_element_with_wait(ProfilePageLocators.order_history_field).is_displayed()

    @allure.step('Выходим из профиля в "Личном кабинете"')
    def account_logout(self):
        self.click_element(ConstructorPageLocators.profile_button)
        self.click_element(ProfilePageLocators.logout_button)
        return self.find_element_with_wait(LoginPageLocators.login_title).is_displayed()