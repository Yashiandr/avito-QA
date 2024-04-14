from playwright.sync_api import Page
import config


class IndexPage:

    def open_index_page(self, page: Page) -> None:
        page.goto(config.url.DOMAIN)

    def get_avito_ecocounter_div1(self, page: Page):
        self.open_index_page(page)
        return page.locator(config.elements.ECOCOUNTER_CO2)

    def get_avito_ecocounter_div2(self, page: Page):
        self.open_index_page(page)
        return page.locator(config.elements.ECOCOUNTER_WATER)

    def get_avito_ecocounter_div3(self, page: Page):
        self.open_index_page(page)
        return page.locator(config.elements.ECOCOUNTER_kWt)
