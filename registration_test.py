import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import random



@pytest.fixture
def driver(request):
    browser = webdriver.Chrome()
    #print(browser.capabilities)
    request.addfinalizer(browser.quit)
    return browser

def test_registration(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("http://localhost/litecart/en/")

    newCustomer = driver.find_element_by_css_selector("[name = login_form] a").click()
    assert wait.until(EC.url_matches("http://localhost/litecart/en/create_account"))

#start data
    email_random = str(random.randint(1000, 9999))+"@gmail.com"

#fill fields
    first_name = driver.find_element_by_css_selector("form [name = firstname]").send_keys("Jan")
    last_name = driver.find_element_by_css_selector("form [name = lastname]").send_keys("Kowalski")
    address1 = driver.find_element_by_xpath("//form[@name='customer_form']/table/tbody/tr[3]/td[1]/input").send_keys("Bobrza 12")
    postcode = driver.execute_script("return document.querySelector('form [name = postcode]')").send_keys("55-100")
    #postcode = driver.find_element_by_css_selector("form [name = postcode]").send_keys("55-100")
    city = driver.find_element_by_css_selector("form [name = city]").send_keys("Testowe Miasto")
    country = driver.find_element_by_css_selector("form tr:nth-child(5) td:first-of-type").click()
    country_input = driver.find_element_by_css_selector(".select2-search__field").send_keys("Poland"+ Keys.ENTER)
    email = driver.find_element_by_css_selector("form [name = email]").send_keys(email_random)
    phone_number = driver.find_element_by_css_selector("form [name = phone]").send_keys("+48 555 666 777 888")
    password = driver.find_element_by_css_selector("form [name = password").send_keys("Abc123")
    password_confirme = driver.find_element_by_css_selector("form [name = confirmed_password").send_keys("Abc123")

    submit_button = driver.find_element_by_css_selector("form [type=submit]").click()
    try:
        driver.find_element_by_css_selector(".notice .success")
    except:
        result1 = False
    result1 = True
    print(result1)

#logout
    logout = driver.find_element_by_css_selector("#navigation ul li:nth-child(4) a").click()
    try:
        driver.find_element_by_css_selector(".notice .success")
    except:
        result2 = False
    result2 = True
    print(result2)

#login
    login_email = driver.find_element_by_css_selector("form [name=email]").send_keys(email_random)
    login_password = driver.find_element_by_css_selector("form [name =password]").send_keys("Abc123")
    login = driver.find_element_by_css_selector("[name=login_form] .button-set [value=Login]").click()
    try:
        driver.find_element_by_css_selector(".notice .success")
    except:
        result3 = False
    result3 = True
    print(result3)

#loguot
    logout
    try:
        driver.find_element_by_css_selector(".notice .success")
    except:
        result4 = False
    result4 = True
    print(result4)