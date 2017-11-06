from selenium import webdriver
from time import sleep


driver=webdriver.Firefox()
driver.get("http://localhost/litecart/en/")

def test_loggin(driver):
    loggin=driver.find_element_by_name("email").send_keys("agnieszka.rydz@gmail.com")
    passwors=driver.find_element_by_name("password").send_keys("gis1partner")
    submit_button=driver.find_element_by_css_selector(".button-set button:first-child").click()

def after_test_loggin(driver):
    driver.quit()



test_loggin(driver)
sleep(10)
after_test_loggin(driver)