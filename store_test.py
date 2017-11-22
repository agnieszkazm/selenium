import pytest
import re
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

def test_store(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("http://localhost/litecart")
    #assert "Online Store | My Store" in driver.title
    assert wait.until(EC.title_is("Online Store | My Store"))
    for i in range(3):
        driver.find_elements_by_css_selector("#box-most-popular li")[i].click()
        #wait.until(EC.title_is("http://localhost/litecart/en/rubber-ducks-c-1/subcategory-c-2/yellow-duck-p-1"))
        try:
            addArticelArt = driver.find_element_by_css_selector('options [name="options[Size]"]').click()
            addArticelArtDropdown = driver.find_element_by_css_selector('options [name="options[Size]"] [value="Medium"]')
        except:
            pass

        cartCounterLocator = '#cart .quantity'
        cartCounter = driver.find_element_by_css_selector(cartCounterLocator)
        addToCart= driver.find_element_by_css_selector(".quantity [type='submit']").click()
        wait.until(EC.text_to_be_present_in_element(cartCounterLocator, str(i+1)))
        cartCounter
        assert(cartCounter == 1+i)

        driver.execute_script("window.history.go(-1)")


