import random
import allure

from locators.order_list_page_locators import OrderListPageLocators
from pages.base_page import BasePage

class OrderListPage(BasePage):

    @allure.step('Открывем всплывающее окно с деталями заказа')
    def open_order_details(self):
        orders_list = self.find_few_elements(OrderListPageLocators.orders_list)
        self.click_web_element(random.choice(orders_list))

    @allure.step('Смотрим на всплывающее окно с деталями заказа')
    def order_details_pop_up_visible(self):
        return self.find_element_with_wait(OrderListPageLocators.order_details_pop_up).is_displayed()

    @allure.step('Собираем номера всех заказов в список')
    def get_all_orders_id(self):
        orders_list = self.find_few_elements(OrderListPageLocators.orders_list_numbers)
        orders_id = []
        for order in orders_list:
            orders_id.append(order.text)

        return orders_id

    @allure.step('Смотрим, есть ли номера заказов пользователя в разделе со всеми заказами')
    def check_user_orders_in_all_orders(self, user_orders, all_orders):
        for order in user_orders:
            if order not in all_orders:
                return False
        return True

    @allure.step('Cмотрим текущий счетчик "Выполнено за всё время"')
    def get_current_all_orders_counter(self):
        self.go_to_order_list()
        return int(self.find_element_with_wait(OrderListPageLocators.all_time_orders_counter).text)

    @allure.step('Cмотрим текущий счетчик "Выполнено за сегодня"')
    def get_current_today_orders_counter(self):
        self.go_to_order_list()
        return int(self.find_element_with_wait(OrderListPageLocators.today_orders_counter).text)

    @allure.step('Ожидаем появления заказа в поле "В работе"')
    def order_work_in_progress_visible(self, order_number):
        self.wait_for_text_in_element(OrderListPageLocators.work_in_progress_field, order_number)
        return self.find_element_with_wait(OrderListPageLocators.work_in_progress_field).text







