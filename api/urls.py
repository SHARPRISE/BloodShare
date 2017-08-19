from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^users/$', views.user_list, name='user-list'),
    url(r'^alerts/$', views.alert_list, name='alert-list'),
    url(r'^centres/$', views.centre_list, name='centre-list'),
    url(r'^articles/$', views.article_list, name='article-list'),
    url(r'^statistiques/$', views.statistique_list, name='statistique-list'),
    url(r'^demande/$', views.demande_list, name='demande-list'),
    url(r'^planifier/$', views.planifier_list, name='planifier-list'),
    url(r'^user/(?P<pk>[0-9]+)/$', views.user_detail),
    url(r'^alerts/(?P<pk>[0-9]+)/$', views.alert_detail),
    url(r'^centres/(?P<pk>[0-9]+)/$', views.centres_detail),
    url(r'^articles/(?P<pk>[0-9]+)/$', views.article_detail),
    url(r'^statistiques/(?P<pk>[0-9]+)/$', views.statistique_detail),
    url(r'^demande/(?P<pk>[0-9]+)/$', views.demande_detail),
    url(r'^planifier/(?P<pk>[0-9]+)/$', views.planifier_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)