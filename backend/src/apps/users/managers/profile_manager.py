from typing import TYPE_CHECKING

from django.db import models
from django.db.models import QuerySet

if TYPE_CHECKING:
    from apps.users.models import Profile


class ProfileManager(models.Manager):
    def get_queryset(self) -> QuerySet["Profile"]:
        return super().get_queryset()

    def get_queryset_with_user(self) -> QuerySet["Profile"]:
        return self.get_queryset().prefetch_related("user").all()

    def get_profile(self, user: "User", **kwargs) -> "Profile":
        return self.get_queryset().get(user=user, **kwargs)

    def create_profile(self, user: "User", **extra_fields) -> "Profile":
        return self.create(user=user, **extra_fields)

    @staticmethod
    def update_profile(profile: "Profile", **kwargs) -> "Profile":
        for key, value in kwargs.items():
            setattr(profile, key, value)
        profile.save()
        return profile

    @staticmethod
    def delete_profile(profile: "Profile") -> None:
        profile.delete()
