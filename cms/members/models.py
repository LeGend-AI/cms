from django.conf import settings
from django.db import models

class MemberProfile(models.Model):
  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  organization = models.CharField(max_length=200)
  title = models.CharField(max_length=50)
