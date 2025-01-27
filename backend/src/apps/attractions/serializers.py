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
    categories = serializers.SerializerMethodField()

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

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        categories_names = validated_data.pop("add_categories", [])
        attraction = super().create(validated_data)
        categories = []
        for name in categories_names:
            category, created = Category.objects.get_or_create(name=name)
            categories.append(category)
        attraction.categories.set(categories)
        return attraction

    def update(self, instance, validated_data):
        validated_data["user"] = self.context["request"].user
        categories_names = validated_data.pop("add_categories", [])

        if categories_names:
            categories = []
            for name in categories_names:
                category, created = Category.objects.get_or_create(name=name)
                categories.append(category)
            instance.categories.set(categories)

        return super().update(instance, validated_data)


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
