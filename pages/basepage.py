class BasePage:
    def __init__(self, page) -> None:
        self.page = page

    def click(self, locator):
        self.page.locator(locator).click()