"""General fixtures for pytest framework"""

import pytest

from .constants import Constants
from .driver_wrapper import DriverWrapper
from .pages.main_page import MainPage
from .pages.result_page import ResultPage
from .webdriver_factory import get_webdriver


@pytest.fixture(scope='module')
def browser():
    """Driver initialization with wrapper"""
    driver = get_webdriver(Constants.BROWSER)
    driver.get(Constants.URL)
    res = DriverWrapper(driver)
    yield res
    driver.quit()


@pytest.fixture(scope='module')
def main_page(browser):
    yield MainPage(browser)


@pytest.fixture(scope='module')
def result_page(browser):
    yield ResultPage(browser)
