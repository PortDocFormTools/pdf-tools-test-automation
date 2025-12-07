from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from pages.elements.base_element import BaseElement


def test_has_title(page: Page):
    base_page = BasePage(page)
    title = BaseElement(page, "#title")
    base_page.go_to("http://uitestingplayground.com/")

    # Expect a title "to contain" a substring.
    assert base_page.get_title() == "UI Test Automation Playground"
    assert title.is_visible()
