import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.urlresolvers import reverse
from selenium import webdriver
from bounce.settings import BASE_DIR\


class FunctionalTest(StaticLiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Chrome()

	def tearDown(self):
		self.browser.quit()

	def login(self, username, password):
		self.browser.find_element_by_id('id_username').send_keys(username)
		self.browser.find_element_by_id('id_password').send_keys(password)
		login_button = self.browser.find_element_by_id('submit')
		self.click_wait(login_button)

	def click_wait(self,  element, seconds=.5):
		element.click()
		time.sleep(seconds)

	def check_stylesheet(self, view_name):
		self.browser.get("{0}{1}".format(self.live_server_url, reverse(view_name)))
		css_link = self.browser.find_element_by_css_selector('link[rel="stylesheet"]')
		self.browser.get(css_link.get_attribute('href'))
		css_used = self.browser.find_element_by_css_selector('body').text

		with open (BASE_DIR + '/links/static/css/main.css', "r") as css_file:
			actual_css = css_file.read().strip()

		self.assertEqual(css_used, actual_css)