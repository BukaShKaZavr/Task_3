import allure

class TestProfilePage:

    @allure.title('Позитивная проверка перехода при нажатии на кнопку "Личного кабинета"')
    def test_go_to_profile(self, profile_page):
        assert profile_page.go_to_profile()

    @allure.title('Позитивная проверка перехода в "Историю заказов" при нажатии кнопки')
    def test_go_to_order_history(self, profile_page):
        assert profile_page.go_to_order_history()

    @allure.title('Позитивная проверка выхода из аккаунта')
    def test_account_logout(self, profile_page):
        assert profile_page.account_logout()