from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from django.views.generic import TemplateView
from oauth2client.contrib.django_util import decorators # Google oAuth
# oAuth
from .models import CredentialsModel # To get credentials
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.contrib.django_util.storage import DjangoORMStorage
from django.conf import settings


# Flow to authenticate the user
def get_flow(request):
    flow = OAuth2WebServerFlow(
        client_id = settings.GOOGLE_OAUTH2_CLIENT_ID,
        client_secret = settings.GOOGLE_OAUTH2_CLIENT_SECRET,
        scope = settings.GOOGLE_OAUTH2_SCOPES,
        redirect_uri = settings.GOOGLE_REDIRECT,
        access_type='offline',
        prompt="consent",
    )

    return flow

##### Google OAuth #######

@decorators.oauth_required
def get_profile_required(request):
    resp, content = request.oauth.http.request(
        'https://www.googleapis.com/plus/v1/people/me')
    return HttpResponse(content)

@decorators.oauth_enabled
def get_profile_optional(request):
    if request.oauth.has_credentials():
        # this could be passed into a view
        # request.oauth.http is also initialized
        return HttpResponse('User email: {}'.format(
            request.oauth.credentials.id_token['email']))
    else:
        return HttpResponse(
            'Here is an OAuth Authorize link:<a href="{}">Authorize</a>'
            .format(request.oauth.get_authorize_redirect()))
