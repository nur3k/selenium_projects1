from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from tivixlab.tests_frontend.Pages.locators import Locators


class Result:
    def __init__(self, driver):
        self.driver = driver

    def return_price_per_rent(self):
        return self.driver.find_element_by_xpath(Locators.x_price_per_rent)

    def return_price_per_day(self):
        return self.driver.find_element_by_xpath(Locators.x_price_per_day)

    def wait_for_resultpage_to_be_loaded(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(expected_conditions._element_if_visible(Locators.x_rent_btn))
        finally:
            return False
