import pytest

import config
from playwright.sync_api import Browser, BrowserContext, Page, sync_playwright


@pytest.fixture()
def page(browser) -> [Page, str]:
    playwright = sync_playwright().start()
    if browser == 'firefox':
        browser = get_firefox_browser(playwright)
        context = get_context(browser)
        page_data = context.new_page()
        browserName = 'firefox'
    elif browser == 'chromium':
        browser = get_chrome_browser(playwright)
        context = get_context(browser)
        page_data = context.new_page()
        browserName = 'chrome'
    elif browser == 'webkit':
        browser = get_webkit_browser(playwright)
        context = get_context(browser)
        page_data = context.new_page()
        browserName = 'webkit'
    else:
        browser = get_chrome_browser(playwright)
        context = get_context(browser)
        page_data = context.new_page()
        browserName = 'chrome'
    yield [page_data, browserName]
    for context in browser.contexts:
        context.close()
    browser.close()
    playwright.stop()


def get_firefox_browser(playwright) -> Browser:
    return playwright.firefox.launch(
        headless=config.headless.ENABLE,
        slow_mo=50,
    )

def get_webkit_browser(playwright) -> Browser:
    return playwright.webkit.launch(
        headless=config.headless.ENABLE,
        slow_mo=50,
    )


def get_chrome_browser(playwright) -> Browser:
    return playwright.chromium.launch(
        headless=config.headless.ENABLE,
        slow_mo=50
    )


def get_context(browser) -> BrowserContext:
    resolution = config.screenResolution.R1920x1080
    context = browser.new_context(
        viewport={"width": int(resolution.split('x')[0]), "height": int(resolution.split('x')[1])},
        locale="ru_RU"
    )
    context.set_default_timeout(
        timeout=config.expectations.DEFAULT_TIMEOUT
    )
    return context
