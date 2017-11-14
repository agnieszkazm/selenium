import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    browser=webdriver.Firefox()
    # print(browser.capabilities)
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

    #table = driver.find_element_by_id("box-apps-menu")
    apps = driver.find_elements_by_css_selector("ul#box-apps-menu li")
    doc = 0
    for i in range(len(apps)):
        #table = driver.find_element_by_id("box-apps-menu")
        #doc = driver.find_elements_by_css_selector('ul#box-apps-menu ul li')
        app1=driver.find_elements_by_css_selector("ul#box-apps-menu li")[i+doc].click()
        doc = len(driver.find_elements_by_css_selector('ul#box-apps-menu ul li'))
        naglowek1 = driver.find_element_by_css_selector("h1").text
        print(naglowek1)
        #app1.click()


       # if doc > 0:
        for j in range(doc):
            doc1 = driver.find_element_by_css_selector("ul#box-apps-menu ul li:nth-child(" + str(j + 1) + ")").click()
            #table = driver.find_element_by_id("box-apps-menu")
            # apps = table.find_elements_by_tag_name("li")[i]
            #driver.find_element_by_css_selector("ul#box-apps-menu ul li:nth-child(" + str(j + 1) + ")").click()
            naglowek2 = driver.find_element_by_css_selector("h1").text
            print(naglowek2)
            #doc1.click()


