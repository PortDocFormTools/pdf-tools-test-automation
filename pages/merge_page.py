import config
from playwright.sync_api import Page
from pages.base_pdf_page import BasePDFPage
from pages.elements.base_element import BaseElement


class MergePage(BasePDFPage):
    def __init__(self, page: Page):
        super().__init__(page, "Merge page", url=config.MERGE_URL)
        self._merge_button = BaseElement(page, "#mergeBtn")

    def merge_button_is_clickable(self) -> bool:
        return self._merge_button.is_clickable()