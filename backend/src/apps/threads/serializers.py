import datetime

from rest_framework import serializers

from apps.attractions.models import Attraction
from apps.media.serializers import MediaSerializer
from apps.threads.models import Comment, Review


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user_id = serializers.CharField(source="user.id", read_only=True)
    review_id = serializers.PrimaryKeyRelatedField(
        source="review",
        queryset=Review.objects.all(),
        required=True,
        write_only=True,
    )
    media = MediaSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = [
            "id",
            "content",
            "created_at",
            "user",
            "user_id",
            "review_id",
            "media",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "media",
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['review_id'] = str(instance.review.id)
        return data


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    attraction_id = serializers.PrimaryKeyRelatedField(
        source="attraction",
        queryset=Attraction.objects.all(),
        required=True,
        write_only=True,
    )
    media = MediaSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = [
            "id",
            "rating",
            "price",
            "time_spent",
            "title",
            "description",
            # nested
            "user",
            "attraction_id",
            "media",
            "comments",
        ]
        read_only_fields = [
            "id",
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['attraction_id'] = instance.attraction.id
        return data

    def validate_rating(self, value):  # noqa
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5")
        return value

    def validate_price(self, value):  # noqa
        if value < 0:
            raise serializers.ValidationError("Price cannot be negative")
        return value

    def validate_time_spent(self, value):  # noqa
        if value is not None and isinstance(value, datetime.time):
            if value < datetime.time(0, 0):
                raise serializers.ValidationError("Time spent cannot be negative")
        return value
