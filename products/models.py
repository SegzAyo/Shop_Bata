from django.db import models

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
    price = models.DecimalField(max_digits=6, decimal_places=2)
    imageURLs = models.URLField(max_length=1024, null=True, blank=True)
    sizes = models.CharField(max_length=254, null=True, blank=True)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name
