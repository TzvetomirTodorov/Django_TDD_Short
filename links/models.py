from urllib.parse import urlparse
from django.db import models
from django.contrib.auth.models import User

class Link(models.Model):
	title = models.CharField(max_length=120)
	url = models.URLField(max_length=300)
	submitted_by = models.ForeignKey(User)
	submitted = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

	@property
	def domain(self):
		return urlparse(self.url).netloc