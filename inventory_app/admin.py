from django.contrib import admin
from .models import Category, Item, InventoryChangeLog


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity', 'user')
    list_filter = ('category',)
    search_fields = ('name', 'description')


@admin.register(InventoryChangeLog)
class InventoryChangeLogAdmin(admin.ModelAdmin):
    list_display = ('item', 'user', 'action', 'timestamp')
    list_filter = ('action', 'timestamp')
