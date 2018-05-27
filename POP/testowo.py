# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BaseTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("http://malinowykoszyk.pl")

    def test(self):
        search_field = self.driver.find_element_by_id("search_query_top")
        search_field.click()
        search_field.send_keys("ksiazki")
        search_field.submit()

        wait = WebDriverWait(self.driver, 10)
        title_is_page = EC.title_is("Search")
        wait.until(title_is_page)
        self.assertTrue(title_is_page(self.driver))

        products_count = 0
        products = {}
        for product in self.driver.find_elements_by_css_selector('.product_list li'):
            title = product.find_element_by_css_selector(".product-name").get_attribute("innerHTML")
            link = product.find_element_by_css_selector('.replace-2x')

            products[title[1:-1]] = link
        wait = WebDriverWait(self.driver, 10)    
        print(products.values()[0])
        products.values()[0].click()
        productsTitle=products.keys()[0]
        print(productsTitle)

        titleOnProductPage = self.driver.find_element_by_css_selector('.product-title h1').get_attribute("innerHTML")
        print(titleOnProductPage)
 
        self.assertTrue(productsTitle==titleOnProductPage)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print ('quit driver')


if __name__ ==	'__main__':
	unittest.main()