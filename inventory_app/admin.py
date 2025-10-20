from django.contrib import admin
from .models import Category, Item, InventoryChangeLog


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'category', 'quantity', 'price', 'date_added', 'last_updated')
    list_filter = ('category', 'date_added')
    search_fields = ('name', 'description', 'user__username')


@admin.register(InventoryChangeLog)
class InventoryChangeLogAdmin(admin.ModelAdmin):
    list_display = ('item', 'user', 'change_type', 'quantity_changed', 'timestamp')
    list_filter = ('change_type', 'timestamp')
    search_fields = ('item__name', 'user__username')

