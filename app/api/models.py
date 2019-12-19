from django.db import models


class Application(models.Model):
    key = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
