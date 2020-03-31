from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from tests_frontend.Pages.locators import Locators


class Result:
    def __init__(self, driver):
        self.driver = driver

    def return_how_many_findings_str(self):
        findings_str = self.driver.find_element_by_id(Locators.id_result_stats).text
        findings_str = findings_str.split()
        return findings_str[1]

    def return_how_many_findings_displayed(self):
        count = len(self.driver.find_elements_by_xpath(Locators.x_displayed_record))
        return count

    def return_how_many_images_displayed(self):
        count = len(self.driver.find_elements_by_xpath(Locators.x_displayed_images))
        return count

    def wait_for_resultpage_to_be_loaded(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(expected_conditions._element_if_visible(Locators.id_result_stats))
        finally:
            return False
