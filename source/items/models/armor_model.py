from django.db import models

from items.models import ItemModel


class ArmorModel(ItemModel):
    category = models.CharField()
    armor_class_bonus = models.IntegerField()
    dex_cap = models.IntegerField()
    check_penalty = models.IntegerField()
    speed_penalty = models.IntegerField()
    str = models.IntegerField()
    group = models.ManyToManyField('items.ArmorGroupModel', related_name='armors')
    spec_effect = models.ManyToManyField('items.ArmorSpecModel', related_name='armors')