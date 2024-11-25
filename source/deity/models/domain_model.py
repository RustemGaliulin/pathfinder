from django.db import models


class DomainModel(models.Model):
    title = models.CharField()
    description = models.TextField()
    # spell = models.ForeignKey(Spell) after spells model
    # adnvanced_spell = models.ForeignKey(Spell) after spells model
    # apocryphic_spell = models.ForeignKey(Spell) after spells model