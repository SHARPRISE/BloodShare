from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^alerts/$', views.AlertList.as_view(), name='alert-list'),
    url(r'^centres/$', views.CentreList.as_view(), name='centre-list'),
    url(r'^articles/$', views.ArticleList.as_view(), name='article-list'),
    url(r'^statistiques/$', views.StatistiqueList.as_view(), name='statistique-list'),
    url(r'^demande/$', views.DemandeList.as_view(), name='demande-list'),
    url(r'^planifier/$', views.PlanifierList.as_view(), name='planifier-list'),
    url(r'^user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^alerts/(?P<pk>[0-9]+)/$', views.AlertDetail.as_view()),
    url(r'^centres/(?P<pk>[0-9]+)/$', views.CentresDetail.as_view()),
    url(r'^articles/(?P<pk>[0-9]+)/$', views.ArticleDetail.as_view()),
    url(r'^statistiques/(?P<pk>[0-9]+)/$', views.StatistiqueDetail.as_view()),
    url(r'^demande/(?P<pk>[0-9]+)/$', views.DemandeDetail.as_view()),
    url(r'^planifier/(?P<pk>[0-9]+)/$', views.PlanifierDetail.as_view()),
    url(r'^api-auth/', include('rest_framework.urls'))
]

urlpatterns = format_suffix_patterns(urlpatterns)
