import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    browser = webdriver.Firefox(capabilities={"marionette": True, "unexpectedAlertBehaviour": "dismiss"})
    #print(browser.capabilities)
    request.addfinalizer(browser.quit)
    return browser

def test_loggin(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    login = driver.find_element_by_name("username").send_keys("admin")
    passwort = driver.find_element_by_name("password").send_keys("admin")
    submit_button = driver.find_element_by_css_selector(".footer [type='submit']").click()
    #assert "My Store" in driver.title
    assert wait.until(EC.title_is("Countries | My Store"))

    editButton = driver.find_element_by_css_selector("form tr:nth-of-type(2) td:last-child").click()
    assert wait.until(EC.url_contains("app=countries"))

    numberOfWindows = driver.find_elements_by_css_selector("tbody form tr a")
    original_window= driver.current_window_handle
    print("Original" + original_window)

    for i in range(len(numberOfWindows)):
        numberOfWindow = driver.find_element_by_css_selector("tbody form tr a").click()
        wait.until(EC.number_of_windows_to_be(2))
        existing_windows = driver.window_handles
        print(existing_windows)
        #wait.until(lambda driver: len(original_window) != len(existing_windows))
        driver.switch_to_window(existing_windows[1])
        driver.close()
        driver.switch_to_window(original_window)
