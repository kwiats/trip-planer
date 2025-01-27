from dj_rest_auth.views import LogoutView
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from apps.auth.views import (
    FacebookConnectView,
    GitHubConnectView,
    LoginView,
    RegisterView,
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="rest_register"),
    path("login/", LoginView.as_view(), name="rest_login"),
    path("logout/", LogoutView.as_view(), name="rest_logout"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # social auth
    path("facebook/connect/", FacebookConnectView.as_view(), name="fb_connect"),
    path("github/connect/", GitHubConnectView.as_view(), name="github_connect"),
]
