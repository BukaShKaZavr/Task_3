from selenium.webdriver.common.by import By

class LoginPageLocators:

    login_title = (By.XPATH, '//*[text()="Вход"]')
    forgot_password_button = (By.XPATH, '//*[@class="Auth_link__1fOlj" and text()="Восстановить пароль"]')
    recover_password_title = (By.XPATH, '//*[text()="Восстановление пароля"]')
    email_field = (By.XPATH, '//*[@class="text input__textfield text_type_main-default"]')
    recover_button = (By.XPATH, '//*[text()="Восстановить"]')

    new_password_field = (By.XPATH, '//*[text()="Пароль"]')
    new_password_field_active = (By.XPATH, '//*[@class="input pr-6 pl-6 input_type_text input_size_default input_status_active"]')
    code_from_email_field = (By.XPATH, '//*[text()="Введите код из письма"]')
    hide_unhide_password_button = (By.CSS_SELECTOR, ".input__icon.input__icon-action > svg")
    save_password_button = (By.XPATH, '//*[text()="Сохранить"]')

    login_email = (By.XPATH, '//*[@class="text input__textfield text_type_main-default" and @name="name"]')
    login_password = (By.XPATH, '//*[@class="text input__textfield text_type_main-default" and @name="Пароль"]')
    login_button = (By.XPATH, '//*[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]')



