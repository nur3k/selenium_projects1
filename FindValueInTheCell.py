import unittest
from selenium import webdriver


class SalarySearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.qtptutorial.net/automation-practice/")
        self.assertIn("Automation Testing Practice Page", driver.title)

        table = driver.find_element_by_id("htmlTableId")
        header = table.find_elements_by_tag_name("th")
        row = table.find_elements_by_tag_name("tr")

        index_of_column = 1
        index_of_row = 2
        DESIRED_HEADER = "Salary"
        DESIRED_ROW = "Automation Testing Architect"

        for i in range(len(header)):
            if header[i].text == DESIRED_HEADER:
                index_of_column = i + 1

        for i in range(len(row)):
            if row[i].text == DESIRED_ROW:
                index_of_row = i + 1

        xpath = '//tr[%d]//td[%d]' % (index_of_row, index_of_column)
        print(driver.find_element_by_xpath(xpath).text)


if __name__ == "__main__":
    unittest.main()
