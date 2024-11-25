from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from accounts.models import CustomUser
from char.models import AbilitiesModel
from char.models.background_model import BackgroundModel
from char.models.size_model import SizeModel
from char.models.health_model import HealthModel
from char.models.race_model import RaceModel


class Alignment(models.TextChoices):
    LAWFUL_GOOD = "LG", "Lawful Good"
    NEUTRAL_GOOD = "NG", "Neutral Good"
    CHAOTIC_GOOD = "CG", "Chaotic Good"
    LAWFUL_NEUTRAL = "LN", "Lawful Neutral"
    TRUE_NEUTRAL = "TN", "True Neutral"
    CHAOTIC_NEUTRAL = "CN", "Chaotic Neutral"
    LAWFUL_EVIL = "LE", "Lawful Evil"
    NEUTRAL_EVIL = "NE", "Neutral Evil"
    CHAOTIC_EVIL = "CE", "Chaotic Evil"


class CharacterModel(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='characters', blank=False, null=False)
    name = models.CharField(max_length=150, blank=False, null=False)
    experience = models.IntegerField(blank=False, validators=[MinValueValidator(0), MaxValueValidator(1000)])
    level = models.IntegerField(blank=False, validators=[MinValueValidator(1), MaxValueValidator(20)], default=1)
    hero_points = models.IntegerField(blank=False, validators=[MinValueValidator(0), MaxValueValidator(20)], default=0)
    race = models.ForeignKey(RaceModel, on_delete=models.DO_NOTHING, related_name='character', blank=False, null=False)
    abilities = models.ForeignKey(AbilitiesModel, on_delete=models.DO_NOTHING, related_name='character')
    health = models.ForeignKey(HealthModel, on_delete=models.DO_NOTHING, related_name='character')
    heritage = models.ForeignKey("char.HeritageModel", on_delete=models.DO_NOTHING, related_name='chars', blank=True,
                                 null=True)
    # char_class = models.ForeignKey - after class model
    size = models.ForeignKey(SizeModel, on_delete=models.DO_NOTHING, related_name='character')
    alignment = models.CharField(max_length=2, blank=True, null=True, choices=Alignment.choices,
                                 default=Alignment.TRUE_NEUTRAL)
    saving_throw_notes = models.CharField(blank=True, null=True)
    background = models.ForeignKey(BackgroundModel, on_delete=models.DO_NOTHING, blank=True, null=True)
    deity = models.ForeignKey('deity.DeityModel', on_delete=models.DO_NOTHING, blank=True, null=True)
