from django.conf.urls import url, include
from django.contrib import admin
from ga import views
from ga.views import Kpi


urlpatterns = [
    url(r'^ga/$', views.ga),
    url(r'^report', views.report),
    url(r'^kpi$', Kpi.as_view(), name = 'kpi'),
]
