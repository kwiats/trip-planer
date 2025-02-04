from typing import TYPE_CHECKING

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.db.models import QuerySet

if TYPE_CHECKING:
    from apps.users.models import User


class UserManager(BaseUserManager):
    def get_queryset(self) -> QuerySet["User"]:
        return super().get_queryset()

    def get_user(self, **kwargs) -> "User":
        return self.get_queryset().get(**kwargs)

    def get_user_by_id(self, user_id: int) -> "User":
        return self.get_queryset().get(id=user_id)

    def get_queryset_with_profile(self) -> QuerySet["User"]:
        return self.get_queryset().filter(profile__isnull=False).select_related("profile")

    def create_user(self, email: str, password: str, **extra_fields) -> "User":
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        if not password:
            raise ValueError("Password required")
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email: str, password: str, **extra_fields) -> "User":
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)

    def update_user(self, user: "User", **kwargs) -> "User":
        if "password" in kwargs:
            user.set_password(kwargs["password"])
            kwargs.pop("password")
        if "email" in kwargs:
            user.email = self.normalize_email(kwargs["email"])
            kwargs.pop("email")
        for key, value in kwargs.items():
            setattr(user, key, value)
        user.save()
        return user

    @staticmethod
    def delete_user(user: "User") -> None:
        user.delete()
