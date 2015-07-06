from django.test import TestCase
from django.core.urlresolvers import resolve, reverse
from links.views import home
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