from rest_framework import serializers
from .models import Category, Item, InventoryChangeLog


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class ItemSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Item
        fields = [
            'id', 'user', 'name', 'description',
            'quantity', 'price', 'category', 'category_name',
            'date_added', 'last_updated'
        ]


class InventoryChangeLogSerializer(serializers.ModelSerializer):
    item_name = serializers.ReadOnlyField(source='item.name')
    user_name = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = InventoryChangeLog
        fields = [
            'id', 'item', 'item_name', 'user', 'user_name',
            'change_type', 'quantity_changed', 'timestamp'
        ]

