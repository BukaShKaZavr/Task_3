import allure
from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage


class ProfilePage(BasePage):

    @allure.step('Проверяем точно ли мы в "Личном кабинете"')
    def profile_page_description_visible(self):
        return self.find_element_with_wait(ProfilePageLocators.profile_page_description).is_displayed()

    @allure.step('Нажимаем на кнопку "История заказов"')
    def click_order_history_button(self):
        self.go_to_profile_menu()
        self.click_element(ProfilePageLocators.order_history_button)

    @allure.step('Смотрим на поле заказов в разделе "История заказов"')
    def order_history_field_visible(self):
        return self.find_element_with_wait(ProfilePageLocators.order_history_field).is_displayed()

    @allure.step('Собираем номера заказов в разделе "История заказов"')
    def get_user_orders_id(self):
        self.go_to_profile_menu()
        self.click_element(ProfilePageLocators.order_history_button)
        user_orders_list = self.find_few_elements(ProfilePageLocators.user_orders_list)
        user_orders_id = []
        for order in user_orders_list:
            user_orders_id.append(order.text)

        return user_orders_id

    @allure.step('Нажимаем на кнопку "Выход"')
    def account_logout(self):
        self.go_to_profile_menu()
        self.click_element(ProfilePageLocators.logout_button)

    @allure.step('Смотрим на отсутствие описания профиля при попытке зайти в личный кабинет после выхода')
    def profile_description_invisible(self):
        self.go_to_profile_menu()
        return self.element_is_not_visible(ProfilePageLocators.profile_page_description)