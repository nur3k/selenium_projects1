import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class AllegroSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver = webdriver.wait

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.google.pl")
        self.assertIn("Google", driver.title)

        elem = driver.find_element_by_name("q")
        elem.send_keys("allegro")
        elem.send_keys(Keys.RETURN)
        driver.implicitly_wait(5)

        elem = driver.find_element_by_tag_name(
            'h3')  # wybierz trzeci HEADER - pod tym indeksem pojawia sie pierwszy pokazany wynik wyszukania
        elem.click()
        driver.implicitly_wait(5)

        elem = driver.find_element_by_name("string")
        elem.send_keys("witcher")
        elem.send_keys(Keys.RETURN)
        driver.implicitly_wait(5)

        #   Select lista = new Select(driver.findElement(By.id("sort-select")));
        elem = driver.find_element_by_class_name("sort__sorting-list__btn__8xObu")
        elem.click()

        elem = driver.find_element_by_class_name("sort__sorting-method__2IDSZ")
        elem.click()
        driver.implicitly_wait(5)

        assert "No results found." not in driver.page_source


#   def tearDown(self):
#       self.driver.close()

if __name__ == "__main__":
    unittest.main()
