from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from django.views.generic import TemplateView
from oauth2client.contrib.django_util import decorators # Google oAuth
# Google Analytics
# import argparse
#
# from apiclient.discovery import build
# import httplib2
# from oauth2client import client
# from oauth2client import file
# from oauth2client import tools

# Create your views here.

class Index(TemplateView):
    template_name = 'ga/index.html'

def ga(request):
#   return HttpResponse('hello')
   @decorators.oauth_required
   def requires_default_scopes(request):
      email = request.oauth.credentials.id_token['email']
    # service = build(serviceName='calendar', version='v3', http=request.oauth.http, developerKey=API_KEY)
      analytics = build('analytics', 'v4', http=http, discoveryServiceUrl='https://analyticsreporting.googleapis.com/$discovery/rest')
      events = service.events().list(calendarId='primary').execute()['items']
      return HttpResponse("email: {0}".format(email))
      return HttpResponse("email: {0}".format(email))
    # return HttpResponse("email: {0} , Analytics: {1}".format(email,str(analytics)))
    # return HttpResponse("email: {0} , calendar: {1}".format(email, str(events)))


@decorators.oauth_required
def report(request):
    current_user = request.user
    username = request.user.username
    return HttpResponse ('Current user ID: '+str(current_user.id)+', Username: '+str(username))

class Kpi(TemplateView):
    template_name = 'ga/kpi.html'


##### Google OAuth #######

#
#
# def index(request):
#     return HttpResponse("Hello world!")
#

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
