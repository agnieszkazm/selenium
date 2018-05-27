# -*- coding: utf-8 -*-

from base import BasePage
from base import InvalidPageException

class HomePage(BasePage):
	# check if page is loaded
	_home_page_loading_check_locator = 'columns-container'

	def __init__(self, driver):
		super(HomePage, self).__init__(driver)

	def __validate__page(self, driver):
		try:
			driver.find_element_by_class_name(self._home_page_loading_check_locator)
		except:
			raise InvalidPageException("Home Page not loaded")