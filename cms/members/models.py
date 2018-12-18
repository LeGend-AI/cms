from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  organization = models.CharField(max_length=200)
  title = models.CharField(max_length=50)
