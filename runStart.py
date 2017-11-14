import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver(request):
    #options = webdriver.ChromeOptions()
    #options.add_argument("start-maximized")
    #browser=webdriver.Chrome(chrome_options=options)
    browser = webdriver.Firefox(capabilities={"marionette": True, "unexpectedAlertBehaviour": "dismiss"})

    print(browser.capabilities)
    request.addfinalizer(browser.quit)
    return browser

def test_example(driver):
    driver.get("http://www.google.com/")
    assert "Google" in driver.title
    driver.find_element_by_name("q").send_keys("webdriver")
    driver.find_element_by_name("btnK").click()
    WebDriverWait(driver, 10).until(EC.title_is("webdriver - Szukaj w Google"))
