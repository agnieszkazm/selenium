import pytest
import re
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


@pytest.fixture
def driver(request):
    browser = webdriver.Chrome()
    #print(browser.capabilities)
    request.addfinalizer(browser.quit)

    return browser

def test_store(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("http://localhost/litecart")
    #assert "Online Store | My Store" in driver.title
    assert wait.until(EC.title_is("Online Store | My Store"))
    for i in range(3):
        driver.find_elements_by_css_selector("#box-most-popular li")[i].click()
        #wait.until(EC.title_is("http://localhost/litecart/en/rubber-ducks-c-1/subcategory-c-2/yellow-duck-p-1"))
        try:
            addArticelArt = driver.find_element_by_css_selector('.options [name="options[Size]"]').click()
            addArticelArtDropdown = driver.find_element_by_css_selector('.options [name="options[Size]"] [value="Medium"]').click()
        except:
            pass


        cartCounter = driver.find_element_by_css_selector('#cart .quantity')
        addToCart= driver.find_element_by_css_selector(".quantity [type='submit']").click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#cart .quantity'), str(i+1)))
        cartCounter
        assert(cartCounter.text == str(1+i))

        driver.execute_script("window.history.go(-1)")

    basket = driver.find_element_by_css_selector("#cart .link").click()
    assert wait.until(EC.title_is("Checkout | My Store"))
    for i in range(3):
        remove_button = driver.find_elements_by_css_selector("#box-checkout-cart [name='remove_cart_item']")[0]
        #wait.until(EC.visibility_of(remove_button))
        remove_button.click()
        wait.until(EC.staleness_of(driver.find_element_by_css_selector('.dataTable')))