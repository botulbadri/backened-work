from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Family(models.Model):
    name = models.CharField(max_length = 25)
    description = models.CharField(max_length = 20)
    age = models.CharField(max_length = 15)
    def __str__ (self):
        return self.name
        