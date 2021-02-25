from selenium.webdriver.common.by import By


class MainPage:
    ACCEPT_CONSENT = (By.CSS_SELECTOR, "[data-role=accept-consent]")
    SEARCH_IB = (By.CSS_SELECTOR, '[type="search"]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '[data-role="search-button"]')

    def __init__(self, wrapper):
        self.__wrapper = wrapper

    def accept_consent(self):
        self.__wrapper.click_element(self.ACCEPT_CONSENT)

    def insert_text_to_search_ib(self, text):
        self.__wrapper.input_entry(self.SEARCH_IB, text)

    def click_search_button(self):
        self.__wrapper.click_element(self.SEARCH_BUTTON)