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

		#He sees fifteen interesting links to check out
		links = self.browser.find_elements_by_css_selector('li.link a')
		self.assertEqual(len(links) , 15)


if __name__	== '__main__':
	unittest.main(warnings='ignore')
