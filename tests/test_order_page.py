import allure
import pytest
from data import OrderPageData
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title('Проверяем позитивный сценарий заказа самоката')
    @allure.description('Проверяем весь флоу позитивного сценария с двумя наборами данных')
    @pytest.mark.parametrize('data_order', [OrderPageData.TEST_DATA, OrderPageData.TEST_DATA_2])
    def test_order_scooter(self, driver, data_order):
        order_page = OrderPage(driver)
        order_page.open_order_page()
        order_page.wait_for_load_form()
        order_page.create_order(data_order)
        order_page.wait_for_load_order_completed()
        assert order_page.get_expected_result() in order_page.get_actual_result()
