import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time


@pytest.fixture
def driver(request):
    d = DesiredCapabilities.CHROME
    d['loggingPrefs'] = {'browser': 'ALL'}
    browser = webdriver.Chrome(desired_capabilities=d)
    #browser = webdriver.Chrome()
    #print(browser.capabilities)
    request.addfinalizer(browser.quit)
    return browser

def test(driver):
    #driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 10)
    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
    login = driver.find_element_by_name("username").send_keys("admin")
    passwort = driver.find_element_by_name("password").send_keys("admin")
    submit_button = driver.find_element_by_css_selector(".footer [type='submit']").click()
    #assert "My Store" in driver.title
    assert wait.until(EC.title_is("Catalog | My Store"))

    menulenght = driver.find_elements_by_css_selector(".dataTable tr.row")
    # menu = driver.find_elements_by_css_selector(".dataTable tr.row td:nth-of-type(3) a")[3].click()
    # time.sleep(3)
    for i in range(3, len(menulenght)):
        menu = driver.find_elements_by_css_selector(".dataTable tr.row td:nth-of-type(3) a")[i].click()
        header = driver.find_element_by_css_selector("h1")
        if wait.until(EC.title_contains("Edit Product")):
            for l in driver.get_log("browser"):
                print(l)
            driver.execute_script("window.history.go(-1)")
        else:
            continue





