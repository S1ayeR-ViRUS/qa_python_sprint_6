import allure
import pytest
from locators.locators_main_page import LocatorsMainPage
from pages.main_page import MainPage
from data import MainPageData


class TestMainPage:
    @allure.title('Проверяем выпадающий список в блоке "Вопросы о важном"')
    @allure.description('Проверяем, что по клику вопрос, открывается соответсвующий ответ')
    @pytest.mark.parametrize('index, question, answer', MainPageData.FAQ)
    def test_check_question_and_answer(self, driver, index, question, answer):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.scroll_to_block()
        question_received = main_page.click_on_question(index)
        answer_received = main_page.get_answer(index)
        assert question_received == question
        assert answer_received == answer

    @allure.title('Проверяем кнопки "Заказать" на Главной странице')
    @allure.description('Проверяем, что по клику на кнопку "Заказать" на главной странице, открывается страница заказа')
    @pytest.mark.parametrize('locator', [LocatorsMainPage.HEADER_ORDER_BUTTON, LocatorsMainPage.FOOTER_ORDER_BUTTON])
    def test_click_order_button(self, driver, locator):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.scroll_to_element(locator)
        main_page.wait_for_load_element(locator)
        main_page.click_element(locator)
        main_page.wait_for_load_form()
        expected_url = main_page.get_url_order_page()
        assert driver.current_url == expected_url
