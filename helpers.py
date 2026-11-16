import random
import string
from selenium import webdriver

def generate_random_strings(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


class WebdriverFactory:
    @staticmethod
    def get_webdriver(browser_name: str):
        if browser_name == "firefox":
            return webdriver.Firefox()
        elif browser_name == "chrome":
            return webdriver.Chrome()
        return 'Бразуер не тестируется'
