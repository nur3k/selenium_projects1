"""This module contains methods for wrapping Selenium"""
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

TIMEOUT = 20
TIMEOUT_SHORT = 3


class DriverWrapper():
    """Webdriver wrapper"""

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator, wait_type=EC.presence_of_element_located, timeout=TIMEOUT):
        """Returns element for the specific locator"""
        try:
            WebDriverWait(self.driver, timeout).until(wait_type(locator))
        except TimeoutException:
            raise TimeoutException(f"Cannot find element {locator}")
        return self.driver.find_element(*locator)

    def get_elements(self, locator, wait_type=EC.presence_of_all_elements_located, timeout=TIMEOUT):
        """Returns element for the specific locator"""
        try:
            WebDriverWait(self.driver, TIMEOUT).until(wait_type(locator))
        except TimeoutException:
            raise TimeoutException(f"Cannot find element {locator}")
        return self.driver.find_elements(*locator)

    def click_element(self, locator, number=0):
        """Clicks on the element with specific locator"""
        self.get_elements(locator, wait_type=EC.presence_of_all_elements_located)[number].click()

    def input_entry(self, locator, entry, index=0):
        """Enters data into textbox"""
        elements = self.get_elements(locator)
        elements[index].send_keys(entry)

    def open_element_in_new_tab(self, locator):
        element = self.get_element(locator)
        element.send_keys(Keys.CONTROL + Keys.ENTER)

    def switch_tab(self, idx=0):
        self.driver.switch_to.window(self.driver.window_handles[idx])

    def close_active_tab(self):
        self.driver.close()

    def wait_until_element_not_visible(self, locator):
        WebDriverWait(self.driver, TIMEOUT).until(EC.invisibility_of_element_located(locator))
