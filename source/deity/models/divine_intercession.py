from django.db import models


class DivineIntercessionModel(models.Model):
    minor_boon = models.TextField()
    moderate_boon = models.TextField()
    major_boon = models.TextField()
    minor_curse = models.TextField()
    moderate_curse = models.TextField()
    major_curse = models.TextField()
