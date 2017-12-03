from selenium.webdriver.support.wait import WebDriverWait

class mainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, base_url):
        self.driver.get(base_url)
        return self

    def choose_product(self):
        self.driver.find_elements_by_css_selector("#box-most-popular li")[1].click()
