from django.db import models
from django.contrib.auth.models import User


class Collection(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)