import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    browser = webdriver.Firefox()
    print(browser.capabilities)
    request.addfinalizer(browser.quit)
    return browser



def test_loggin(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("http://localhost/litecart/admin")
    loggin=driver.find_element_by_name("username").send_keys("admin")
    passwort=driver.find_element_by_name("password").send_keys("admin")
    submit_button=driver.find_element_by_css_selector(".footer [type='submit']").click()
    wait.until(EC.title_is("My Store"))


    table=driver.find_element_by_id("box-apps-menu")
    apps=table.find_elements_by_tag_name("li")
    for i in range(len(apps)):
        table.find_elements_by_tag_name("li")[i]
        doc=table.find_elements_by_css_selector('ul li')
        for j in range(len(doc)):
            table = driver.find_element_by_id("box-apps-menu")
            apps = table.find_elements_by_tag_name("li")[i]
            table.find_elements_by_css_selector('ul li')[j].click()
            naglowek2=driver.find_element_by_tag_name("h1").text
            print(naglowek2)

