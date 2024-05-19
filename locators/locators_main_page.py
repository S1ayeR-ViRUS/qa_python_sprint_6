from selenium.webdriver.common.by import By


class LocatorsMainPage:
    PAGE_TITLE = [By.XPATH, "//div[contains(@class, 'Home_Header')]"]  #Заголовок страницы "Самокат на пару дней"
    FAQ_LIST = [By.CLASS_NAME, "accordion"]  #Блок FAQ
    FAQ_QUESTION = [By.XPATH, "(//div[@class='accordion__button'])[{}]"]  #Текст вопроса
    FAQ_ANSWER = [By.XPATH, "(//div[@class='accordion__panel'])[{}]"]  #Текст ответа
    HEADER_ORDER_BUTTON = [By.XPATH, "(//button[text()='Заказать'])[1]"]  #Кнопка заказать сверху
    FOOTER_ORDER_BUTTON = [By.XPATH, "(//button[text()='Заказать'])[2]"]  #Кнопка заказать снизу