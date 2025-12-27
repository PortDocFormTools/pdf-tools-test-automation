
import allure
from pages.elements.base_element import BaseElement


class ToolCard:
    def __init__(self, page, tool_name: str):
        self._page = page
        self._card = BaseElement.from_test_id(self._page, f"card-{tool_name}")
        self._title = self._card.child("h3")
        self._open_button = self._card.child("a")

    def is_visible(self) -> bool:
        return self._card.is_visible()

    def title(self) -> str:
        return self._title.text()

    def open_is_clickable(self) -> bool:
        return self._open_button.is_visible() and self._open_button.is_enabled()

    @allure.step("Click Open button on {tool_name} tool card")
    def open(self):
        self._open_button.click()
