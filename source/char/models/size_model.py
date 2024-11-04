from django.db import models

SIZES = [
    ("tiny", "Tiny"),
    ("small", "Small"),
    ("medium", "Medium"),
    ("large", "Large"),
    ("huge", "Huge"),
    ("gargantuan", "Gargantuan"),
]


class SizeModel(models.Model):
    title = models.CharField(choices=SIZES)
