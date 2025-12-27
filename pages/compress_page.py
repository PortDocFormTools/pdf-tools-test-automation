import config
import allure
from playwright.sync_api import Page
from pages.base_page import BasePage
from pages.elements.base_element import BaseElement


class CompressPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, "Compress page", url=config.COMPRESS_URL)
        self._page = page
        self._header = BaseElement.from_test_id(page, "page-title")
        self._back_home_link = BaseElement.from_test_id(page, "back-home")
        self._drag_drop_zone = BaseElement(page, "#dropZone")
        self._choose_pdf_button = self._drag_drop_zone.child(".file-btn")
        self._upload_and_compress_button = BaseElement(page, "#uploadBtn")

    def is_opened(self) -> bool:
        return self._header.is_visible()

    def header_text(self) -> str:
        return self._header.text()

    def back_home_link_is_clickable(self) -> bool:
        return self._back_home_link.is_clickable()

    @allure.step("Click Back Home link")
    def click_back_home_link(self):
        self._back_home_link.click()

    def drag_drop_zone_is_visible(self) -> bool:
        return self._drag_drop_zone.is_visible()

    def choose_pdf_button_is_clickable(self) -> bool:
        return self._choose_pdf_button.is_clickable()

    def upload_and_compress_button_is_clickable(self) -> bool:
        return self._upload_and_compress_button.is_clickable()
