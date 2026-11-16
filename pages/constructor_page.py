import allure
import random
from locators.constructor_page_locators import ConstructorPageLocators
from pages.base_page import BasePage

class ConstructorPage(BasePage):

    @allure.step('Смотрим на заголовок раздела "Конструктор"')
    def constructor_menu_title_visible(self):
        return self.find_element_with_wait(ConstructorPageLocators.constructor_title).is_displayed()

    @allure.step('Смотрим на заголовок раздела "Лента заказов"')
    def order_list_menu_title_visible(self):
        return self.find_element_with_wait(ConstructorPageLocators.order_list_title).is_displayed()

    @allure.step('Нажимаем на случайный ингредиент')
    def click_to_ingredient(self):
        random_ingredient = random.choice(self.find_few_elements(ConstructorPageLocators.ingredients_list))
        self.click_web_element(random_ingredient)

    @allure.step('Смотрим на всплывающее окно с деталями ингредиента')
    def ingredient_details_pop_up_visible(self):
        return self.find_element_with_wait(ConstructorPageLocators.ingredient_details_pop_up).is_displayed()

    @allure.step('Закрываем всплывающее окно с деталями ингредиента')
    def close_ingredient_details_pop_up(self):
        close_button = self.find_few_elements(ConstructorPageLocators.close_pop_up_buttons)
        self.click_web_element_js(close_button[0])

    @allure.step('Смотрим на отсутсвие всплывающего окна с деталями ингредиента')
    def ingredient_details_pop_up_invisible(self):
        return self.element_is_not_visible(ConstructorPageLocators.ingredient_details_pop_up)

    @allure.step('Добавляем ингредиенты в заказ')
    def add_ingredients_for_order(self):
        self.wait_for_modal_window_to_disappear()
        ingredient_bun = self.find_few_elements(ConstructorPageLocators.ingredients_list)[:2]
        self.drag_and_drop_method_js(random.choice(ingredient_bun), ConstructorPageLocators.add_item_field)
        other_ingredients = self.find_few_elements(ConstructorPageLocators.ingredients_list)[2:]
        random_ingredient = random.choice(other_ingredients)
        self.drag_and_drop_method_js(random_ingredient, ConstructorPageLocators.add_item_field)

    @allure.step('Нажимаем на кнопку заказа')
    def confirm_order(self):
        self.click_element(ConstructorPageLocators.place_order_button)

    @allure.step('Смотрим на всплывающее окно оформленного заказа')
    def order_confirmed_pop_up(self):
        return self.find_element_with_wait(ConstructorPageLocators.order_confirm_pop_up).is_displayed()

    @allure.step('Делаем заказ с ингредиентами')
    def full_order(self):
        self.wait_for_modal_window_to_disappear()
        ingredient_bun = self.find_few_elements(ConstructorPageLocators.ingredients_list)[:2]
        self.drag_and_drop_method_js(random.choice(ingredient_bun), ConstructorPageLocators.add_item_field)
        other_ingredients = self.find_few_elements(ConstructorPageLocators.ingredients_list)[2:]
        random_ingredient = random.choice(other_ingredients)
        self.drag_and_drop_method_js(random_ingredient, ConstructorPageLocators.add_item_field)
        self.click_element(ConstructorPageLocators.place_order_button)
        close_button = self.find_few_elements(ConstructorPageLocators.close_pop_up_buttons)
        self.click_web_element_js(close_button[0])

    @allure.step('Забираем номер заказа с всплывающего окна после подтверждения')
    def get_order_number_from_pop_up(self):
        self.add_ingredients_for_order()
        self.confirm_order()
        close_pop_up_button = self.find_few_elements(ConstructorPageLocators.close_pop_up_buttons)
        self.wait_for_order_not_default(ConstructorPageLocators.order_number_on_confirm_pop_up)
        user_order_number = self.find_element_with_wait(ConstructorPageLocators.order_number_on_confirm_pop_up).text
        self.click_web_element_js(close_pop_up_button[-1])

        return user_order_number

    @allure.step('Находим случайную булку и добавляем ее в заказ')
    def add_random_bun(self):
        ingredient_bun = self.find_few_elements(ConstructorPageLocators.ingredients_list)[:2]
        self.drag_and_drop_method_js(random.choice(ingredient_bun), ConstructorPageLocators.add_item_field)

    @allure.step('Находим случайный ингредиент (не булку)')
    def get_random_ingredient(self):
        other_ingredients = self.find_few_elements(ConstructorPageLocators.ingredients_list)[2:]
        return random.choice(other_ingredients)

    @allure.step('Смотрим на текущий счетчик ингредиента')
    def get_ingredient_counter(self, ingredient_element):
        counter_element = ingredient_element.find_element(*ConstructorPageLocators.ingredient_counter)
        return int(counter_element.text)

    @allure.step('Добавляем ингредиент в заказ')
    def add_ingredient_to_order(self, ingredient_element):
        self.drag_and_drop_method_js(ingredient_element, ConstructorPageLocators.add_item_field)