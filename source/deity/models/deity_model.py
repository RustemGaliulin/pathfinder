from django.db import models

from char.models.char_model import Alignment


class DeityModel(models.Model):
    name = models.CharField()
    title = models.CharField()
    description = models.TextField()
    category = models.CharField()
    edicts = models.TextField()
    anathema = models.TextField()
    areas_of_concern = models.TextField()
    pantheons = models.TextField()
    followers_alignment = models.CharField(max_length=2, blank=True, null=True, choices=Alignment.choices)
    allies = models.ManyToManyField('self')
    enemies = models.ManyToManyField('self')
    # relationship - not sure if needed
    devotees = models.TextField(blank=True)
    animal = models.CharField(blank=True)
    devotee_benefits = models.ForeignKey("deity.DevoteeBenefitModel", on_delete=models.DO_NOTHING, blank=True,
                                         null=True)
    divine_intercession = models.ForeignKey("deity.DivineIntercessionModel", on_delete=models.DO_NOTHING, blank=True,
                                            null=True)
