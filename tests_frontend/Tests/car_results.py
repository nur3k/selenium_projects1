import unittest
from selenium import webdriver

from tests_frontend.Pages.HomePage import Home
from tests_frontend.Pages.ResultPage import Result


class GoogleTesting(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        inst.driver = webdriver.Chrome()
        inst.driver.get('https://google.com')
        inst.home = Home(inst.driver)
        inst.home.wait_for_homepage_to_be_loaded()
        inst.home.insert_given_text("samochód")
        inst.home.send_enter_button()

        inst.result = Result(inst.driver)
        inst.result.wait_for_resultpage_to_be_loaded()

    def test_records_how_many_findings(self):
        result_text = self.result.return_how_many_findings_str()
        output = "Found about {} results".format(result_text)
        print(output)

    def test_how_many_records_displayed(self):
        records = self.result.return_how_many_findings_displayed()
        image_records = self.result.return_how_many_images_displayed()
        print("Displayed {} records".format(records))
        assert records == 10, "There are less than 10 records \n" \
                              "Found as well {} images".format(image_records)

    def test_are_there_any_pictures_displayed(self):
        image_records = self.result.return_how_many_images_displayed()
        assert image_records > 0

    @classmethod
    def tearDownClass(inst):
        inst.driver.close()
        inst.driver.quit()


if __name__ == "__main__":
    unittest.main()
