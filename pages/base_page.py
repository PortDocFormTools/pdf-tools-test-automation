import allure
from playwright.sync_api import Page
import config


class BasePage:
    def __init__(self, page: Page, name: str, url: str = None):
        self.page = page
        self.name = name
        self.url = url or config.BASE_URL
        if not self.url:
            raise ValueError(f"URL for page '{self.name}' is not set.")

    def navigate(self):
        with allure.step(f"Navigate to {self.name} page by URL: {self.url}"):
            self.page.goto(self.url)

    def title(self) -> str:
        return self.page.title()
