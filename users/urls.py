from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)


urlpatterns = [
    path("users/", views.UserView.as_view()),
    path("users/<int:user_id>/", views.UserDetailView.as_view()),
    path("users/login/", jwt_views.TokenObtainPairView.as_view()),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"
    ),
]
