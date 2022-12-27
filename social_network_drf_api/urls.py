from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework_simplejwt.views import TokenRefreshView

from api.views import JWTAuthenticationView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("login/", JWTAuthenticationView.as_view(), name="jwt_token"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
