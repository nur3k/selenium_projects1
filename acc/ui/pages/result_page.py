from selenium.webdriver.common.by import By


class ResultPage:
    DROPDOWN_SORT = (By.ID, "allegro.listing.sort")
    MOST_EXPENSIVE_OPTION = (By.CSS_SELECTOR, '[value="dd"]')
    NON_SPONSORED_REC = lambda self, idx: (
        By.CSS_SELECTOR, f"div.opbox-listing section:nth-child(3) article:nth-child({idx}) a")
    LOADING_ICON = (By.CSS_SELECTOR, '[data-role="loader"]')
    ADD_TO_BASKET = (By.ID, 'add-to-cart-button')
    BASKET = (By.CSS_SELECTOR, '[alt=Koszyk]')

    def __init__(self, wrapper):
        self.__wrapper = wrapper

    def click_on_sort(self):
        self.__wrapper.click_element(self.DROPDOWN_SORT)

    def sort_most_expensive(self):
        self.click_on_sort()
        self.__wrapper.click_element(self.MOST_EXPENSIVE_OPTION)
        self.__wrapper.wait_until_element_not_visible(self.LOADING_ICON)

    def add_article_into_basket(self, idx=0):
        self.__wrapper.open_element_in_new_tab(self.NON_SPONSORED_REC(idx))
        self.__wrapper.switch_tab(idx)
        self.__wrapper.click_element(self.ADD_TO_BASKET)
        self.__wrapper.switch_tab(0)

    def open_basket(self):
        self.__wrapper.click_element(self.BASKET)

