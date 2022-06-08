from selenium import webdriver
from main.locators import Locators
import time


class BasePage:
    def __init__(self):
        # self.capabilities = {
        #             "browserName": "chrome",
        #             "browserVersion": "100.0",
        #             "selenoid:options": {
        #                 "enableVNC": True,
        #                 "enableVideo": False
        #                 }
        #             }
        # self.browser = webdriver.Remote(command_executor="http://localhost:4444/wd/hub",
        #                                 desired_capabilities=self.capabilities)
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(60)
        self.browser.maximize_window()
        self.url = "https://yandex.ru/"

    def open_search_stroke(self):
        self.browser.get(self.url)
        time.sleep(3)

    def close_window(self):
        wd = self.browser
        wd.find_element(*Locators.CLOSE_BUTTON).click()

    def get_request(self):
        wd = self.browser
        wd.find_element(*Locators.TEXT_FIELD).send_keys('Python')
        wd.find_element(*Locators.SEARCH_BUTTON).click()

    def quit(self):
        self.browser.quit()
