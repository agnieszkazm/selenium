from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("https://www.google.pl")
sleep(10)
driver.quit()	