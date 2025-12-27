from playwright.sync_api import Locator, Page


class BaseElement:
    def __init__(self, page: Page, locator: str | Locator):
        self.page = page
        self.locator = locator if isinstance(
            locator, Locator) else page.locator(locator)

    @classmethod
    def from_role(cls, page: Page, role: str, name: str = None) -> 'BaseElement':
        return cls(page, page.get_by_role(role, name=name))

    @classmethod
    def from_text(cls, page: Page, text: str) -> 'BaseElement':
        return cls(page, page.get_by_text(text))

    @classmethod
    def from_label(cls, page: Page, label: str) -> 'BaseElement':
        return cls(page, page.get_by_label(label))

    @classmethod
    def from_test_id(cls, page: Page, test_id: str) -> 'BaseElement':
        return cls(page, page.get_by_test_id(test_id))

    def child(self, selector: str) -> 'BaseElement':
        return BaseElement(self.page, self.locator.locator(selector))

    def child_by_role(self, role: str, name: str = None) -> 'BaseElement':
        return BaseElement(self.page, self.locator.get_by_role(role, name=name))

    def child_by_text(self, text: str) -> 'BaseElement':
        return BaseElement(self.page, self.locator.get_by_text(text))

    def child_by_label(self, label: str) -> 'BaseElement':
        return BaseElement(self.page, self.locator.get_by_label(label))

    def child_by_test_id(self, test_id: str) -> 'BaseElement':
        return BaseElement(self.page, self.locator.get_by_test_id(test_id))

    def click(self):
        self.locator.click()

    def text(self) -> str:
        return self.locator.inner_text().strip()

    def is_visible(self) -> bool:
        return self.locator.is_visible()

    def is_enabled(self) -> bool:
        return self.locator.is_enabled()

    def is_clickable(self) -> bool:
        return self.is_visible() and self.is_enabled()

    def upload_file(self, file_path: str):
        self.locator.set_input_files(file_path)
