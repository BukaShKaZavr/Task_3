import allure


class TestConstructorPage:

    @allure.title('Позитивная проверка нажатия на кнопку "Конструктор"')
    def test_click_constructor_button(self, constructor_page):
        constructor_page.go_to_constructor_menu()
        assert constructor_page.constructor_menu_title_visible()

    @allure.title('Позитивная проверка нажатия на кнопку "Лента заказов"')
    def test_click_order_list_button(self, constructor_page):
        constructor_page.go_to_order_list()
        assert constructor_page.order_list_menu_title_visible()

    @allure.title('Позитивная проверка нажатия на любой ингредиент и проверка появления окна с деталями')
    def test_pop_up_with_ingredient_details(self, constructor_page):
        constructor_page.click_to_ingredient()
        assert constructor_page.ingredient_details_pop_up_visible()

    @allure.title('Позитивная проверка закрытия окна с деталями ингредиента по крестику')
    def test_close_pop_up_with_ingredient_details(self, constructor_page):
        constructor_page.click_to_ingredient()
        constructor_page.close_ingredient_details_pop_up()
        assert constructor_page.ingredient_details_pop_up_invisible()

    @allure.title('Позитивная проверка добавления ингредиента в заказ и увеличения его каунтера')
    def test_add_ingredient(self, constructor_page):
        constructor_page.add_random_bun()
        random_ingredient = constructor_page.get_random_ingredient()
        current_counter = int(constructor_page.get_ingredient_counter(random_ingredient))
        constructor_page.add_ingredient_to_order(random_ingredient)
        new_counter = int(constructor_page.get_ingredient_counter(random_ingredient))

        assert new_counter == current_counter+1

    @allure.title('Позитивная проверка оформления заказа зарегистрированным пользователем')
    def test_place_order(self, constructor_page):
        constructor_page.add_ingredients_for_order()
        constructor_page.confirm_order()
        assert constructor_page.order_confirmed_pop_up()