# from django.conf import settings
from django.db import models
# from django.utils import timezone
#



class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    calories = models.PositiveIntegerField()
    category = models.CharField(max_length=50, choices=[('Food', 'Food'), ('Drink', 'Drink'), ('Dessert', 'Dessert')])

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    img_url = models.FileField(upload_to='image', max_length=254)
    calories = models.TextField()
    protein = models.IntegerField()

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=100)
    product_type = models.CharField(max_length=50)
    image = models.ImageField(upload_to='product_images/')
    image_hash = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return self.name







class About(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField()
    feedback = models.CharField(max_length=200)

    def __str__(self):
        return self.name