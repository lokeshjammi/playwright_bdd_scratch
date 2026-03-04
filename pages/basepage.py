class BasePage:
    def __init__(self, page) -> None:
        self.page = page

    def click(self, locator):
        self.page.locator(locator).click()

    def enter_text(self, locator, text):
        self.page.locator(locator).fill(text)