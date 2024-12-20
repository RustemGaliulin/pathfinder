from django.db import models


class HeritageModel(models.Model):
    title = models.CharField()
    description = models.TextField()
    universal = models.BooleanField()
    race = models.ForeignKey("char.RaceModel", on_delete=models.CASCADE, related_name="heritages", null=True,
                             blank=True)
