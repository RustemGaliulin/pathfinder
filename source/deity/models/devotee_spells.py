from django.db import models

class DevoteeSpellsModel(models.Model):
    # spell = models.ForeignKey(Spell) after spell model
    level_criteria = models.IntegerField(blank=True, null=True)