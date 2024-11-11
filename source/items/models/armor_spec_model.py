from django.db import models


class ArmorSpecModel(models.Model):
    title = models.CharField()
    description = models.TextField()
