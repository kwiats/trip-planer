from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from apps.attractions.models import Attraction, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "description",
        ]


class AttractionSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user_id = serializers.PrimaryKeyRelatedField(
        source="user",
        read_only=True,
    )
    add_categories = serializers.ListField(
        child=serializers.CharField(),
        write_only=True,
        required=False,
    )
    categories = serializers.SerializerMethodField(read_only=True)

    rating = serializers.SerializerMethodField(read_only=True)
    time_spent = serializers.SerializerMethodField(read_only=True)
    price = serializers.SerializerMethodField(read_only=True)
    visits = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Attraction
        fields = [
            "id",
            "name",
            "description",
            "longitude",
            "latitude",
            "open_hours",
            "address",
            "city",
            "country",
            "rating",
            "time_spent",
            "price",
            "visits",
            # nested
            "user_id",
            "user",
            "categories",
            "add_categories",
        ]

    def get_categories(self, obj) -> list[str]:  # noqa
        return [category.name for category in obj.categories.all()]

    @extend_schema_field(serializers.FloatField())
    def get_rating(self, obj):
        return obj.rating

    @extend_schema_field(serializers.FloatField())
    def get_time_spent(self, obj):
        return obj.time_spent

    @extend_schema_field(serializers.FloatField())
    def get_price(self, obj):
        return obj.price

    @extend_schema_field(serializers.IntegerField())
    def get_visits(self, obj):
        return obj.visits

    def create(self, validated_data):
        user = validated_data.pop("user")
        categories_names = validated_data.pop("add_categories", [])
        attraction = Attraction.objects.create(user=user, **validated_data)
        categories = []
        for name in categories_names:
            category, _ = Category.objects.get_or_create(name=name)
            categories.append(category)
        attraction.categories.add(*categories)
        attraction.save()
        return attraction

    def update(self, instance, validated_data):
        instance.user = validated_data.pop("user", instance.user)
        categories_names = validated_data.pop("add_categories", [])

        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()

        if categories_names:
            categories = []
            for name in categories_names:
                category, _ = Category.objects.get_or_create(name=name)
                categories.append(category)
            instance.categories.set(categories)

        return instance

class AttractionImagesSerializer(serializers.ModelSerializer):
    images_urls = serializers.SerializerMethodField()

    class Meta:
        model = Attraction
        fields = [
            "id",
            "images_urls",
        ]

    def get_images_urls(self, obj) -> list[str]:  # noqa
        return [image.file_url for image in obj.media.all()]
