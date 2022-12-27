from django.urls import path
from django.conf.urls import include

from rest_framework import routers

from .views import (
    UserViewSet,
    PostViewSet,
    LikeViewSet,
    ActivitiesViewSet,
    AnalyticsViewSet,
)

router = routers.DefaultRouter()
router.register("users", UserViewSet)
router.register("posts", PostViewSet)
router.register("likes", LikeViewSet, basename="like")
router.register("activities", ActivitiesViewSet)
router.register("analytics", AnalyticsViewSet, basename="analytics")

urlpatterns = [
    path("", include(router.urls)),
]
