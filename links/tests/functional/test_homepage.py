import unittest
from selenium import webdriver

class HomepageTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Chrome()

	def tearDown(self):
		self.browser.quit()
		

	def test_homepage_layout(self):
		#Charlie opens his web browser and goes to the Bounce HomepageTest
		self.browser.get('http://localhost:8000')

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

if __name__	== '__main__':
	unittest.main(warnings='ignore')
