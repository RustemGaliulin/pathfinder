from django.db import models

from items.models import ItemModel

class ShieldModel(ItemModel):
    armor_bonus = models.IntegerField()
    extra_armor_bonus = models.IntegerField()
    speed_penalty = models.IntegerField()
    hardness = models.IntegerField()
    hp = models.IntegerField()
    break_limit = models.IntegerField()
