from playwright.sync_api import Page
from pages.base_page import BasePage
from pages.elements.base_element import BaseElement
from pages.elements.tool_card import ToolCard


class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, "Home page")
        self._page = page
        self._header = BaseElement(page, "header")
        self._description = BaseElement.from_test_id(page, "page-subtitle")
        self.compress_tool_card = ToolCard(page, "compress")
        self.merge_tool_card = ToolCard(page, "merge")
        self.split_tool_card = ToolCard(page, "split")

    def is_opened(self) -> bool:
        return self._header.is_visible()

    def header_text(self) -> str:
        return self._header.text()

    def description_text(self) -> str:
        return self._description.text()
