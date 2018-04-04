from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^group/', views.group, name='group'),
    url(r'^venue/', views.venue, name='venue'),
    url(r'^feed/', views.feed, name='feed'),
    url(r'^venue_detail/', views.venue_detail, name='venue_detail'),
    url(r'^home/$', views.home, name='home'),
    url(r'^venues/$', views.venue_list, name='venue_list'),
    url(r'^venues/(?P<pk>\d+)/delete/$', views.venue_delete, name='venue_delete'),
    url(r'^venues/(?P<pk>\d+)/edit/$', views.venue_edit, name='venue_edit'),
    url(r'^venues/(?P<pk>\d+)/detail/$', views.venue_detail, name='venue_detail'),
    url(r'^venues/create/$', views.venue_new, name='venue_new'),
    url(r'^groups/$', views.group_list, name='group_list'),
    url(r'^groups/(?P<pk>\d+)/detail/$', views.group_detail, name='group_detail'),
    url(r'^groups/create/$', views.group_new, name='group_new'),
    url(r'^groups/(?P<pk>\d+)/edit/$', views.group_edit, name='group_edit'),]




#urlpatterns = format_suffix_patterns(urlpatterns)
