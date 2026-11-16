from selenium.webdriver.common.by import By

class ProfilePageLocators:

    order_history_button = (By.XPATH, '//*[@class="Account_link__2ETsJ text text_type_main-medium text_color_inactive"]')
    order_history_field_2 = (By.XPATH, '//*[@class="OrderHistory_orderHistory__qy1VB"]')
    order_history_field = (By.XPATH, '//*[(contains(@class,"Account_link_active__2opc9")) and (text() = "История заказов")]')
    user_orders_list = (By.XPATH, '//*[@class="OrderHistory_listItem__2x95r mb-6"]//*[@class="text text_type_digits-default"]')
    logout_button = (By.XPATH, '//*[@class="Account_button__14Yp3 text text_type_main-medium text_color_inactive"]')
    profile_page_description = (By.XPATH, '//*[@class="Account_text__fZAIn text text_type_main-default"]')
