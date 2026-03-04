from behave import *
from Utilities.config_reader import read_config_file
from pages.RegistrationPage import RegistrationPage

@given(u'I am on the way2automation.com homepage')
def step_impl(context):
    url = read_config_file('basic_info', 'url')
    page = context.page
    context.registration_page = RegistrationPage(page)
    context.registration_page.open_given_url(url)

@when(u'page title is displayed as "{page_title}"')
def step_impl(context, page_title):
    context.registration_page.read_page_title(page_title)

@then('Check for the display of registration form with title "{registration_form_title}"')
def step_impl(context, registration_form_title):
    context.registration_page.check_registration_form_title(registration_form_title)

@then('Click on name field')
def step_impl(context):
    context.registration_page.click_field()

@then('enter name field value as "{field_value}"')
def step_impl(context, field_value):
    context.registration_page.enter_field_value(field_value)