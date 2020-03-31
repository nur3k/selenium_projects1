from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from tests_frontend.Pages.locators import Locators


class Home:
    def __init__(self, driver):
        self.driver = driver
        self.input_box = self.driver.find_element_by_xpath(Locators.x_search_inputbox)

    def insert_given_text(self, text):
        self.input_box.send_keys(text)

    def send_enter_button(self):
        self.input_box.send_keys(Keys.ENTER)

    def wait_for_homepage_to_be_loaded(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(expected_conditions._element_if_visible(Locators.id_google_logo))
        finally:
            return False
