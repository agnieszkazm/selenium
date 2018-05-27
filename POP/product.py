# -*- coding: utf-8 -*-

from base import BasePage
from base import InvalidPageException

class ProductPage(BasePage):
	_page_title_locator = ".product-title h1"

	def __init__(self, driver):
		super(ProductPage, self).__init__(driver)

	@property
	def name(self):
		return self.driver.find_element_by_css_selector(self._page_title_locator).text.strip()


	def _validate_page (self, driver):
		try:
			driver.find_element_by_css_selector(self._page_title_locator) 
		except:
			raise InvalidPageException("Product page not loaded")