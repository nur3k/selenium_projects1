from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def get_webdriver(browser_name):
    if browser_name.lower() == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        return webdriver.Chrome(ChromeDriverManager().install(), options=options)
