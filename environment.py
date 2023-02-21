from browser import Browser
from pages.ebay_homepage import HomePage


def before_all(context):
    context.browser = Browser()
    context.home_page_object = HomePage()

def after_all(context):
    context.browser.close()