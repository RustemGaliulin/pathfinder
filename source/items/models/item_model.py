from django.db import models


class ItemModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    level = models.IntegerField()
    bulk = models.IntegerField()
    # item_damage = models.DecimalField(max_digits=10, decimal_places=) needs to be defined
    shoddy = models.BooleanField()
    descriptors = models.ManyToManyField('items.DescriptorModel', related_name='items')
