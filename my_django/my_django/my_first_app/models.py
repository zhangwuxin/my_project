from __future__ import unicode_literals

from django.db import models

# Create your models here.
class MY_TABLE(models.Model):
    name = models.CharField(max_length=20)
    name = models.IntegerField(max_length=20)
    class Meta:
        managed = False
        db_table = 'my_table'