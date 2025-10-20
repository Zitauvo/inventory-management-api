from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="items")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class InventoryChangeLog(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="change_logs")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    change_type = models.CharField(max_length=50, choices=[
        ('added', 'Added'),
        ('removed', 'Removed'),
        ('updated', 'Updated')
    ])
    quantity_changed = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item.name} - {self.change_type} ({self.quantity_changed})"
