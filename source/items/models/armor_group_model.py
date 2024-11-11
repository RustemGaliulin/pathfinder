from django.db import models


class ArmorGroupModel(models.Model):
    title = models.CharField()
    description = models.TextField()
