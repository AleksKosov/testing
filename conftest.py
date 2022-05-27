from selenium import webdriver
from main.base_page import BasePage
import pytest


@pytest.fixture(scope='session')
def app():
    driver = BasePage()
    yield driver
    driver.quit()
    return driver
