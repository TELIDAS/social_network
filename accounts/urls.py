from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views

app_name = "accounts"
urlpatterns = [
    path(
        "api/token/", views.NPOObtainTokenPairView.as_view(),
        name="token_obtain_pair"
    ),
    path(
        "api/token/refresh/", jwt_views.TokenRefreshView.as_view(),
        name="token_refresh"
    ),
    path("api/token-verify/", jwt_views.TokenVerifyView.as_view(),
         name="token_verify"),
    path("api/register/", views.RegisterAPIView.as_view(),
         name="register_generic"),
    path("api/user/", views.UserLastLoginAPIView.as_view(),
         name="user_last_login"),
]
