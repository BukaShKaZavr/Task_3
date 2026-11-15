import allure
from locators.constructor_page_locators import ConstructorPageLocators
import urls
class TestOrderListPage:

    @allure.title('Позитивная проверка открытия всплывающеге окна с деталями при нажатии на заказ')
    def test_order_details_pop_up(self, order_list_page):
        order_list_page.go_to_url(urls.base_url)
        order_list_page.element_is_not_visible(ConstructorPageLocators.modal_window)
        order_list_page.click_element(ConstructorPageLocators.order_list_button)

        assert order_list_page.open_order_details()

    @allure.title('Проверка отображения заказов из "Истории заказов" пользователя на странице "Лента Заказов"')
    def test_check_user_orders_in_all_orders(self, order_list_page):
        assert order_list_page.check_user_orders_in_all_orders()

    @allure.title('Позитивная проверка увеличения счетчика "Выполнено за всё время" после оформления заказа')
    def test_increase_all_orders_count_after_order(self, order_list_page):
        assert order_list_page.check_all_orders_count_increase_after_order()

    @allure.title('Позитивная проверка увеличения счетчика "Выполнено за сегодня " после оформления заказа')
    def test_increase_today_orders_count_after_order(self, order_list_page):
        assert order_list_page.check_today_orders_count_increase_after_order()

    @allure.title('Позитивная проверка появления номера оформленного заказа в разделе "В работе"')
    def test_user_order_in_working_list(self, order_list_page):
        assert order_list_page.check_order_work_in_progress()