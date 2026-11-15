import allure
import random
from locators.constructor_page_locators import ConstructorPageLocators
from pages.base_page import BasePage

class ConstructorPage(BasePage):

    @allure.step('Нажимаем на кнопку "Конструктор"')
    def click_constructor_button(self):
        self.click_element(ConstructorPageLocators.constructor_button)
        return self.find_element_with_wait(ConstructorPageLocators.constructor_title).is_displayed()

    @allure.step('Нажимаем на кнопку "Лента заказов"')
    def click_order_list_button(self):
        self.click_element(ConstructorPageLocators.order_list_button)
        return self.find_element_with_wait(ConstructorPageLocators.order_list_title).is_displayed()

    @allure.step('Нажимаем на случайный ингредиент')
    def click_to_ingredient(self):
        random_ingredient = random.choice(self.find_few_elements(ConstructorPageLocators.ingredients_list))
        self.click_web_element(random_ingredient)
        return self.find_element_with_wait(ConstructorPageLocators.ingredient_details_pop_up).is_displayed()

    @allure.step('Закрываем всплывающее окно с деталями ингредиента')
    def close_ingredient_details_pop_up(self):
        random_ingredient = random.choice(self.find_few_elements(ConstructorPageLocators.ingredients_list))
        self.click_web_element(random_ingredient)
        close_button = self.find_few_elements(ConstructorPageLocators.close_pop_up_buttons)
        self.click_web_element_js(close_button[0])
        return self.element_is_not_visible(ConstructorPageLocators.ingredient_details_pop_up)

    @allure.step('Добавляем ингредиенты и делаем заказ')
    def place_order(self):
        ingredient_bun = self.find_few_elements(ConstructorPageLocators.ingredients_list)[:2]
        self.drag_and_drop_method_js(random.choice(ingredient_bun), ConstructorPageLocators.add_item_field)
        other_ingredients = self.find_few_elements(ConstructorPageLocators.ingredients_list)[2:]
        self.drag_and_drop_method_js(random.choice(other_ingredients), ConstructorPageLocators.add_item_field)
        self.click_element(ConstructorPageLocators.place_order_button)
        return self.find_element_with_wait(ConstructorPageLocators.order_confirm_pop_up).is_displayed()

    @allure.step('Добавляем ингредиенты заказ и сравниваем счетчик ингрелиента ДО и ПОСЛЕ')
    def add_ingredient_to_order(self):
        self.element_is_not_visible(ConstructorPageLocators.modal_window)
        ingredient_bun = self.find_few_elements(ConstructorPageLocators.ingredients_list)[:2]
        self.drag_and_drop_method_js(random.choice(ingredient_bun), ConstructorPageLocators.add_item_field)
        other_ingredients = self.find_few_elements(ConstructorPageLocators.ingredients_list)[2:]
        random_ingredient = random.choice(other_ingredients)
        random_ingredient_counter = random_ingredient.find_element(*ConstructorPageLocators.ingredient_counter)
        current_counter = int(random_ingredient_counter.text)
        self.drag_and_drop_method_js(random_ingredient, ConstructorPageLocators.add_item_field)
        new_counter = int(random_ingredient.find_element(*ConstructorPageLocators.ingredient_counter).text)

        return new_counter == current_counter + 1