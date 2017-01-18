
from django.db import models
from django.contrib import admin

from django.contrib.auth.models import User
# Which one?
from oauth2client.contrib.django_util.models import CredentialsField
# from oauth2client.contrib.django_orm import CredentialsField

class Credentials(models.Model):
    id = models.OneToOneField(User, primary_key=True)
    credential = CredentialsField()

    class Meta:
        db_table = 'credentials'
# To show credentials when called
    def __str__(self):
    	return 'creds'

# to be able to see credentials in admin
class CredentialsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Credentials, CredentialsAdmin)
