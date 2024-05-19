import allure

from data import Url, OrderPageData
from locators.locators_base_page import LocatorsBasePage
from locators.locators_main_page import LocatorsMainPage
from locators.locators_order_page import LocatorsOrderPage
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Заполняем формы заказа')
    def create_order(self, data_order):
        self.set_value(LocatorsOrderPage.FIRST_NAME, data_order['first_name'])
        self.set_value(LocatorsOrderPage.LAST_NAME, data_order['last_name'])
        self.set_value(LocatorsOrderPage.ADDRESS, data_order['address'])
        self.set_metro_station(data_order['station'])
        self.set_value(LocatorsOrderPage.PHONE_NUMBER, data_order['phone_number'])
        self.click_element(LocatorsOrderPage.BUTTON_NEXT)
        self.wait_for_load_element(LocatorsOrderPage.PAGE2_TITLE)
        self.set_value(LocatorsOrderPage.DELIVERY_DATE, data_order['delivery_date'])
        self.click_element(LocatorsOrderPage.SELECT_DATE)
        self.wait_for_load_element(LocatorsOrderPage.RENT_TIME)
        self.set_rent_days(data_order['rent_days'])
        self.set_scooter_color(data_order['color'])
        self.set_value(LocatorsOrderPage.COMMENT, data_order['comment'])
        self.click_element(LocatorsOrderPage.BUTTON_ORDER)
        self.wait_for_load_element(LocatorsOrderPage.CONFIRM_ORDER)
        self.click_element(LocatorsOrderPage.BUTTON_YES)

    @allure.step('Выбираем станцию метро')
    def set_metro_station(self, station):
        self.click_element(LocatorsOrderPage.METRO_STATION)
        method, station_loc = LocatorsOrderPage.SELECT_STATION
        station_locator_with_name = (method, station_loc.format(station))
        self.scroll_to_element(station_locator_with_name)
        self.click_element(station_locator_with_name)

    @allure.step('Выбираем срок аренды')
    def set_rent_days(self, rent_days):
        self.click_element(LocatorsOrderPage.RENT_TIME)
        method, rent_days_loc = LocatorsOrderPage.SELECT_RENT_TIME
        rent_days_locator_with_period = (method, rent_days_loc.format(rent_days))
        self.click_element(rent_days_locator_with_period)

    @allure.step('Выбираем цвет самоката')
    def set_scooter_color(self, scooter_color):
        method, checkbox_loc = LocatorsOrderPage.CHECKBOX_COLOR
        checkbox_locator_with_color = (method, checkbox_loc.format(scooter_color))
        self.click_element(checkbox_locator_with_color)

    @allure.step('Открываем страницу заказа')
    def open_order_page(self):
        self.open_page(Url.ORDER_PAGE)

    @allure.step('Ожидаем загрузку страницы заказа')
    def wait_for_load_form(self):
        self.wait_for_load_element(LocatorsOrderPage.PAGE1_TITLE)

    @allure.step('Ожидаем загрузку окна "Заказ оформлен"')
    def wait_for_load_order_completed(self):
        self.wait_for_load_element(LocatorsOrderPage.COMPLETE_ORDER)

    @allure.step('Находим текст заголовка в окне подтверждения заказа')
    def get_actual_result(self):
        actual_result = self.find_element(LocatorsOrderPage.COMPLETE_ORDER).text
        return actual_result

    @allure.step('Выводим ожидаемый результат текста заголовка')
    def get_expected_result(self):
        expected_result = OrderPageData.COMPLETE_ORDER_TITLE
        return expected_result

    @allure.step('Кликаем на логотип Самоката')
    def click_on_logo_scooter(self):
        self.click_element(LocatorsBasePage.LOGO_SCOOTER)

    @allure.step('Кликаем на логотип Яндекса')
    def click_on_logo_yandex(self):
        self.click_element(LocatorsBasePage.LOGO_YANDEX)

    @allure.step('Ожидаем загрузку заголовка "Самокат на пару дней" на главной странице')
    def wait_for_load_page_title(self):
        self.wait_for_load_element(LocatorsMainPage.PAGE_TITLE)

    @allure.step('Ожидаем открытие страницы Дзен')
    def wait_for_open_dzen(self):
        self.wait_for_open_page(Url.REDIRECT)

    @allure.step('Получаем ожидаемый URL главной страницы')
    def get_url_main_page(self):
        return Url.MAIN_PAGE

    @allure.step('Получаем ожидаемый URL страницы Дзен')
    def get_url_dzen_page(self):
        return Url.REDIRECT
