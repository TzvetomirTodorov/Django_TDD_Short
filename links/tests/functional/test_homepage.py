# import unittest
# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
# from selenium import webdriver
from links.tests.functional.base import FunctionalTest

# class HomepageTest(unittest.TestCase):
class HomepageSmallTest(FunctionalTest):
	fixtures = ['data-small.json']
	
	def test_homepage_layout(self):
		#Charlie opens his web browser and goes to the Bounce HomepageTest
		# self.browser.get('http://localhost:8000')
		self.browser.get(self.live_server_url)

		#He sees "Bounce" in the page header and the browser title
		self.assertEqual(self.browser.title, "Bounce")
		header_text = self.browser.find_element_by_css_selector('header h1').text
		self.assertEqual(header_text, "Bounce")

		#He sees fifteen interesting links to check out
		links = self.browser.find_elements_by_css_selector('li.link a')
		self.assertEqual(len(links) , 6)

		for link in links:
			self.assertTrue(link.get_attribute("href"))
			self.assertTrue(link.text)


class HomepageLargeTest(FunctionalTest):
	fixtures = ['data-large.json']
		
	def test_large_homepage_layout(self):
		
		#D opens his web browser and goes to the Bounce homepage
		self.browser.get(self.live_server_url)

		#He sees fifteen interesting links to check out
		links = self.browser.find_elements_by_css_selector('li.link a')
		self.assertEqual(len(links), 15)

		for link in links:
			self.assertTrue(link.get_attribute("href"))
			self.assertTrue(link.text)


class HomepageEmptyTest(FunctionalTest):

	def test_empty_homepage_layout(self):

		#Bobby opens his web browser and goes to the Bounce homepage
		self.browser.get(self.live_server_url)

		#No links have been posted so he only sees a "no links" message
		links = self.browser.find_elements_by_css_selector('li.link a')
		self.assertEqual(len(links), 0)

		message = self.browser.find_element_by_id('no-links').text
		self.assertEqual(message, "Sorry, no links have been posted.")

# if __name__	== '__main__':
# 	unittest.main(warnings='ignore')
