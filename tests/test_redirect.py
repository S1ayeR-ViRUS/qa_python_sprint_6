import allure

from pages.main_page import MainPage
from pages.order_page import OrderPage



class TestRedirect:
    @allure.title('Проверяем переход на главную страницу по клику на логотип Самоката')
    def test_redirect_to_main_page(self, driver):
        order_page = OrderPage(driver)
        main_page = MainPage(driver)
        order_page.open_order_page()
        order_page.click_on_logo_scooter()
        main_page.wait_for_load_page_title()
        expected_url = order_page.get_url_main_page()
        assert driver.current_url == expected_url

    @allure.title('Проверяем открытие нового окна со станицей Дзен по клику на логотип Яндекса')
    def test_redirect_to_dzen_in_new_window(self, driver):
        order_page = OrderPage(driver)
        order_page.open_order_page()
        order_page.click_on_logo_yandex()
        order_page.switch_to_new_window()
        order_page.wait_for_open_dzen()
        expected_url = order_page.get_url_dzen_page()
        assert driver.current_url == expected_url
