from django.db import models


class Proficiency(models.Model):
    UNTRAINED = "U"
    TRAINED = "T"
    EXPERT = "E"
    MASTER = "M"
    LEGENDARY = "L"

    PROFICIENCY_CHOICES = [
        (UNTRAINED, "Untrained"),
        (TRAINED, "Trained"),
        (EXPERT, "Expert"),
        (MASTER, "Master"),
        (LEGENDARY, "Legendary"),
    ]

    level = models.CharField(max_length=1, choices=PROFICIENCY_CHOICES, unique=True)
    name = models.CharField(max_length=20, unique=True)
    bonus = models.IntegerField()