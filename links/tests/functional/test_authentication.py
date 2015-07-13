import unittest
import time
from links.tests.functional.base import FunctionalTest

class AuthenticationTest(FunctionalTest):
	fixtures = ['data-small.json', 'users.json']

	def test_user_can_login_and_logout(self):
		# Q is browsing links on Bounce
		self.browser.get(self.live_server_url)

		#He wants to login to have a customzed user experience.
		#He licks the 'Login' Link which takes him to the Login form
		login_link = self.browser.find_element_by_id('login')
		login_link.click()
		time.sleep(5)

		#He notices the browser title change
		self.assertEqual(self.browser.title, 'Bounce | Login')

		#He enters his username and password and clicks the 'Login' submission button
		self.browser.find_element_by_id('id_username').send_keys('test_user')
		self.browser.find_element_by_id('id_password').send_keys('test_password')
		login_button = self.browser.find_element_by_id('submit')
		login_button.click()
		time.sleep(5)

		#He is redirected back to the homepage but now sees his username
		#and Logout button in the header. The login button is no longer present
		header_text = self.browser.find_element_by_tag_name('header').text
		self.assertIn('test_user', header_text)
		self.assertIn('Logout', header_text)
		self.assertNotIn('Login', header_text)

		#Q is done browsing Links and wants to Logout so he clicks the 'Logout' button
		logout_link = self.browser.find_element_by_id('logout')
		logout_link.click()
		time.sleep(5)

		#The homepage reLoads and he can no longer see his username
		#or Logout in the header, The Login button is again present
		header_text = self.browser.find_element_by_tag_name('header').text
		self.assertNotIn('test_user', header_text)
		self.assertNotIn('Logout', header_text)
		self.assertIn('Login', header_text)

	@unittest.skip('Silly test.')	
	def test_login_stylesheet(self):
		self.check_stylesheet('login')
		
	def test_user_cant_login_and_returns_to_homepage(self):
		# Bo wants to Login to Bounce
		self.browser.get(self.live_server_url + '/login')

		# He enters an invalid username and password and clicks the 'Login' button
		self.browser.find_element_by_id('id_username').send_keys('invalid_user')
		self.browser.find_element_by_id('id_password').send_keys('invalid_password')
		login_button = self.browser.find_element_by_id('submit')
		login_button.click()
		time.sleep(5)

		# The login form responds with an error message
		error_message = self.browser.find_element_by_css_selector('p.error').text
		self.assertIn("Your username and password didn't match.", error_message)

		# Bo can't remember his login info and decides to just browse without Logging in
		home_link = self.browser.find_element_by_css_selector('header>h1>a')
		home_link.click()
		time.sleep(5)
		self.assertEqual(self.browser.current_url, self.live_server_url + '/')