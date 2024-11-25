from django.db import models


class SavingsModel(models.Model):
    total_value = models.IntegerField()
    title = models.CharField()
    ability = models.ManyToManyField("char.AbilitiesModel", on_delete=models.DO_NOTHING, related_name="savings")
    item_bonus = models.IntegerField()
    proficiency_level = models.ForeignKey("skills.ProficiencyModel", on_delete=models.DO_NOTHING,
                                          related_name="savings")
