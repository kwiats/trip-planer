import logging

from dj_rest_auth.registration.serializers import (
    RegisterSerializer as BaseRegisterSerializer,
)
from dj_rest_auth.serializers import LoginSerializer as BaseLoginSerializer
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from rest_framework import exceptions, serializers

from apps.users.models import User


class RegisterSerializer(BaseRegisterSerializer):
    id = serializers.UUIDField(read_only=True)
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    rewrite_password = serializers.CharField(write_only=True, required=True)

    def to_internal_value(self, data):
        if "password" in data:
            data["password1"] = data.get("password")
        if "rewrite_password" in data:
            data["password2"] = data.get("rewrite_password")
        return super().to_internal_value(data)

    def save(self, request):
        user = super().save(request)
        user.is_active = True
        user.save()
        return user


class LoginSerializer(BaseLoginSerializer):
    username = None

    def authenticate(self, email=None, password=None, **kwargs):
        try:
            user = User.objects.get_user(email=email)
        except User.DoesNotExist:
            return None
        else:
            if user.check_password(password) and self._user_can_authenticate(user):
                return user
        return None

    @staticmethod
    def _user_can_authenticate(user):
        is_active = getattr(user, "is_active", None)
        return is_active is True

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        if not email or not password:
            msg = _("Must include 'email' and 'password'.")
            raise exceptions.ValidationError(msg)

        user = self.authenticate(email=email, password=password)
        if not user:
            msg = _("Unable to log in with provided credentials.")
            raise exceptions.ValidationError(msg)

        self.validate_auth_user_status(user)

        # If required, is the email verified?
        if "dj_rest_auth.registration" in settings.INSTALLED_APPS:
            self.validate_email_verification_status(user, email=email)

        attrs["user"] = user
        return attrs
