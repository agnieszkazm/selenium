import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    browser=webdriver.Firefox()
    #print(browser.capabilities)
    request.addfinalizer(browser.quit)
    return browser

def test_loggin(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("http://localhost/litecart/admin")
    login=driver.find_element_by_name("username").send_keys("admin")
    passwort=driver.find_element_by_name("password").send_keys("admin")
    submit_button=driver.find_element_by_css_selector(".footer [type='submit']").click()
    #assert "My Store" in driver.title
    assert wait.until(EC.title_is("My Store"))

    menulenght = driver.find_elements_by_css_selector("ul#box-apps-menu li")
    submenulength = 0
    for i in range(len(menulenght)):
        menu = driver.find_elements_by_css_selector("ul#box-apps-menu li")[i+submenulength].click()
        submenulength = len(driver.find_elements_by_css_selector('ul#box-apps-menu ul li'))
        header1 = driver.find_element_by_css_selector("h1").text
        print(header1)

        for j in range(submenulength):
            submenu = driver.find_element_by_css_selector("ul#box-apps-menu ul li:nth-child(" + str(j + 1) + ")").click()
            header2 = driver.find_element_by_css_selector("h1").text
            print(header2)



