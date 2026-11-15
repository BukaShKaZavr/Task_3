import allure


class TestConstructorPage:

    @allure.title('Позитивная проверка нажатия на кнопку "Конструктор"')
    def test_click_constructor_button(self, constructor_page):
        assert constructor_page.click_constructor_button()

    @allure.title('Позитивная проверка нажатия на кнопку "Лента заказов"')
    def test_click_order_list_button(self, constructor_page):
        assert constructor_page.click_order_list_button()

    @allure.title('Позитивная проверка нажатия на любой ингредиент и проверка появления окна с деталями')
    def test_pop_up_with_ingredient_details(self, constructor_page):
        assert constructor_page.click_to_ingredient()

    @allure.title('Позитивная проверка закрытия окна с деталями ингредиента по крестику')
    def test_close_pop_up_with_ingredient_details(self, constructor_page):
        assert constructor_page.close_ingredient_details_pop_up()

    @allure.title('Позитивная проверка добавления ингредиента в заказ и увеличения его каунтера')
    def test_add_ingredient(self, constructor_page):
        assert constructor_page.add_ingredient_to_order()

    @allure.title('Позитивная проверка оформления заказа зарегистрированным пользователем')
    def test_place_order(self, constructor_page):
        assert constructor_page.place_order()