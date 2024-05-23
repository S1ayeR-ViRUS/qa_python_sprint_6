from selenium.webdriver.common.by import By


class LocatorsBasePage:

    LOGO_YANDEX = [By.XPATH, "//a[@href='//yandex.ru']"]  #Логотип "Яндекс"
    LOGO_SCOOTER = [By.XPATH, "//a[@href='/']"]  #Логотип "Самокат"