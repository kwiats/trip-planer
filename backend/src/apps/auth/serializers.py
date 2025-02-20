from dj_rest_auth.registration.serializers import (
    RegisterSerializer as BaseRegisterSerializer,
)
from dj_rest_auth.serializers import LoginSerializer as BaseLoginSerializer
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from rest_framework import exceptions
from rest_framework import serializers
from urllib.parse import quote, urlencode
from allauth.mfa.models import Authenticator
from allauth.mfa.adapter import get_adapter
from apps.auth.utils import generate_otp, convert_to_base64

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


class MFASetupSerializer(serializers.Serializer):
    def create(self, validated_data):
        user = self.context['request'].user
        adapter = get_adapter()

        existing_totp = Authenticator.objects.filter(
            user=user,
            type=Authenticator.Type.TOTP
        ).first()

        if existing_totp:
            raise serializers.ValidationError({
                'mfa': 'Totp is already exists'
            })

        number = generate_otp()
        secret = convert_to_base64(number)

        authenticator = Authenticator.objects.create(
            user=user,
            type=Authenticator.Type.TOTP,
            data={
                'secret': adapter.encrypt(secret),
                'digits': settings.MFA_TOTP_DIGITS,
                'period': settings.MFA_TOTP_PERIOD,
                'algorithm': 'SHA1',
                'confirmed': False
            }
        )

        totp_url = adapter.build_totp_url(user, authenticator.data['secret'])

        return {
            'secret': secret,
            'qr_url': totp_url
        }

    def to_representation(self, instance):
        return {
            'secret': instance['secret'],
            'qr_url': instance['qr_url']
        }


class MFAVerifySerializer(serializers.Serializer):
    code = serializers.CharField()

    def validate(self, attrs):
        user = self.context['request'].user
        try:
            authenticator = Authenticator.objects.get(
                user=user,
                type=Authenticator.Type.TOTP
            )

            adapter = get_adapter()
            secret = adapter.decrypt(authenticator.data['secret'])

            if secret != attrs['code']:
                raise serializers.ValidationError({
                    'code': 'Wrong code'
                })

            authenticator.data['confirmed'] = True
            authenticator.save()

        except Authenticator.DoesNotExist:
            raise serializers.ValidationError({
                'mfa': 'MFA is not enabled'
            })

        return attrs


class MFAStatusSerializer(serializers.Serializer):
    mfa_enabled = serializers.BooleanField(read_only=True)
    type = serializers.CharField(read_only=True)

    def to_representation(self, instance):
        return {
            'mfa_enabled': instance['mfa_enabled'],
            'type': instance['type']
        }