import unittest
from links.tests.functional.base import FunctionalTest


class NewLinkSubmissionTest(FunctionalTest):
	fixtures = ['data-small.json', 'users.json']

	def test_logged_in_user_can_submit_new_link(self):
		# Anne finds a cool article and wants to share it on Bounce
		# She Logs in and clicks the "New Link" button
		self.browser.get(self.live_server_url + '/login')
		self.login('test_user', 'test_password')
		new_link = self.browser.find_element_by_id('new-link')
		self.click_wait(new_link)

		# She fills out the new link form with a title and URL and clicks "Post"
		new_title = "Ray, the self-driving forklift that is parking cars at a German airport"
		new_url  = "http://www.washingtonpost.com/blogs/innovations/wp/2014/07/01/meet-ray-"\
							 "the-self-driving-forklift-that-is-parking-cars-at-a-german-airport/"

		self.browser.find_element_by_id('id_title').send_keys(new_title)
		self.browser.find_element_by_id('id_url').send_keys(new_url)
		post_button = self.browser.find_element_by_id('submit')
		self.click_wait(post_button)	

		# She is redirected to the homepage and sees her link at the top
		self.assertEqual(self.browser.current_url, self.live_server_url + '/')
		first_link_title = self.browser.find_element_by_css_selector('li.link a').text
		self.assertIn("Ray, the self-driving forklift", first_link_title)

		# self.fail("Finish new link when logged in test.")

	def test_logged_out_user_cannot_submit_new_link(self):
		# Andy finds a cool article and wants to sahre it on Bounce
		# He is not logged in so he doesn't see the "New Link" button
		self.browser.get(self.live_server_url)
		self.assertNotIn('New Link', self.browser.find_element_by_tag_name('body').text)

		# Andy is smart and knows the URL for the new link form so he tries that
		self.browser.get(self.live_server_url + '/submit/')

		# He is redirected to the login page instead
		self.assertEqual(self.browser.current_url, self.live_server_url + '/login/?next=/submit/')

		# He logs in and is redirected to the new link form
		self.login('test_user', ('test_password'))
		self.assertEqual(self.browser.current_url, self.live_server_url + '/submit/')

		# self.fail("Finish new link when logged out test.")
	@unittest.skip('Silly test.')
	def test_new_link_page_stylesheet(self):
		self.browser.get(self.live_server_url + '/login')
		self.login('test_user', 'test_password')
		self.check_stylesheet('new_link')