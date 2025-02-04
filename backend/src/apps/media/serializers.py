from django.core.validators import FileExtensionValidator
from rest_framework import serializers

from apps.attractions.models import Attraction
from apps.media.models import Media
from apps.media.services import MediaService
from apps.threads.models import Comment, Review
from core.storages import MediaS3Boto3Storage


class MediaCreateSerializer(serializers.ModelSerializer):
    file = serializers.FileField(
        write_only=True,
        required=True,
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png", "webp"])
        ],
    )
    bucket_name = serializers.CharField(required=False)
    file_name = serializers.CharField(required=True)
    file_type = serializers.CharField(
        required=False,
        allow_null=True,
        allow_blank=True,
    )
    attraction_id = serializers.PrimaryKeyRelatedField(
        queryset=Attraction.objects.all(),
        required=False,
        allow_null=True,
    )
    review_id = serializers.PrimaryKeyRelatedField(
        queryset=Review.objects.all(),
        required=False,
        allow_null=True,
    )
    comment_id = serializers.PrimaryKeyRelatedField(
        queryset=Comment.objects.all(),
        required=False,
        allow_null=True,
    )

    class Meta:
        model = Media
        fields = [
            "id",
            "bucket_name",
            "file_name",
            "file_type",
            "file",
            "created_at",
            "updated_at",
            "attraction_id",
            "review_id",
            "comment_id",
            "file_url",
        ]
        read_only_fields = [
            "id",
            "file_url",
            "created_at",
            "updated_at",
        ]

    def validate(self, data):
        file = self.context.get("request").FILES.get("file")

        if not file:
            raise serializers.ValidationError("File is required.")

        relations = ["attraction_id", "review_id", "comment_id"]
        set_relations = sum(1 for rel in relations if data.get(rel, None) is not None)

        if set_relations > 1:
            raise serializers.ValidationError(
                "Only one relation (attraction, review, or comment) can be set."
            )

        if set_relations == 0 and not data.get("bucket_name", None):
            raise serializers.ValidationError(
                "Bucket name is required if no relations are set."
            )
        return data

    def create(self, validated_data):
        media_service = MediaService(storage=MediaS3Boto3Storage())
        media = media_service.create_media(validated_data)

        return media


class MediaSerializer(serializers.ModelSerializer):
    bucket_name = serializers.CharField(required=False)
    file_name = serializers.CharField(required=True)
    file_type = serializers.CharField(
        required=False,
        allow_null=True,
        allow_blank=True,
    )
    attraction_id = serializers.PrimaryKeyRelatedField(
        queryset=Attraction.objects.all(),
        required=False,
        allow_null=True,
    )
    review_id = serializers.PrimaryKeyRelatedField(
        queryset=Review.objects.all(),
        required=False,
        allow_null=True,
    )
    comment_id = serializers.PrimaryKeyRelatedField(
        queryset=Comment.objects.all(),
        required=False,
        allow_null=True,
    )

    class Meta:
        model = Media
        fields = [
            "id",
            "file_url",
            "bucket_name",
            "file_name",
            "file_type",
            "created_at",
            "updated_at",
            "attraction_id",
            "review_id",
            "comment_id",
        ]
        read_only_fields = [
            "id",
            "file_url",
            "created_at",
            "updated_at",
        ]


class FileUrlListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ["file_url"]

    def to_representation(self, instance):
        return instance.file_url
