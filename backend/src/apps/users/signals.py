import random

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from apps.users.models import Profile, User


@receiver(pre_save, sender=User)
def make_username_user(sender, instance, *args, **kwargs):  # noqa
    if instance.pk:
        try:
            user = User.objects.get(pk=instance.pk)
            if instance.username == user.username:
                return
        except User.DoesNotExist:
            pass

    if not instance.username:
        base_username = instance.email.split("@")[0]
        unique_username = base_username
        while User.objects.filter(username=unique_username).exists():
            random_number = random.randint(10000, 99999)
            unique_username = f"{base_username}_{random_number}"
        instance.username = unique_username


# @receiver(post_save, sender=User)
# def create_or_update_user_profile(sender, instance, created, **kwargs):  # noqa
#     if created:
#         Profile.objects.create(user=instance)
#     else:
#         if hasattr(instance, "profile"):
#             instance.profile.save()
