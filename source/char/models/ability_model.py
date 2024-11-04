from django.db import models




class AbilitiesModel(models.Model):
    strength = models.IntegerField(default=10)
    dexterity = models.IntegerField(default=10)
    constitution = models.IntegerField(default=10)
    intelligence = models.IntegerField(default=10)
    wisdom = models.IntegerField(default=10)
    charisma = models.IntegerField(default=10)

    def get_modifier(self, ability_name):
        score = getattr(self, ability_name, 0)
        return (score - 10) // 2

    @property
    def modifiers(self):
        return {ability: self.get_modifier(ability) for ability in
                ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']}
