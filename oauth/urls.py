from django.conf.urls import url, include
from django.contrib import admin
from oauth import views

from django.contrib.auth import views as auth_views # For Login
from django.views.generic.edit import CreateView # For Registration
from django.contrib.auth.forms import UserCreationForm # For Registration

from oauth.views import login, logout, oauth2redirect, get_flow

##### Google oAuth ######
from django.conf import urls
import django.contrib.auth.views
import oauth2client.contrib.django_util.site as django_util_site

urlpatterns = [
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^oauth2redirect', oauth2redirect, name='oauth2redirect'),
    url(r'^get_flow/$', get_flow, name = 'get_flow'),
]



'''
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


urlpatterns = [
    # GA App
    urls.url(r'^login', django.contrib.auth.views.login, name="login"),
    url(r'^logout/$', auth_views.logout, {'next_page': '/?code=exit'}, name='logout'),
    url('^register/', CreateView.as_view(template_name='registration/register.html', form_class=UserCreationForm, success_url='/')),
    url('^accounts/', include('django.contrib.auth.urls')),
    # oAuth App
    url(r'^accounts/login/', login_view, name='login'), # why do i need accounts here?
#    url(r'^register/', register_view, name='register'),
#    url(r'^logout/', logout_view, name='logout'),
    # Google oAuth
    url(r'^get_creds/', views.get_creds, name='get_creds'),
    url(r'^oauth2/redirect/', views.oauth2redirect, name='oauth2redirect'),
    url(r'^admin/', include(admin.site.urls)),
]
'''
