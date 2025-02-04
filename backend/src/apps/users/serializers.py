from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from apps.users.models import Profile, User


class ChangePasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(required=True)
    rewrite_new_password = serializers.CharField(required=True)
    old_password = serializers.CharField(required=True)

    def validate(self, attrs):
        user = self.context["request"].user
        if not user.check_password(attrs["old_password"]):
            raise serializers.ValidationError("Wrong password")
        if attrs["new_password"] != attrs["rewrite_new_password"]:
            raise serializers.ValidationError("Passwords don't match")

        if all(
            [
                attrs["new_password"] == attrs["old_password"],
                attrs["rewrite_new_password"] == attrs["old_password"],
            ]
        ):
            raise serializers.ValidationError("New password can't be the same as the old one")

        self._validate_password(attrs["new_password"], user)
        return attrs

    @staticmethod
    def _validate_password(password: str, user: "User"):
        try:
            validate_password(password, user)
        except serializers.ValidationError as error:
            raise serializers.ValidationError(str(error))

    def update(self, instance, validated_data):
        instance = User.objects.update_user(
            user=instance,
            password=validated_data["new_password"],
        )
        return instance


class ChangeEmailSerializer(serializers.Serializer):
    new_email = serializers.EmailField(required=True)
    old_email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
    rewrite_password = serializers.CharField(required=True)

    def validate(self, attrs):
        user = self.context["request"].user
        if not user.check_password(attrs["password"]):
            raise serializers.ValidationError("Wrong password")
        if attrs["new_email"] == attrs["old_email"]:
            raise serializers.ValidationError(
                "New email can't be the same as the old one"
            )
        if attrs["password"] != attrs["rewrite_password"]:
            raise serializers.ValidationError("Passwords don't match")
        self._validate_password(attrs["password"], user)
        return attrs

    @staticmethod
    def _validate_password(password: str, user: "User"):
        try:
            validate_password(password, user)
        except serializers.ValidationError as error:
            raise serializers.ValidationError(str(error))

    def update(self, instance, validated_data):
        instance = User.objects.update_user(
            user=instance,
            email=validated_data["new_email"],
        )
        return instance


class ProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    full_name = serializers.CharField(read_only=True)

    class Meta:
        model = Profile
        fields = (
            "first_name",
            "last_name",
            "full_name",
        )


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    email = serializers.EmailField(read_only=True, required=False)
    first_name = serializers.CharField(write_only=True, required=False)
    last_name = serializers.CharField(write_only=True, required=False)

    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "profile",
        )
        read_only_fields = ("email", "username")

    def create(self, validated_data):
        profile_data = {
            "first_name": validated_data.pop("first_name", None),
            "last_name": validated_data.pop("last_name", None)
        }
        user = self.context["request"].user

        if not Profile.objects.filter(user=user).exists():
            Profile.objects.create_profile(
                user=user,
                **profile_data,
            )
        else:
            raise serializers.ValidationError(
                {
                    "detail": "First name or/and last name are "
                              "required to create a profile.",
                }
            )
        return user

    def update(self, instance, validated_data):
        profile_data = {
            "first_name": validated_data.pop("first_name", None),
            "last_name": validated_data.pop("last_name", None)
        }

        User.objects.update_user(
            user=instance,
            **validated_data,
        )

        if not hasattr(instance, "profile"):
            raise serializers.ValidationError(
                {
                    "detail": "User doesn't have a profile",
                }
            )
        else:
            Profile.objects.update_profile(
                profile=instance.profile, **profile_data
            )

        return instance
