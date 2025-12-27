import allure
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.merge_page import MergePage


@allure.parent_suite("PDF Tools")
@allure.suite("MERGE")
@allure.id("1")
@allure.tag("smoke")
def test_merge_verify_page_contents(page: Page):
    # Precondition
    home_page = HomePage(page)
    home_page.navigate()
    merge_page = home_page.merge_tool_card.open()

    # Step 1
    with allure.step("Verify that Merge Page is opened"):
        assert merge_page.is_opened()
        assert merge_page.header_text() == "Merge PDF"

    # Step 2
    with allure.step("Verify page elements"):
        assert merge_page.back_home_link_is_clickable()
        assert merge_page.drag_drop_zone_is_visible()
        assert merge_page.choose_pdf_button_is_clickable()
        assert merge_page.merge_button_is_clickable()

    # Step 3
    with allure.step("Verify navigation back to Home Page"):
        merge_page.click_back_home_link()
        assert home_page.is_opened()
