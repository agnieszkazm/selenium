# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver

class BaseTestCase(unittest.TestCase):
	
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(30)
		self.driver.maximize_window()
		self.driver.get("http://malinowykoszyk.pl")

	def tearDown(self):
		self.driver.quit()

