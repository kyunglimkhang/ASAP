from django.db import models
from django_random_queryset import RandomManager


class Keyword(models.Model):
    objects = RandomManager()
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Item(models.Model):
    asin = models.CharField(max_length=50, primary_key=True)
    title = models.CharField(max_length=150)
    price = models.FloatField(null=True)
    is_women = models.BooleanField()
    CATEGORIES = (
        ('top', 'top'),
        ('bottom', 'bottom'),
        ('outer', 'outer'),
        ('set', 'set'),
        ('sport', 'sport'),
        ('etc', 'etc'),
        ('shoes', 'shoes'),
        ('bag', 'bag'),
        ('accessories', 'accessories')
    )
    category = models.CharField(max_length=15, choices=CATEGORIES)
    keywords = models.ManyToManyField(Keyword, related_name='items')

    def __str__(self):
        return self.asin
