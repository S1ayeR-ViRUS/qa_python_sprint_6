import allure
from data import Url
from locators.locators_main_page import LocatorsMainPage
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Открываем главуню страницу')
    def open_main_page(self):
        self.open_page(Url.MAIN_PAGE)

    @allure.step('Скроллим до блока "Вопросы о важном", ожидаем загрузку блока')
    def scroll_to_block(self):
        self.scroll_to_element(LocatorsMainPage.FAQ_LIST)
        self.wait_for_load_element(LocatorsMainPage.FAQ_LIST)

    @allure.step('Получаем текст вопроса в блоке "Вопросы о важном"')
    def click_on_question(self, index):
        method, locator = LocatorsMainPage.FAQ_QUESTION
        locator = locator.format(index)
        self.wait_for_load_element((method, locator))
        question = self.find_element((method, locator))
        question.click()
        return question.text

    @allure.step('Получаем текст ответа в блоке "Вопросы о важном"')
    def get_answer(self, index):
        method, locator = LocatorsMainPage.FAQ_ANSWER
        locator = locator.format(index)
        self.wait_for_load_element((method, locator))
        return self.find_element((method, locator)).text

    @allure.step('Получаем ожидаемый URL главной страницы')
    def get_url_main_page(self):
        return Url.MAIN_PAGE

    @allure.step('Ожидаем загрузку заголовка "Самокат на пару дней" на главной странице')
    def wait_for_load_page_title(self):
        self.wait_for_load_element(LocatorsMainPage.PAGE_TITLE)
