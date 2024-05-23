import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.locators_base_page import LocatorsBasePage
from data import Url

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, page_url):
        self.driver.get(page_url)

    def wait_for_load_element(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

    def wait_for_open_page(self, page_url):
        return WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(page_url))

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def click_element(self, locator):
        self.find_element(locator).click()

    def set_value(self, locator, value):
        self.find_element(locator).send_keys(value)

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def switch_to_new_window(self):
        return self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Кликаем на логотип Самоката')
    def click_on_logo_scooter(self):
        self.click_element(LocatorsBasePage.LOGO_SCOOTER)

    @allure.step('Кликаем на логотип Яндекса')
    def click_on_logo_yandex(self):
        self.click_element(LocatorsBasePage.LOGO_YANDEX)

    @allure.step('Получаем ожидаемый URL страницы Дзен')
    def get_url_dzen_page(self):
        return Url.REDIRECT

    @allure.step('Ожидаем открытие страницы Дзен')
    def wait_for_open_dzen(self):
        self.wait_for_open_page(Url.REDIRECT)

    @allure.step('Получаем фактический URL')
    def get_current_url(self):
        return self.driver.current_url