
import api_methods

default_order_number = ['9999']
password_border_colour = 'rgb(76, 76, 255)'

test_login_pass = api_methods.register_new_user_and_return_login_password()
email = test_login_pass[0]

