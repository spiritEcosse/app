import uuid

from django.db import models


class Application(models.Model):
    key = models.CharField(max_length=40)
    name = models.CharField(max_length=200)

    def save(self, **kwargs):
        self.key = uuid.uuid4()
        super(Application, self).save(kwargs)
