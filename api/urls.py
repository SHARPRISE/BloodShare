from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    url(r'^api$', views.api_root),
    url(r'^alerts_api/$', views.alert_list, name='alert-list'),
    url(r'^alerts_api/(?P<pk>[0-9]+)/$', views.alert_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)