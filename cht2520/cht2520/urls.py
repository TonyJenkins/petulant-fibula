from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cht2520.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^guestbook/', include ('guestbook.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
