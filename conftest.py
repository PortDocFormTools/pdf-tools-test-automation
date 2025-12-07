import pytest
from playwright.sync_api import sync_playwright
import config

@pytest.fixture(scope="session")
def browser():
    opts = config.PLAYWRIGHT_OPTIONS
    with sync_playwright() as p:
        browser = getattr(p, opts["browser_type"]).launch(
            headless=opts["headless"],
            slow_mo=opts["slow_mo"],
            args=["--start-maximized"]
        )
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    yield page
    context.close()
