from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import data


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.wait = WebDriverWait(self.driver, self.timeout)

    def go_to_url(self, url):
        self.driver.get(url)

    def find_element_with_wait(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def find_few_elements(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_elements(*locator)

    def wait_for_text_in_element(self, locator, text):
        self.wait.until(expected_conditions.text_to_be_present_in_element(locator, text))

    def click_element(self, locator):
        self.wait.until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def click_web_element(self, element):
        self.wait.until(expected_conditions.element_to_be_clickable(element))
        element.click()

    #Нашел этот метод клика на просторах интернета
    #Какое то модоальное окно в Firefox на дает кликать на некоторые элементы, ниже я сделал ожидание для таких мест, но с pop-up-ами оно почему то не работает
    def click_element_js(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def click_web_element_js(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    # При запуске страницы в Firefox, есть какой то невидимый элемент и Firefox отказывался кликать сразу на что то, хотя хром работает без проблем
    # При этот репится почему то только на последней версии Firefox
    # Сделал вот такой метод, чтобы проверять пропажу этого элемента, его локатор брал из ошибки

    def element_is_not_visible(self, locator):
        def check_elements(driver):
            elements = driver.find_elements(*locator)

            for element in elements:
                if element.is_displayed():
                    return False
            return True
        return self.wait.until(check_elements)

    def wait_text(self, locator, text):
        self.wait.until_not(expected_conditions.text_to_be_present_in_element(locator, text))
        return self.driver.find_element(*locator).text

    def wait_for_order_not_default(self, locator):
        element = self.find_element_with_wait(locator)
        self.wait.until( lambda driver: element.text not in data.default_order_number)

    def add_text(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text(self, locator):
        return self.find_element_with_wait(locator).text

    def scroll_to_element(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator))
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def drag_and_drop_method(self, element_from, locator_to):
        element_to = self.find_element_with_wait(locator_to)
        ActionChains(self.driver).drag_and_drop(element_from, element_to).perform()

    #Этот метод также нашел в интернете, метод выше не работал в Firefox
    #Изначально думал, что проблема в размере окна, но перебрал разные варианты проблема не уходила, поэтому использовал этот метод
    def drag_and_drop_method_js(self, element_from, locator_to):
        element_to = self.find_element_with_wait(locator_to)

        self.driver.execute_script("""
            function createEvent(typeOfEvent) {
                var event = document.createEvent("CustomEvent");
                event.initCustomEvent(typeOfEvent, true, true, null);
                event.dataTransfer = {
                    data: {},
                    setData: function(key, value) { this.data[key] = value; },
                    getData: function(key) { return this.data[key]; }
                };
                return event;
            }
            function dispatchEvent(element, event, transferData) {
                if (transferData !== undefined) {
                    event.dataTransfer = transferData;
                }
                element.dispatchEvent(event);
            }
            var source = arguments[0];
            var target = arguments[1];
            var dragStartEvent = createEvent('dragstart');
            dispatchEvent(source, dragStartEvent);
            var dropEvent = createEvent('drop');
            dispatchEvent(target, dropEvent, dragStartEvent.dataTransfer);
            var dragEndEvent = createEvent('dragend');
            dispatchEvent(source, dragEndEvent, dropEvent.dataTransfer);
        """, element_from, element_to)