from multiprocessing import context
from os import name
from typing import Self

from playwright.sync_api import Page
from pages.basepage import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page) -> None:
        super().__init__(page)
        self.page = page
        # self.base_page = BasePage(page)

    def open_given_url(self, url):
        self.page.goto(url, wait_until='networkidle')

    def read_page_title(self,expected_page_title):
        actual_page_title = self.page.title()
        assert actual_page_title == expected_page_title

    def check_registration_form_title(self, registration_form_title):
        actual_form_title = self.page.locator("//h3[contains(text(), 'Dummy Registration Form')]").inner_text()
        if actual_form_title:
            pass
        else:
            print("Form is not displayed")

    def click_field(self):
        self.name_field_xpath = "//input[@name='name']"
        self.click(self.name_field_xpath)

    def enter_field_value(self, field_value):
        self.enter_text(self.name_field_xpath, field_value)
        self.page.screenshot(path="screenshot.png", full_page=True)