from django.db import models

from items.models import ItemModel


class WeaponModel(ItemModel):
    damage = models.CharField()
    damage_type = models.CharField()
    hands = models.FloatField()
    tag = models.ManyToManyField('items.WeaponGroupModel', related_name='weapons', )
