from django.conf.urls import patterns, url

urlpatterns = patterns	('',
	url(r'^$', 'links.views.home', name='home'),
	url(r'^submit/$', 'links.views.new_link', name='new_link'),	
)