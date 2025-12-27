import allure
from playwright.sync_api import Page
from pages.home_page import HomePage
from fixtures.home_page_fixture import home_page_data


@allure.suite("HOME")
@allure.id("TC-HOME-1")
@allure.feature("Home Page")
@allure.tag("smoke")
def test_home_verify_page_contents(page: Page, home_page_data):
    # Precondition
    home_page = HomePage(page)
    home_page.navigate()
    with allure.step("Verify that Home Page is opened"):
        assert home_page.is_opened()

    # Step 1
    with allure.step("Verify page title/descriptionn"):
        assert home_page.title() == home_page_data["title"]
        assert home_page.header_text() == home_page_data["header"]
        assert home_page.description_text(
        ) == home_page_data["description"]

        # Step 2
    with allure.step("Verify Compress PDF card"):
        assert home_page.compress_tool_card.is_visible()
        assert home_page.compress_tool_card.title(
        ) == home_page_data["cards-titles"]["compress"]
        assert home_page.compress_tool_card.open_is_clickable()

    # Step 3
    with allure.step("Verify Merge PDF card"):
        assert home_page.merge_tool_card.is_visible()
        assert home_page.merge_tool_card.title(
        ) == home_page_data["cards-titles"]["merge"]
        assert home_page.merge_tool_card.open_is_clickable()

    # Step 4
    with allure.step("Verify Split PDF card"):
        assert home_page.split_tool_card.is_visible()
        assert home_page.split_tool_card.title(
        ) == home_page_data["cards-titles"]["split"]
        assert home_page.split_tool_card.open_is_clickable()
