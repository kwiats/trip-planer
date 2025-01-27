import datetime

from rest_framework import serializers

from apps.attractions.models import Attraction
from apps.media.serializers import MediaSerializer
from apps.threads.models import Comment, Review


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    review_id = serializers.UUIDField(source="review.id", required=True)
    user_id = serializers.PrimaryKeyRelatedField(source="user", read_only=True)
    media = MediaSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = [
            "id",
            "content",
            "created_at",
            "user",
            "review_id",
            "user_id",
            "media",
        ]
        read_only_fields = [
            "created_at",
        ]

    def create(self, validated_data):
        review_id = validated_data.pop("review").get("id")
        try:
            review = Review.objects.get(id=review_id)
        except Review.DoesNotExist:
            raise serializers.ValidationError({"detail": "Review not found"})

        validated_data["review"] = review
        return super().create(validated_data)


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    attraction_id = serializers.PrimaryKeyRelatedField(
        queryset=Attraction.objects.all(),
        required=True,
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
