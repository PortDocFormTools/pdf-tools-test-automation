import config
from playwright.sync_api import Page
from pages.base_pdf_page import BasePDFPage
from pages.elements.base_element import BaseElement


class SplitPage(BasePDFPage):
    def __init__(self, page: Page):
        super().__init__(page, "Split page", url=config.SPLIT_URL)
        self._split_button = BaseElement(page, "#splitBtn")
        self._split_range = BaseElement(page, ".split-range")
        self._from_page_input = self._split_range.child("#from")
        self._to_page_input = self._split_range.child("#to")

    def from_page_input_is_visible(self) -> bool:
        return self._from_page_input.is_visible()

    def from_page_input_is_enabled(self) -> bool:
        return self._from_page_input.is_enabled()

    def to_page_input_is_visible(self) -> bool:
        return self._to_page_input.is_visible()

    def to_page_input_is_enabled(self) -> bool:
        return self._to_page_input.is_enabled()
        
    def split_button_is_clickable(self) -> bool:
        return self._split_button.is_clickable()