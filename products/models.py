from django.db import models

class Product(models.Model):

    product_id = models.CharField(max_length=50)

    name = models.CharField(max_length=100)

    category = models.CharField(max_length=100)

    brand = models.CharField(max_length=100)

    price = models.FloatField()

    stock = models.IntegerField()

    def __str__(self):
        return self.name
