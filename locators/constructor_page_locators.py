from selenium.webdriver.common.by import By

class ConstructorPageLocators:

    constructor_title = (By.XPATH, '//*[@class = "text text_type_main-large mb-5 mt-10" and text() = "Соберите бургер"]')
    order_list_title = (By.XPATH, '//*[@class = "text text_type_main-large mt-10 mb-5" and text() = "Лента заказов"]')

    place_order_button = (By.XPATH, '//*[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]')
    ingredients_list = (By.XPATH, '//*[@class="BurgerIngredients_ingredients__menuContainer__Xu3Mo"]/ul/a')
    ingredient_counter = (By.XPATH, './/*[@class="counter_counter__num__3nue1"]')
    ingredient_details_pop_up = (By.XPATH,'//*[@class="Modal_modal_opened__3ISw4 Modal_modal__P3_V5"]//*[(contains(@class,"Modal_modal__title_modified__3Hjkd"))]')
    order_number_on_confirm_pop_up = (By.XPATH,'//*[@class="Modal_modal_opened__3ISw4 Modal_modal__P3_V5"]//*[@class="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]')
    close_pop_up_buttons = (By.XPATH, '//button[contains(@class, "Modal_modal__close")]')
    add_item_field = (By.XPATH, '//*[@class="BurgerConstructor_basket__29Cd7 mt-25 "]')
    order_confirm_pop_up = (By.XPATH,'//*[@class="Modal_modal_opened__3ISw4 Modal_modal__P3_V5"]//*[(contains(@class,"undefined text text_type_main-medium mb-15")) and (text() = "идентификатор заказа")]')