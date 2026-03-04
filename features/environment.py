import configparser
import os
from playwright.sync_api import sync_playwright
from Utilities.config_reader import read_config_file

config = read_config_file('basic_info', 'url')


def before_scenario(context, scenario):
    context.play_wright = sync_playwright().start()
    browser = read_config_file('basic_info', 'browser')
    if browser == 'chrome':
        context.browser = context.play_wright.chromium.launch(headless=True)
        context.page = context.browser.new_page(viewport={'width': 1920, 'height': 1080})

def after_scenario(context, scenario):
    context.page.close()