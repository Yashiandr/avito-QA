import pytest
import pages
import config


def test_get_screenshot_ecocounter_CO2(page):
    (pages.index_page.get_avito_ecocounter_div1(page[0])
     .screenshot(path=f"output/EcoCounter_CO2_{config.screenResolution.R1920x1080}_{page[1]}.png"))


def test_get_screenshot_ecocounter_water(page):
    (pages.index_page.get_avito_ecocounter_div2(page[0])
     .screenshot(path=f"output/EcoCounter_Water_{config.screenResolution.R1920x1080}_{page[1]}.png"))


def test_get_screenshot_ecocounter_kWt(page):
    (pages.index_page.get_avito_ecocounter_div3(page[0])
     .screenshot(path=f"output/EcoCounter_kWt_{config.screenResolution.R1920x1080}_{page[1]}.png"))
