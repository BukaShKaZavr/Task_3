from selenium.webdriver.common.by import By

class OrderListPageLocators:

    all_time_orders_counter = (By.XPATH, '//*[@class="undefined mb-15"]//*[(contains(@class,"OrderFeed_number__2MbrQ text text_type_digits-large"))]')
    today_orders_counter = (By.XPATH, '//div[.//p[text()="Выполнено за сегодня:"]]/p[contains(@class, "OrderFeed_number")]')
    orders_list = (By.XPATH, '//*[@class="OrderHistory_listItem__2x95r mb-6"]')
    order_details_pop_up = (By.XPATH, '//*[@class="Modal_modal_opened__3ISw4 Modal_modal__P3_V5"]//*[@class="Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10"]')
    orders_list_numbers = (By.XPATH, '//*[@class="OrderHistory_listItem__2x95r mb-6"]//*[@class="text text_type_digits-default"]')

    work_in_progress_field = (By.XPATH, '//*[@class="OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]//*[@class="text text_type_digits-default mb-2"]')

