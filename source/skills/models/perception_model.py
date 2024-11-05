from django.contrib.postgres.fields import ArrayField
from django.db import models

from char.models import CharacterModel
from skills.models import ProficiencyModel


class PerceptionModel(models.Model):
    character = models.ForeignKey(CharacterModel, on_delete=models.CASCADE)
    ability_bonus = models.IntegerField()
    proficiency_bonus = models.ForeignKey(ProficiencyModel, on_delete=models.DO_NOTHING)
    item_bonus = models.IntegerField()
    senses = ArrayField(models.CharField(max_length=200), size=15) # most likely goes to M2M later
