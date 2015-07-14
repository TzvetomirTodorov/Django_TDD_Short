import unittest
# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
# from selenium import webdriver
# from bounce.settings import BASE_DIR
from links.tests.functional.base import FunctionalTest

# class HomepageTest(unittest.TestCase):

# class MyCSSTest(unittest.TestCase):

# 	def setUp(self):
# 		self.browser = webdriver.Chrome()

# 	def tearDown(self):
# 		self.browser.quit()

# 	maxDiff = None
# 	def test_homepage_stylesheet(self):
# 		self.browser.get('http://127.0.0.1:8000/')
# 		css_link = self.browser.find_element_by_css_selector('link[rel="stylesheet"]')
# 		self.browser.get(css_link.get_attribute('href'))
# 		css_used = self.browser.find_element_by_tag_name('body').text

# 		with open (BASE_DIR + '/links/static/css/main.css', "r") as css_file:
# 			actual_css = css_file.read().strip()

# 		self.assertEqual(css_used, actual_css)


class HomepageSmallTest(FunctionalTest):
	fixtures = ['data-small.json', 'users.json']
	
	def test_small_homepage_layout(self):
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

		#He notices that the first link was submitted by ttodorov
		username = self.browser.find_element_by_css_selector('.link span.submitted‐by')
		self.assertEqual(username.text, "ttodorov")

		#He notices that the first link was submitted some time ago
		time_ago = self.browser.find_element_by_css_selector('.link span.submitted-at').text
		self.assertTrue(time_ago.replace('ago', ''))
		
		#He notices that the first link is from http://ward.com/wp-content/about.php
		domain = self.browser.find_element_by_css_selector('.link small.link-domain').text
		self.assertEqual(domain, "vimeo.com") 

	def test_homepage_stylesheet(self):
		self.check_stylesheet('home')
		


	maxDiff = None
	@unittest.skip('Silly test.')	
	def test_homepage_stylesheet(self):
		self.browser.get(self.live_server_url)
		css_link = self.browser.find_element_by_css_selector('link[rel="stylesheet"]')
		self.browser.get(css_link.get_attribute('href'))
		css_used = self.browser.find_element_by_tag_name('body').text

		with open (BASE_DIR + '/links/static/css/main.css', "r") as css_file:
			actual_css = css_file.read().strip()

		self.assertEqual(css_used, actual_css)


class HomepageLargeTest(FunctionalTest):
	fixtures = ['data-large.json', 'users.json']
		
	def test_large_homepage_layout(self):
		
		#D opens his web browser and goes to the Bounce homepage
		self.browser.get(self.live_server_url)

		#He sees fifteen interesting links to check out
		links = self.browser.find_elements_by_css_selector('li.link a')
		self.assertEqual(len(links), 15)

		for link in links:
			self.assertTrue(link.get_attribute("href"))
			self.assertTrue(link.text)

		#He notices that the first link was submitted by ttodorov
		username = self.browser.find_element_by_css_selector('.link span.submitted‐by')
		self.assertEqual(username.text, "ttodorov")

		#He notices that the first link was submitted some time ago
		time_ago = self.browser.find_element_by_css_selector('.link span.submitted-at').text
		self.assertTrue(time_ago.replace('ago', ''))
		
		#He notices that the first link is from http://ward.com/wp-content/about.php
		domain = self.browser.find_element_by_css_selector('.link small.link-domain').text
		self.assertEqual(domain, "www.youtube.com")

	def test_link_boosting(self):
		# Al opens up the Bounce homepage in his browser.

		# He's not logged in so the boost button is not visible for any link.
		# He does however see the score for each link.

		# He signs in and now sees the boost button for each link.

		# The boost buttons are blue for the links he personally submitted,
		# green for the links he has boosted, and gray for the rest.

		# He sees a link that he likes and clicks the boost button.
		# It turns green and the score goes up by one.

		# He accidentally clicks the boost button for another link that he
		# doesn't like so he clisk the boost button again. It returns to
		# gray and the score goes down by one.

		# He decides to add a link of his own.

		# He sees his linnk at the top of the homepage already boosted with a score of one.
		self.fail('Finish link boosting test.')



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
