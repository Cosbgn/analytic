from django.db import models

# Create your models here.

###### Google oAuth ##########
from django.contrib.auth.models import User
from oauth2client.contrib.django_util.models import CredentialsField

class CredentialsModel(models.Model):
    user_id = models.OneToOneField(User)
    credential = CredentialsField()
