import unittest
from selenium import webdriver

from tivixlab.tests_frontend.Pages.HomePage import Home
from tivixlab.tests_frontend.Pages.ResultPage import Result


class QaLabTesting(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        inst.driver = webdriver.Chrome()
        inst.driver.get('http://qalab.pl.tivixlabs.com')
        inst.home = Home(inst.driver)
        inst.home.wait_for_homepage_to_be_loaded()
        inst.result = Result(inst.driver)

    def test_price_per_rent_calculation(self):
        days_to_calculate = 7
        self.home.insert_todays_pickup_date()
        self.home.insert_increased_dropoff_date(days_to_calculate)
        self.home.click_search_button()
        self.result.wait_for_resultpage_to_be_loaded()
        price_per_rent = self.result.return_price_per_rent()
        prices_per_day = self.result.return_price_per_day()
        assert price_per_rent == prices_per_day * days_to_calculate

    @classmethod
    def tearDownClass(inst):
        inst.driver.close()
        inst.driver.quit()


if __name__ == "__main__":
    unittest.main()
