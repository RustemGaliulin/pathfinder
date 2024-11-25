from django.db import models


class DevoteeBenefitModel(models.Model):
    ability = models.ManyToManyField('char.AbilitiesModel', related_name='devotee_benefits')
    skill = models.ManyToManyField('skills.SkillModel', related_name='devotee_benefits')
    weapon = models.CharField(blank=True)
    domain = models.ManyToManyField('deity.DomainModel', related_name='devotee_benefits')
    alternate_domain = models.ManyToManyField('deity.DomainModel', related_name='devotee_benefits_alternate')
    devotee_spells = models.ManyToManyField('deity.DevoteeSpellsModel', related_name='devotee_benefits')
