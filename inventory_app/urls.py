from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet,
    ItemViewSet,
    InventoryChangeLogViewSet,
    register_user  # ✅ import the registration view
)

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('items', ItemViewSet)
router.register('logs', InventoryChangeLogViewSet, basename='inventorylog')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', register_user, name='register'),  # ✅ add this route
]
