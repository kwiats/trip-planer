from django.urls import path

from apps.users.views import (
    ChangeEmailView,
    ChangePasswordView,
    UserCreateView,
    UserDetailView,
)

urlpatterns = [
    path("detail/", UserDetailView.as_view(), name="user-detail"),
    path("create/", UserCreateView.as_view(), name="user-create"),
    path("change-password/", ChangePasswordView.as_view(), name="change-password"),
    path("change-email/", ChangeEmailView.as_view(), name="change-email"),
]
