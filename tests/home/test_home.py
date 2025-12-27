from playwright.sync_api import Page
from pages.home_page import HomePage
from fixtures.home_page_fixture import home_page_data


def test_home_verify_page_contents(page: Page, home_page_data):
    # Precondition
    home_page = HomePage(page)
    home_page.navigate()
    assert home_page.is_opened()

    # Step 1
    assert home_page.get_title() == home_page_data["title"]
    assert home_page.get_header_text() == home_page_data["header"]
    assert home_page.get_description_text() == home_page_data["description"]

    # Step 2
    assert home_page.compress_tool_card.is_visible()
    assert home_page.compress_tool_card.get_title(
    ) == home_page_data["cards-titles"]["compress"]
    assert home_page.compress_tool_card.open_is_clickable()

    # Step 3
    assert home_page.merge_tool_card.is_visible()
    assert home_page.merge_tool_card.get_title(
    ) == home_page_data["cards-titles"]["merge"]
    assert home_page.merge_tool_card.open_is_clickable()

    # Step 4
    assert home_page.split_tool_card.is_visible()
    assert home_page.split_tool_card.get_title(
    ) == home_page_data["cards-titles"]["split"]
    assert home_page.split_tool_card.open_is_clickable()
