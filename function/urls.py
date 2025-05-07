from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuItemViewSet, ContactViewSet

router = DefaultRouter()
router.register(r'menu-items', MenuItemViewSet)
router.register(r'contact', ContactViewSet)

urlpatterns = [
    path('', include(router.urls)),  # this was missing!
]
