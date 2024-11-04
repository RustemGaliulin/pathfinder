from django.db import models

from char.models.size_model import SizeModel


class RaceModel(models.Model):
    title = models.CharField(blank=False, null=False, max_length=50)
    hit_points = models.IntegerField(blank=False, null=False)
    size = models.ForeignKey(SizeModel, on_delete=models.DO_NOTHING)
    speed = models.IntegerField(blank=False, null=False)
    special = models.CharField(blank=False, null=False, max_length=150)  # like elve's low-light vision
