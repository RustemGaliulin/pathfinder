from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from accounts.models import CustomUser

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


class Character(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='characters', blank=False, null=False)
    name = models.CharField(max_length="150", blank=False, null=False)
    experience = models.IntegerField(blank=False, validators=[MinValueValidator(0), MaxValueValidator(1000)])
    level = models.IntegerField(blank=False, validators=[MinValueValidator(1), MaxValueValidator(20)], default=1)
    hero_points = models.IntegerField(blank=False, validators=[MinValueValidator(0), MaxValueValidator(20)], default=0)
    # race = models.ForeignKey() - after race model
    # heritage = models.ForeignKey - after heritage model
    # char_class = models.ForeignKey - after class model
    # size = models.ForeignKey - after size model
    alignment = models.CharField(max_length=2, blank=True, null=True, choices=Alignment.choices,
                                 default=Alignment.TRUE_NEUTRAL)
    # deity = models.ForeignKey() - after deity model

