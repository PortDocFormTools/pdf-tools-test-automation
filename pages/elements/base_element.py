class BaseElement:
    def __init__(self, page, locator):
        self.page = page
        self.locator = page.locator(locator)

    def click(self):
        self.locator.click()

    def text(self):
        return self.locator.text_content()
    

    def is_visible(self):
        return self.locator.is_visible()
