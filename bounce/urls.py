from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'bounce.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', login, name="login"),
    url(r'^logout/$', logout, {'next_page':'/'}, name="logout"),
    url(r'^', include('links.urls')),
]
