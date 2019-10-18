from __future__ import unicode_literals

from django.db import models

# Create your models here.
class MyTable(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(max_length=20)

    class Meta:
        managed = False
        db_table = "my_table"
