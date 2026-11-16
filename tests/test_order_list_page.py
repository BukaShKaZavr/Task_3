import allure


class TestOrderListPage:

    @allure.title('Позитивная проверка открытия всплывающеге окна с деталями при нажатии на заказ')
    def test_order_details_pop_up(self, order_list_page):
        order_list_page.go_to_order_list()
        order_list_page.open_order_details()
        assert order_list_page.order_details_pop_up_visible()

    @allure.title('Проверка отображения заказов из "Истории заказов" пользователя на странице "Лента Заказов"')
    def test_check_user_orders_in_all_orders(self, order_list_page, constructor_page, profile_page):
        constructor_page.full_order()
        user_orders_list = profile_page.get_user_orders_id()
        order_list_page.go_to_order_list()
        all_orders_list = order_list_page.get_all_orders_id()

        assert order_list_page.check_user_orders_in_all_orders(user_orders_list, all_orders_list)

    @allure.title('Позитивная проверка увеличения счетчика "Выполнено за всё время" после оформления заказа')
    def test_increase_all_orders_count_after_order(self, order_list_page, constructor_page):
        current_counter = order_list_page.get_current_all_orders_counter()
        order_list_page.go_to_constructor_menu()
        constructor_page.full_order()
        updated_counter = order_list_page.get_current_all_orders_counter()
        assert updated_counter == current_counter+1

    @allure.title('Позитивная проверка увеличения счетчика "Выполнено за сегодня " после оформления заказа')
    def test_increase_today_orders_count_after_order(self, order_list_page, constructor_page):
        current_counter = order_list_page.get_current_today_orders_counter()
        order_list_page.go_to_constructor_menu()
        constructor_page.full_order()
        updated_counter = order_list_page.get_current_today_orders_counter()
        assert updated_counter == current_counter + 1

    @allure.title('Позитивная проверка появления номера оформленного заказа в разделе "В работе"')
    def test_user_order_in_working_list(self, order_list_page, constructor_page):
        user_order = constructor_page.get_order_number_from_pop_up()
        order_list_page.go_to_order_list()
        in_progress_orders = order_list_page.order_work_in_progress_visible(user_order)

        assert user_order in in_progress_orders