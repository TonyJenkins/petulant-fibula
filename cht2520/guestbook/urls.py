from django.conf.urls import patterns, url
from guestbook import views

urlpatterns = patterns ('',
  url (
    regex = r'^$',
    view = views.add_comment,
    name = 'add_comment'
  ),
)
