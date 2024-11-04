from django.contrib.postgres.fields import ArrayField
from django.db import models


class HealthModel(models.Model):
    max = models.IntegerField()
    current = models.IntegerField()
    temp = models.IntegerField()
    dying = models.BooleanField(default=False)
    wounded = models.BooleanField(default=False)
    resist = ArrayField(models.CharField(max_length=100), blank=True, default=list)
    immunities = ArrayField(models.CharField(max_length=100), blank=True, default=list)
    conditions = ArrayField(models.CharField(max_length=100), blank=True, default=list)
