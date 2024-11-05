from django.db import models

from char.models import CharacterModel


class CoinsModel(models.Model):
    character = models.OneToOneField(CharacterModel, on_delete=models.CASCADE, related_name='coins')
    gold_pieces = models.PositiveIntegerField(default=0)
    silver_pieces = models.PositiveIntegerField(default=0)
    copper_pieces = models.PositiveIntegerField(default=0)
    platinum_pieces = models.PositiveIntegerField(default=0)
