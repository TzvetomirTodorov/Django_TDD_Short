from django.conf.urls import patterns, url

urlpatterns = patterns	('',
	url(r'^$', 'links.views.home', name='home')	
)