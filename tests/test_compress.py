import allure
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.compress_page import CompressPage


@allure.parent_suite("PDF Tools")
@allure.suite("COMPRESS")
@allure.id("1")
@allure.tag("smoke")
def test_compress_verify_page_contents(page: Page):
    # Precondition
    home_page = HomePage(page)
    home_page.navigate()
    compress_page =home_page.compress_tool_card.open()

    # Step 1
    with allure.step("Verify that Compress Page is opened"):
        assert compress_page.is_opened()
        assert compress_page.header_text() == "Compress PDF"

    # Step 2
    with allure.step("Verify page elements"):
        assert compress_page.back_home_link_is_clickable()
        assert compress_page.drag_drop_zone_is_visible()
        assert compress_page.choose_pdf_button_is_clickable()
        assert compress_page.upload_and_compress_button_is_clickable()

    # Step 3
    with allure.step("Verify navigation back to Home Page"):
        compress_page.click_back_home_link()
        assert home_page.is_opened()
