from django.db import models


class BackgroundModel(models.Model):
    title = models.CharField()
    description = models.TextField()
