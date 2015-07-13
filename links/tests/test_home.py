from django.test import TestCase
from django.core.urlresolvers import resolve, reverse
from django.contrib.auth.views import login, logout
from links.views import home
from links.views import home, new_link
from links.models import Link

class HomeTest(TestCase):

	def test_root_url_resolves_to_home_view(self):
		view_found = resolve('/')
		self.assertEqual(view_found.func, home)

	def test_home_template_used_by_home_view(self):
		response = self.client.get(reverse('home'))
		self.assertTemplateUsed(response, 'home.html')

	def test_most_recent_links_returned_by_home_view(self):
		response = self.client.get(reverse('home'))
		response_links = response.context['links']
		expected_links = Link.objects.all().order_by('-submitted')[:15]
		self.assertQuerysetEqual(response_links, expected_links)


class AuthTest(TestCase):

	def test_login_url_resolves_to_login_view(self):
		view_found = resolve('/login/')
		self.assertEqual(view_found.func, login)

	def test_login_template_used_by_login_view(self):
		response = self.client.get(reverse('login'))
		self.assertTemplateUsed(response, 'registration/login.html')

	def test_logout_url_resolves_to_logout_view(self):
		view_found = resolve('/logout/')
		self.assertEqual(view_found.func, logout)

class NewLinkTest(TestCase):
	fixtures = ['users.json']

	def test_new_link_view_requires_login(self):
		response = self.client.get(reverse('new_link'), follow=True)
		self.assertRedirects(response, '/login/?next=/submit/')

	def test_new_link_url_resolves_to_new_link_view(self):
		view_found = resolve('/submit/')
		self.assertEqual(view_found.func, new_link)

	def test_new_link_template_used_by_new_link_view(self):
		self.client.login(username='test_user', password='test_password')
		response = self.client.get(reverse('new_link'))
		self.assertTemplateUsed(response, 'base.html')
		self.assertTemplateUsed(response, 'new_link.html')

	def test_new_link_view_can_receive_a_post_request(self):
		self.assertEqual(Link.objects.count(), 0)

		self.client.login(username='test_user', password='test_password')
		response = self.client.post(reverse('new_link'), {
			'title': 'Wired',
			'url': 'http://www.wired.com/',
			})

		self.assertRedirects(response, '/')

		self.assertEqual(Link.objects.count(), 1)
		link = Link.objects.first()
		self.assertEqual(link.title, 'Wired')
		self.assertEqual(link.url, 'http://www.wired.com/')


