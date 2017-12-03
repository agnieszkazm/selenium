from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class basketPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_basket(self):
        driver.find_element_by_css_selector("#cart .link").click()
        assert wait.until(EC.title_is("Checkout | My Store"))

    def basket_check(self):
        for i in range(3):
            driver.find_elements_by_css_selector("#box-checkout-cart [name='remove_cart_item']")[0].click()
            wait.until(EC.staleness_of(driver.find_element_by_css_selector('.dataTable')))