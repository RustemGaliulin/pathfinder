from django.db import models

from skills.models.proficiency_model import ProficiencyModel


class SkillModel(models.Model):
    title = models.CharField(max_length=150)
    ability_bonus = models.IntegerField()
    proficiency_level = models.ForeignKey(ProficiencyModel, on_delete=models.DO_NOTHING)
    item_bonus = models.IntegerField()
    armor_penalty = models.IntegerField()
