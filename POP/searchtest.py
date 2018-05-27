# -*- coding: utf-8 -*-

import unittest
from homepage import HomePage
from basetestcase import BaseTestCase
from search import SearchResults


class SearchProductTest(BaseTestCase):
	def testSearchForProduct(self):
		homepage = HomePage(self.driver)
		search_results = homepage.search.searchFor(u'książki')
		losowyProductZeSlownika = search_results.randomItem()
		print("print product name: "+losowyProductZeSlownika)
		product = search_results.open_product_page(losowyProductZeSlownika)
		# searchresults = SearchResults(self.driver)
		# search_results = searchresults
		self.assertEqual(losowyProductZeSlownika.lower(), product.name.lower())

if __name__=='__main__':
	unittest.main(verbosity=2)
