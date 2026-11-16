import allure
import helpers
import api_requests


@allure.step('Регистрируем нового пользователя и возвращаем его логин, пароль и токен')
def register_new_user_and_return_login_password():
    login_pass = []

    email = f'{helpers.generate_random_strings(10)}@test.ru'
    password = helpers.generate_random_strings(10)
    name = helpers.generate_random_strings(10)

    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    request_object = api_requests.RequestsApi()
    response = request_object.create_user(payload)
    data_for_token = response.json()

    if response.status_code == 200:
        login_pass.append(email)
        login_pass.append(password)
        login_pass.append(data_for_token.get('accessToken'))

    return login_pass