import pytest
import allure
from playwright.sync_api import sync_playwright
from allure_commons.types import AttachmentType
import config


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


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
def page(browser, request):
    context = browser.new_context(no_viewport=True)
    page = context.new_page()

    yield page

    if request.node.rep_call.failed:
        allure.attach(
            page.screenshot(),
            name="Screenshot on failure",
            attachment_type=AttachmentType.PNG,
        )
        allure.attach(
            page.url,
            name="Page URL",
            attachment_type=AttachmentType.TEXT,
        )

    context.close()
