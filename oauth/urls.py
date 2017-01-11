from django.conf.urls import url, include
from django.contrib import admin
from oauth import views

from django.contrib.auth import views as auth_views # For Login
from django.views.generic.edit import CreateView # For Registration
from django.contrib.auth.forms import UserCreationForm # For Registration

##### Google oAuth ######
from django.conf import urls
import django.contrib.auth.views
import oauth2client.contrib.django_util.site as django_util_site

urlpatterns = [
    url(r'^logout/$', auth_views.logout, {'next_page': '/?code=exit'}, name='logout'),
    url('^register/', CreateView.as_view(template_name='registration/register.html', form_class=UserCreationForm, success_url='/')),
    url('^accounts/', include('django.contrib.auth.urls')),
    ### Google oAuth ###
    urls.url(r'^profile_required$', views.get_profile_required),
    urls.url(r'^profile_enabled$', views.get_profile_optional),
    urls.url(r'^login', django.contrib.auth.views.login, name="login"),
    urls.url(r'^oauth2/', urls.include(django_util_site.urls)),
    url(r'^flow/$', views.get_flow),
]
