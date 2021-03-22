from datetime import datetime

from django.db import models
from django.utils.crypto import get_random_string
from django.core.validators import MinValueValidator

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Sneakers', 'Sneakers'), 
        ('Boots', 'Boots'),
        ('Moccasins', 'Mocassins'),
        ('Loafers', 'Loafers'),
        ('Oxfords','Oxfords'),
    ]

    categories = models.CharField(max_length=254, null=True, blank=True)
    id = models.CharField(max_length=254, blank=True, primary_key=True)
    name = models.CharField(max_length=254)
    colors = models.CharField(max_length=254, null=True, blank=True)
    brand = models.CharField(max_length=254, null=True, blank=True)
    manufacturer = models.CharField(max_length=254, null=True, blank=True)
    descriptions = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(1)])
    imageURLs = models.URLField(max_length=1024, null=True, blank=True)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    sizes = models.CharField(max_length=254, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            self.pk = get_random_string(10)
        super().save(*args, **kwargs)
