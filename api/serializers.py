from rest_framework import serializers

from products.models import Product
from inventory.models import Inventory
from sales.models import Sale


class ProductSerializer(serializers.ModelSerializer):

    class Meta:

        model = Product

        fields = "__all__"


class InventorySerializer(serializers.ModelSerializer):

    class Meta:

        model = Inventory

        fields = "__all__"


class SaleSerializer(serializers.ModelSerializer):

    class Meta:

        model = Sale

        fields = "__all__"