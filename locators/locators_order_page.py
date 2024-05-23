from selenium.webdriver.common.by import By


class LocatorsOrderPage:

    PAGE1_TITLE = [By.XPATH, "//div[contains(@class, 'Order_Header')]"]  #Заголовок "Для кого самокат"
    FIRST_NAME = [By.XPATH, "//input[@placeholder='* Имя']"]  #Плейсхолдер "Имя"
    LAST_NAME = [By.XPATH, "//input[@placeholder='* Фамилия']"]  #Плейсхолдер "Фамилия"
    ADDRESS = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]  #Плейсхолдер "Адрес: куда привезти заказ"
    METRO_STATION = [By.XPATH, "//input[@placeholder='* Станция метро']"]  #Плейсхолдер "Станция метро"
    SELECT_STATION = [By.XPATH, "//div[text()='{}']"]  #Выбор станции
    PHONE_NUMBER = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]  #Плейсхолдер "Телефон"
    BUTTON_NEXT = [By.XPATH, "//button[text()='Далее']"]  #Кнопка "Далее"
    PAGE2_TITLE = [By.XPATH, "//div[@class='Order_Header__BZXOb']"]  #Заголовок "Про аренду"
    DELIVERY_DATE = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]  #Плейсхолдер "Когда привезти самокат"
    SELECT_DATE = [By.XPATH, "//div[contains(@class, 'react-datepicker__day--selected')]"]  #Выбор даты
    RENT_TIME = [By.XPATH, "//div[@class='Dropdown-placeholder']"]  #Плейсхолдер "Срок аренды"
    SELECT_RENT_TIME = [By.XPATH, ".//div[text()='{}']"]  #Выбор срока аренды
    CHECKBOX_COLOR = [By.ID, '{}']  #Чекбокс цвет самоката
    COMMENT = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]  #Плейсхолдер "Комментарий для курьера"
    BUTTON_ORDER = [By.XPATH, "(//button[text()='Заказать'])[2]"]  #Кнопка "Заказать"
    CONFIRM_ORDER = [By.XPATH, "//div[text()='Хотите оформить заказ?']"]  #Заголовок "Хотите оформить заказ?"
    BUTTON_YES = [By.XPATH, "//button[text()='Да']"]  #Кнопка "Да"
    COMPLETE_ORDER = [By.XPATH, "//div[text() = 'Заказ оформлен']"]  #Заголовок "Заказ оформлен"

