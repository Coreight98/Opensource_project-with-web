from django.conf import settings
from django.db import models
from django.utils import timezone
# class skeleton(models.Model) :
#     content = models.TextField()

from django.db import models

class User(models.Model):
    file = models.FileField()
    options = models.CharField(max_length=2000)