import random

import allure

from locators.order_list_page_locators import OrderListPageLocators
from locators.constructor_page_locators import ConstructorPageLocators
from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage

class OrderListPage(BasePage):

    @allure.step('Открывем всплывающее окно с деталями заказа')
    def open_order_details(self):
        orders_list = self.find_few_elements(OrderListPageLocators.orders_list)
        self.click_web_element(random.choice(orders_list))

        return self.find_element_with_wait(OrderListPageLocators.order_details_pop_up).is_displayed()

    @allure.step('Идем в личный кабинет и смотрим номера заказов пользователя')
    def get_user_orders_id(self):
        ingredient_bun = self.find_few_elements(ConstructorPageLocators.ingredients_list)[:2]
        self.drag_and_drop_method_js(random.choice(ingredient_bun), ConstructorPageLocators.add_item_field)
        other_ingredients = self.find_few_elements(ConstructorPageLocators.ingredients_list)[2:]
        self.drag_and_drop_method_js(random.choice(other_ingredients), ConstructorPageLocators.add_item_field)
        self.click_element(ConstructorPageLocators.place_order_button)
        close_pop_up_button = self.find_few_elements(ConstructorPageLocators.close_pop_up_buttons)
        self.click_web_element_js(close_pop_up_button[-1])
        self.element_is_not_visible(ConstructorPageLocators.modal_window)
        self.click_element(ConstructorPageLocators.profile_button)
        self.click_element(ProfilePageLocators.order_history_button)
        user_orders_list = self.find_few_elements(ProfilePageLocators.user_orders_list)
        user_orders_id = []
        for order in user_orders_list:
            user_orders_id.append(order.text)

        return user_orders_id

    @allure.step('Идем в раздел "Лента заказов" и собираем номера заказов в список')
    def get_all_orders_id(self):
        self.click_element(ConstructorPageLocators.order_list_button)
        orders_list = self.find_few_elements(ConstructorPageLocators.orders_list)
        orders_id = []
        for order in orders_list:
            orders_id.append(order.text)

        return orders_id

    @allure.step('Смотрим, есть ли номера заказом пользователя в разделе со всеми заказами')
    def check_user_orders_in_all_orders(self):
        user_orders = self.get_user_orders_id()
        all_orders = self.get_all_orders_id()

        for order in user_orders:
            if order not in all_orders:
                return False
        return True

    @allure.step('Переходим в раздел "Лента заказов" и смотрим текущий счетчик "Выполнено за всё время"')
    def get_current_all_orders_counter(self):
        self.click_element(ConstructorPageLocators.order_list_button)
        return self.find_element_with_wait(OrderListPageLocators.all_time_orders_counter).text

    @allure.step('Делаем заказ и повторно переходим в раздел "Лента заказов", чтобы посмотреть счетчик "Выполнено за всё время"')
    def get_all_orders_counter_after_order(self):
        self.click_element(ConstructorPageLocators.constructor_button)
        ingredient_bun = self.find_few_elements(ConstructorPageLocators.ingredients_list)[:2]
        self.drag_and_drop_method_js(random.choice(ingredient_bun), ConstructorPageLocators.add_item_field)
        other_ingredients = self.find_few_elements(ConstructorPageLocators.ingredients_list)[2:]
        self.drag_and_drop_method_js(random.choice(other_ingredients), ConstructorPageLocators.add_item_field)
        self.click_element(ConstructorPageLocators.place_order_button)
        close_pop_up_button = self.find_few_elements(ConstructorPageLocators.close_pop_up_buttons)
        self.click_web_element_js(close_pop_up_button[-1])
        self.element_is_not_visible(ConstructorPageLocators.modal_window)
        self.click_element(ConstructorPageLocators.order_list_button)
        return self.find_element_with_wait(OrderListPageLocators.all_time_orders_counter).text

    @allure.step('Сравниваем счетчик "Выполнено за всё время" ДО и ПОСЛЕ заказа')
    def check_all_orders_count_increase_after_order(self):
        current_counter = int(self.get_current_all_orders_counter())
        new_counter = int(self.get_all_orders_counter_after_order())
        return new_counter == current_counter+1

    @allure.step('Переходим в раздел "Лента заказов" и смотрим текущий счетчик "Выполнено за сегодня"')
    def get_current_today_orders_counter(self):
        self.click_element(ConstructorPageLocators.order_list_button)
        return self.find_element_with_wait(OrderListPageLocators.today_orders_counter).text

    @allure.step('Делаем заказ и повторно переходим в раздел "Лента заказов", чтобы посмотреть счетчик "Выполнено за сегодня"')
    def get_today_orders_counter_after_order(self):
        self.click_element(ConstructorPageLocators.constructor_button)
        ingredient_bun = self.find_few_elements(ConstructorPageLocators.ingredients_list)[:2]
        self.drag_and_drop_method_js(random.choice(ingredient_bun), ConstructorPageLocators.add_item_field)
        other_ingredients = self.find_few_elements(ConstructorPageLocators.ingredients_list)[2:]
        self.drag_and_drop_method_js(random.choice(other_ingredients), ConstructorPageLocators.add_item_field)
        self.click_element(ConstructorPageLocators.place_order_button)
        close_pop_up_button = self.find_few_elements(ConstructorPageLocators.close_pop_up_buttons)
        self.click_web_element_js(close_pop_up_button[-1])
        self.element_is_not_visible(ConstructorPageLocators.modal_window)
        self.click_element(ConstructorPageLocators.order_list_button)
        return self.find_element_with_wait(OrderListPageLocators.today_orders_counter).text

    @allure.step('Сравниваем счетчик "Выполнено за сегодня" ДО и ПОСЛЕ заказа')
    def check_today_orders_count_increase_after_order(self):
        current_counter = int(self.get_current_today_orders_counter())
        new_counter = int(self.get_today_orders_counter_after_order())
        return new_counter == current_counter+1

    @allure.step('Делаем заказ и смотрим номер заказа на всплывающем окне')
    def get_order_number_on_confirm_pop_up(self):
        ingredient_bun = self.find_few_elements(ConstructorPageLocators.ingredients_list)[:2]
        self.drag_and_drop_method_js(random.choice(ingredient_bun), ConstructorPageLocators.add_item_field)
        other_ingredients = self.find_few_elements(ConstructorPageLocators.ingredients_list)[2:]
        self.drag_and_drop_method_js(random.choice(other_ingredients), ConstructorPageLocators.add_item_field)
        self.click_element(ConstructorPageLocators.place_order_button)
        close_pop_up_button = self.find_few_elements(ConstructorPageLocators.close_pop_up_buttons)
        self.wait_for_order_not_default(ConstructorPageLocators.order_number_on_confirm_pop_up)
        user_order_number = self.find_element_with_wait(ConstructorPageLocators.order_number_on_confirm_pop_up).text
        self.click_web_element_js(close_pop_up_button[-1])
        self.element_is_not_visible(ConstructorPageLocators.modal_window)

        return user_order_number

    @allure.step('Переходи в раздел "Лента заказов" и смотрим есть ли номер нашего заказа в поле "В работе"')
    def check_order_work_in_progress(self):
        user_order_number = self.get_order_number_on_confirm_pop_up()
        self.click_element(ConstructorPageLocators.order_list_button)
        self.wait_for_text_in_element(OrderListPageLocators.work_in_progress_field, user_order_number)
        orders_in_progress = self.find_element_with_wait(OrderListPageLocators.work_in_progress_field).text

        return user_order_number in orders_in_progress







