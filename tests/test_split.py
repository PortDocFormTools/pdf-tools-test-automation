import allure
from playwright.sync_api import Page
from pages.home_page import HomePage

@allure.parent_suite("PDF Tools")
@allure.suite("SPLIT")
@allure.id("1")
@allure.tag("smoke")
def test_split_verify_page_contents(page: Page):
    # Precondition
    home_page = HomePage(page)
    home_page.navigate()
    split_page = home_page.split_tool_card.open()
    
    # Step 1
    with allure.step("Verify that Split Page is opened"):
        assert split_page.is_opened()
        assert split_page.header_text() == "Split PDF"
        
    # Step 2
    with allure.step("Verify page elements"):
        assert split_page.back_home_link_is_clickable()
        assert split_page.drag_drop_zone_is_visible()
        assert split_page.choose_pdf_button_is_clickable()
        assert split_page.from_page_input_is_visible()
        assert split_page.from_page_input_is_enabled()
        assert split_page.to_page_input_is_visible()
        assert split_page.to_page_input_is_enabled()
        assert split_page.split_button_is_clickable()

    # Step 3
    with allure.step("Verify navigation back to Home Page"):
        split_page.click_back_home_link()
        assert home_page.is_opened()
