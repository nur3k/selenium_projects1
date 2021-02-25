from selenium.webdriver.common.by import By


class ResultPage:
    DROPDOWN_SORT = (By.ID, "allegro.listing.sort")
    MOST_EXPENSIVE_OPTION = (By.CSS_SELECTOR, '[value="dd"]')

    def __init__(self, wrapper):
        self.__wrapper = wrapper

    def click_on_sort(self):
        self.__wrapper.click_element(self.DROPDOWN_SORT)

    def sort_most_expensive(self):
        self.click_on_sort()
        self.__wrapper.click_element(self.MOST_EXPENSIVE_OPTION)