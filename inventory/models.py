from django.db import models
from products.models import Product


class Inventory(models.Model):

    TRANSACTION_TYPES = [

        ('IN', 'Stock In'),

        ('OUT', 'Stock Out'),

        ('ADJUSTMENT', 'Adjustment')

    ]

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    quantity = models.IntegerField()

    transaction_type = models.CharField(
        max_length=20,
        choices=TRANSACTION_TYPES
    )

    date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"{self.product.name} - {self.transaction_type}"