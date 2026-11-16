import allure

class TestProfilePage:

    @allure.title('Позитивная проверка перехода при нажатии на кнопку "Личного кабинета"')
    def test_go_to_profile(self, profile_page):
        profile_page.go_to_profile_menu()
        assert profile_page.profile_page_description_visible()

    @allure.title('Позитивная проверка перехода в "Историю заказов" при нажатии кнопки')
    def test_go_to_order_history(self, profile_page):
        profile_page.go_to_profile_menu()
        profile_page.click_order_history_button()
        assert profile_page.order_history_field_visible()

    @allure.title('Позитивная проверка выхода из аккаунта')
    def test_account_logout(self, profile_page):
        profile_page.account_logout()
        assert profile_page.profile_description_invisible()