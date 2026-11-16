from selenium.webdriver.common.by import By

class BasePageLocators:
    modal_window = (By.XPATH, '//*[@class = "Modal_modal_overlay__x2ZCr"]')
    profile_button = (By.XPATH, '//*[(contains(@class,"AppHeader_header__linkText__3q_va")) and (text() = "Личный Кабинет")]')
    constructor_button = (By.XPATH, '//*[(contains(@class,"AppHeader_header__linkText__3q_va")) and (text() = "Конструктор")]')
    order_list_button = (By.XPATH, '//*[(contains(@class,"AppHeader_header__linkText__3q_va")) and (text() = "Лента Заказов")]')