from django.conf.urls import url, include
from django.contrib import admin
from ga.views import Index

urlpatterns = [
    url(r'^$', Index.as_view(), name = 'home'),
    url(r'^admin/', admin.site.urls),
    url(r'', include('oauth.urls')),
    url(r'', include('ga.urls')),
]
