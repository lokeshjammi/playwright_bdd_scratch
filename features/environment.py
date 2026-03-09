import allure
from playwright.sync_api import sync_playwright
from Utilities.config_reader import read_config_file

config = read_config_file('basic_info', 'url')


def before_scenario(context, scenario):
    context.play_wright = sync_playwright().start()
    browser = read_config_file('basic_info', 'browser')
    if browser == 'chrome':
        context.browser = context.play_wright.chromium.launch(headless=False)
        context.page = context.browser.new_page(viewport={'width': 1920, 'height': 1080})
    allure.dynamic.feature(scenario.feature.name)
    allure.dynamic.title(scenario.name)

def after_step(context, step):
    if step.status == 'failed':
        screenshot_taken = context.page.screenshot()
        allure.attach(screenshot_taken, name='failure_screenshot', attachment_type=allure.attachment_type.PNG)

def after_scenario(context, scenario):
    context.page.close()