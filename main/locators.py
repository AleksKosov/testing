from selenium.webdriver.common.by import By


class Locators:
    TEXT_FIELD = (By.ID, "text")
    CLOSE_BUTTON = (By.CSS_SELECTOR, "div[aria-label='Закрыть']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")