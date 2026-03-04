from multiprocessing import context
from typing import Self
from pages.basepage import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page) -> None:
        super().__init__(page)
        self.page = page

    def open_given_url(self, url):
        self.page.goto(url, wait_until='networkidle')

    def read_page_title(self,expected_page_title):
        actual_page_title = self.page.title()
        assert actual_page_title == expected_page_title        