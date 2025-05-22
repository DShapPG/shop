from django.db import models
from django.db.models import ForeignKey


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()
    category = ForeignKey(Category, on_delete=models.CASCADE)
