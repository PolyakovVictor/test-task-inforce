from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RestaurantViewSet, MenuViewSet, VoteViewSet

router = DefaultRouter()
router.register(r"restaurants", RestaurantViewSet)
router.register(r"menus", MenuViewSet)
router.register(r"votes", VoteViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
