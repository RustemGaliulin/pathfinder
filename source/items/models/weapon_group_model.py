from django.db import models


class WeaponGroupModel(models.Model):
    title = models.CharField()
    critical_hit_description = models.TextField()
