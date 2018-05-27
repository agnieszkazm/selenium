# -*- coding: utf-8 -*-

from base import BasePage
from base import InvalidPageException
from product import ProductPage
import random

class SearchRegion(BasePage):
	_search_box_locator = 'search_query_top'
	print(_search_box_locator)

	def __init__(self, driver):
		super(SearchRegion, self).__init__(driver)

	def searchFor(self,term):
		self.search_field = self.driver.find_element_by_id(self._search_box_locator)
		self.search_field.clear()
		self.search_field.send_keys(term)
		self.search_field.submit()
		return SearchResults(self.driver)

class SearchResults(BasePage):
	_product_list_locator = ".product_list li"
	_product_title_locator = ".product-name"
	_product_image_link = ".replace-2x"
	_products = {}

	def __init__(self, driver):
		super(SearchResults, self).__init__(driver)

		for product in self.driver.find_elements_by_css_selector(self._product_list_locator):
			title = unicode(product.find_element_by_css_selector(self._product_title_locator).get_attribute("innerHTML"))
			link = product.find_element_by_css_selector(self._product_image_link)
            
			self._products[title[1:-1]] = link
 #        products.values()[0].click()
 #        productsTitle=products.keys()[0]
 #        titleOnProductPage = self.driver.find_element_by_css_selector(self._page_title_locator).get_attribute("innerHTML")
 	

 		
	def _validiate_page(self, driver):
		if "Search" not in driver.title:
			raise InvalidPageException('Search results page not loaded')

	@property
	def product_count(self):
		return len(self._products)

	def get_products(self):
		return self._products

	def randomItem(self):
		result = random.choice(self._products.keys())
		print("random choice: "+result)
 		return result

	def open_product_page(self, product_name):
		self._products[product_name].click()
		return ProductPage(self.driver)