from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^alerts/$', views.alert_list, name='alert-list'),
    url(r'^centres/$', views.centre_list, name='centre-list'),
    url(r'^articles/$', views.article_list, name='article-list'),
    url(r'^statistiques/$', views.statistique_list, name='statistique-list'),
    url(r'^alerts/(?P<pk>[0-9]+)/$', views.alert_detail),
    url(r'^centres/(?P<pk>[0-9]+)/$', views.centres_detail),
    url(r'^articles/(?P<pk>[0-9]+)/$', views.article_detail),
    url(r'^statistiques/(?P<pk>[0-9]+)/$', views.statistique_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)