import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest


@pytest.fixture
def driver(request):
    browser = webdriver.Chrome()
    #print(browser.capabilities)
    request.addfinalizer(browser.quit)
    return browser

def test_loggin(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("http://localhost/litecart/en/")

    yellowDuckFirstPage = driver.find_element_by_css_selector("#box-campaigns .product ")

    productTitleFirstPageElement = driver.find_element_by_css_selector("#box-campaigns .product .name").get_attribute("textContent")

    productRegularPriceFirstPageElement = driver.find_element_by_css_selector("#box-campaigns .product .regular-price")
    productRegularPriceFirstPage = productRegularPriceFirstPageElement.get_attribute("textContent")
    productRegularPriceFirstPageColor = productRegularPriceFirstPageElement.value_of_css_property("color")
    productRegularPriceFirstPageTextDecor = productRegularPriceFirstPageElement.value_of_css_property("text-decoration-line")

    productCampaignPriceFirstPageElement = driver.find_element_by_css_selector("#box-campaigns .product .campaign-price")
    productCampaignPriceFirstPage = productCampaignPriceFirstPageElement.get_attribute("textContent")
    productCampaignPriceFirstPageColor = productCampaignPriceFirstPageElement.value_of_css_property("color")
    productCampaignPriceFirstPageFontWeight = productCampaignPriceFirstPageElement.value_of_css_property("font-weight")

    yellowDuckFirstPage.click()

    productTitleSecondPageElement = driver.find_element_by_css_selector("#box-product .title").get_attribute("textContent")

    productRegularPriceSecondPageElement = driver.find_element_by_css_selector("#box-product .regular-price")
    productRegularPriceSecondPage = productRegularPriceSecondPageElement.get_attribute("textContent")
    productRegularPriceSecondPageColor = productRegularPriceSecondPageElement.value_of_css_property("color")
    productRegularPriceSecondPageTextDecor = productRegularPriceSecondPageElement.value_of_css_property(
        "text-decoration-line")

    productCampaignPriceSecondPageElement = driver.find_element_by_css_selector(
        "#box-product .campaign-price")
    productCampaignPriceSecondPage = productCampaignPriceSecondPageElement.get_attribute("textContent")
    productCampaignPriceSecondPageColor = productCampaignPriceSecondPageElement.value_of_css_property("color")
    productCampaignPriceSecondPageFontWeight = productCampaignPriceSecondPageElement.value_of_css_property("font-weight")

    assert productTitleFirstPageElement == productTitleSecondPageElement
    assert productRegularPriceFirstPage == productRegularPriceSecondPage
    assert productRegularPriceFirstPageColor == productRegularPriceSecondPageColor
    assert productRegularPriceFirstPageTextDecor == productRegularPriceSecondPageTextDecor
    assert productCampaignPriceFirstPage == productCampaignPriceSecondPage
    assert productCampaignPriceFirstPageColor == productCampaignPriceSecondPageColor
    assert productCampaignPriceFirstPageFontWeight == productCampaignPriceSecondPageFontWeight
