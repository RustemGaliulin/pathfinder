from django.db import models


class DevoteeBenefitModel(models.Model):
    ability = models.ManyToManyField('char.AbilitiesModel', on_delete=models.DO_NOTHING,
                                     related_name='devotee_benefits')
    skill = models.ManyToManyField('skills.SkillModel', on_delete=models.DO_NOTHING, related_name='devotee_benefits')
    weapon = models.CharField(blank=True)
    domain = models.ManyToManyField('deity.DomainModel', on_delete=models.DO_NOTHING, related_name='devotee_benefits')
    alternate_domain = models.ManyToManyField('deity.DomainModel', on_delete=models.DO_NOTHING,
                                              related_name='devotee_benefits')
    devotee_spells = models.ManyToManyField('deity.devotee_spells', on_delete=models.DO_NOTHING, related_name='devotee_benefits')
