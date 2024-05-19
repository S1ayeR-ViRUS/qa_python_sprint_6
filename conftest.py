import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    firefox_driver = webdriver.Firefox()
    yield firefox_driver
    firefox_driver.quit()