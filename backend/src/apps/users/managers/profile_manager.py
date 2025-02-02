from typing import TYPE_CHECKING

from django.db import models
from django.db.models import QuerySet

if TYPE_CHECKING:
    from apps.users.models import Profile, User


class ProfileManager(models.Manager):
    def get_queryset(self) -> QuerySet["Profile"]:
        return super().get_queryset()

    def get_profile(self, user: "User", **kwargs) -> "Profile":
        return self.get_queryset().get(user=user, **kwargs)

    def get_profile_by_id(self, profile_id: int) -> "Profile":
        return self.get_queryset().get(id=profile_id)

    def create_profile(self, user: "User", **extra_fields) -> "Profile":
        profile = self.create(user=user, **extra_fields)
        profile.save()
        return profile

    @staticmethod
    def update_profile(profile: "Profile", **kwargs) -> "Profile":
        for key, value in kwargs.items():
            setattr(profile, key, value)
        profile.save()
        return profile

    @staticmethod
    def delete_profile(profile: "Profile") -> None:
        profile.delete()
