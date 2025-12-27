import config
from playwright.sync_api import Page
from pages.base_pdf_page import BasePDFPage
from pages.elements.base_element import BaseElement


class CompressPage(BasePDFPage):
    def __init__(self, page: Page):
        super().__init__(page, "Compress page", url=config.COMPRESS_URL)
        self._upload_and_compress_button = BaseElement(page, "#uploadBtn")

    def upload_and_compress_button_is_clickable(self) -> bool:
        return self._upload_and_compress_button.is_clickable()
