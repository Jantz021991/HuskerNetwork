from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^venues/$', views.venue_list, name='venue_list'),
    url(r'^venues/(?P<pk>\d+)/delete/$', views.venue_delete, name='venue_delete'),
    url(r'^venues/(?P<pk>\d+)/edit/$', views.venue_edit, name='venue_edit'),
    url(r'^venues/create/$', views.venue_new, name='venue_new'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
