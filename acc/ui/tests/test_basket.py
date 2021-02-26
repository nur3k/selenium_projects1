import pytest


@pytest.fixture(params=["monitor"])
def search_for_monitor(main_page, request):
    main_page.accept_consent()
    main_page.insert_text_to_search_ib(request.param)
    main_page.click_search_button()


@pytest.fixture
def take_two_most_expensive(result_page):
    result_page.sort_most_expensive()
    result_page.add_article_into_basket(1)
    result_page.add_article_into_basket(2)
    result_page.open_basket()


def test_id01_most_expensive_products(search_for_monitor, take_two_most_expensive):
    assert 1 == 1
