from urllib.parse import urlparse
from django.db import models
from django.contrib.auth.models import User

class Link(models.Model):
	title = models.CharField(max_length=120)
	url = models.URLField(max_length=300)
	score = models.SmallIntegerField(default=0)
	submitted_by = models.ForeignKey(User)
	boosters = models.ManyToManyField(User, related_name='boosted_links')
	submitted = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if self.score < 1:
			self.score = 1
		super(Link, self).save(*args, **kwargs)
		self.boosters.add(self.submitted_by)

	@property
	def domain(self):
		return urlparse(self.url).netloc