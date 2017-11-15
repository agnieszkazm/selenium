import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("start_maximized")
    browser = webdriver.Chrome(chrome_options=options)
    #print(browser.capabilities)
    request.addfinalizer(browser.quit)
    return browser

def test_alphabetical_order(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("http://localhost/litecart/admin")
    login = driver.find_element_by_name("username").send_keys("admin")
    passwort = driver.find_element_by_name("password").send_keys("admin")
    submit_button = driver.find_element_by_css_selector(".footer [type='submit']").click()
    #assert "My Store" in driver.title
    assert wait.until(EC.title_is("My Store"))

    mainMenu = driver.find_element_by_css_selector("ul#box-apps-menu li:nth-child(3)").click()
    assert wait.until(EC.url_contains("http://localhost/litecart/admin/?app=countries&doc=countries"))

#Creating list
    countryListlength = driver.find_elements_by_css_selector("[name=countries_form] td:nth-of-type(5) a")
    countryList = []
    for i in range(len(countryListlength)):
        countryName = driver.find_elements_by_css_selector("[name=countries_form] td:nth-of-type(5) a")[i].get_attribute("textContent")
        countryList.append(countryName)
        print(countryName)

#Checking alfabetical order
    for i in range(len(countryList)-1):
        if countryList[i] > countryList[i + 1]:
            result1 = False
            break
        else:
            result1 = True

    assert result1 == True

#Going to sublist
    sublistCheck = driver.find_elements_by_css_selector("[name=countries_form] td:nth-child(6)")

    for i in range(len(sublistCheck)):
        sublistCheckelement = driver.find_elements_by_css_selector("[name=countries_form] td:nth-child(6)")[i].get_attribute("textContent")
        if sublistCheckelement != "0":
            driver.find_elements_by_css_selector("[name=countries_form] td:nth-of-type(5) a")[i].click()
    #creating sublist

            subcountryListLenght = driver.find_elements_by_css_selector("#table-zones td:nth-child(3)")
            subcountryList = []
            for j in range(len(subcountryListLenght)):
                subcountryName = driver.find_elements_by_css_selector("#table-zones td:nth-child(3)")[j].text
                subcountryList.append(subcountryName)
                print(subcountryName)

     #checking alphabetical order
            for j in range(len(subcountryList)-1):
                if subcountryList[j] > subcountryList[j+1]:
                    result2 = False
                    break
                else:
                    result2 = True

                assert result2 == True

            driver.execute_script("window.history.go(-1)")

