from selenium import webdriver
from pages.product_page import productPage
from pages.basket_page import basketPage
from pages.main_page import mainPage

class Application:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.mainp = mainPage(self.driver)
        self.productp = productPage(self.driver)
        self.basketp = basketPage(self.driver)

    def quit(self):
        self.driver.quit()

    def buyProduct(self):
        self.mainp.open("http://localhost/litecart/en")
        self.mainp.choose_product()
        self.productp.orderProduct()
        self.productp.checkCartCounter()
        self.basketp.open_basket()
        self.basketp.basket_check()