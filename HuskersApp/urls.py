from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^group/', views.group, name='group'),
    url(r'^venue/', views.venue, name='venue'),
    url(r'^feed/', views.feed, name='feed'),
    url(r'^venue_detail/', views.venue_detail, name='venue_detail'),
]

