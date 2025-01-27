from django.db import models

from apps.users.managers import ProfileManager


class Profile(models.Model):
    user = models.OneToOneField(
        "users.User",  # noqa
        on_delete=models.CASCADE,
        related_name="profile",
    )
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)

    objects = ProfileManager()

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name
