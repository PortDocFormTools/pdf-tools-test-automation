from playwright.sync_api import Page
import config


class BasePage:
    def __init__(self, page: Page, url: str = None):
        self.page = page
        self.url = url or config.BASE_URL

    def navigate(self):
        self.page.goto(self.url)

    def get_title(self) -> str:
        return self.page.title()
