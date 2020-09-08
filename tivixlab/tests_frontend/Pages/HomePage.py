from datetime import timedelta, datetime
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from tivixlab.tests_frontend.Pages.locators import Locators


class Home:
    def __init__(self, driver):
        self.driver = driver
        self.searchButton = self.driver.find_element_by_xpath(Locators.x_search_button)
        self.pickUpIb = self.driver.find_element_by_id(Locators.id_pickup_date)
        self.dropOffIb = self.driver.find_element_by_id(Locators.id_dropoff_date)

    def insert_todays_pickup_date(self):
        self.pickUpIb.send_keys(datetime.now().strftime("%d.%m.%Y"))

    def insert_increased_dropoff_date(self, days=7):
        self.dropOffIb.send_keys(datetime.now() + timedelta(days=days)).strftime("%d.%m.%Y")

    def click_search_button(self):
        self.searchButton.click()

    def wait_for_homepage_to_be_loaded(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(expected_conditions._element_if_visible(Locators.x_search_button))
        finally:
            return False
