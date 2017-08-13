from django.conf.urls import url, include

from blood_alert import views

urlpatters = [
    url(r'^add_alert$', views.add_alert, name='add_alert'),
    url(r'^alerts$', views.alerts, name='alerts'),
]
