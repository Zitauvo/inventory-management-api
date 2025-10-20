from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ItemViewSet, InventoryChangeLogViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('items', ItemViewSet)
router.register('logs', InventoryChangeLogViewSet, basename='inventorylog')  # ✅ added basename

urlpatterns = [
    path('', include(router.urls)),
]
