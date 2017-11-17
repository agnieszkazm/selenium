import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


@pytest.fixture
def driver(request):
    browser = webdriver.Chrome()
    #print(browser.capabilities)
    request.addfinalizer(browser.quit)
    return browser

def test_loggin(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("http://localhost/litecart/admin")
    login = driver.find_element_by_name("username").send_keys("admin")
    passwort = driver.find_element_by_name("password").send_keys("admin")
    submit_button = driver.find_element_by_css_selector(".footer [type='submit']").click()
    #assert "My Store" in driver.title
    assert wait.until(EC.title_is("My Store"))

# General tab
    catalog = driver.find_element_by_css_selector("ul#box-apps-menu li:nth-child(2)").click()
    product_page = driver.find_element_by_css_selector("#content .button:nth-child(2)").click()
    enable_check = driver.find_element_by_xpath(".//*[@id='tab-general']/table/tbody/tr[1]/td/label[1]/input").get_attribute("checked")
    if enable_check in (None, False):
        enable = driver.find_element_by_xpath(".//*[@id='tab-general']/table/tbody/tr[1]/td/label[1]/input").click()
    name = driver.find_element_by_css_selector('tbody [name="name[en]"]').send_keys("SuperDuck" + Keys.TAB + "SD")
    prod_group = driver.find_element_by_xpath(".//*[@id='tab-general']/table/tbody/tr[7]/td/div/table/tbody/tr[2]/td[1]/input").click()
    quantity = driver.find_element_by_css_selector("tbody [name=quantity]").send_keys("100")
    date_from = driver.find_element_by_css_selector("tbody [name=date_valid_from]").send_keys("11/17/2017" + Keys.TAB + "12/31/2017")

# Information tab
    info_tab = driver.find_element_by_css_selector('form [href="#tab-information"]').click()
    manufacturer = driver.find_element_by_css_selector('tbody [name="manufacturer_id"]').click()
    select_manufact = driver.find_element_by_css_selector('tbody [name="manufacturer_id"] option:last-child').click()
    text_fields = driver.find_element_by_css_selector('tbody [name="keywords"]').send_keys("SuperDuck, female" + Keys.TAB + "groovy female super duck" + Keys.TAB + "New female SuperDuck inspired by comicbook super heros. A must-have for Wonder Woman fans :-)" + Keys.TAB + "SuperDuck - super hero help" + Keys.TAB + "SuperDuck - super fun")

# Prices tab
    info_tab = driver.find_element_by_css_selector('form [href="#tab-prices"]').click()
    purchase_price = driver.find_element_by_css_selector('#tab-prices [name=purchase_price]').send_keys(Keys.DELETE + "25")
    currency_click = driver.find_element_by_css_selector('tbody [name="purchase_price_currency_code"]').click()
    currency = driver.find_element_by_css_selector('tbody [name="purchase_price_currency_code"] option:last-child').click()
    gross_usd = driver.find_element_by_css_selector('#tab-prices [name="gross_prices[USD]"]').send_keys(Keys.DELETE + "30")
    gross_eur = driver.find_element_by_css_selector('#tab-prices [name="gross_prices[EUR]"]').send_keys(Keys.DELETE + "25")
    #time.sleep(2)
# Save product
    save = driver.find_element_by_css_selector('.button-set [name=save]').click()
    #time.sleep(3)
# Check if product is added
    assert driver.find_element_by_css_selector(".notice.success")
    #time.sleep(3)