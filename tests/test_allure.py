import allure
from playwright.sync_api import Page
from pages.home_page import HomePage


@allure.parent_suite("Allure Verification")
@allure.suite("ALLURE")
@allure.feature("Allure Reporting")
def test_allure_verify_screenshot_on_fail(page: Page):
    home_page = HomePage(page)
    home_page.navigate()
    with allure.step("Verify screenshot on failed step"):
        assert home_page.title() == "Title"
