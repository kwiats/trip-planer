from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from django.db.models import Avg, Count
from drf_spectacular.utils import (
    extend_schema,
)
from rest_framework import generics, mixins
from rest_framework.response import Response

from apps.attractions.models import Attraction
from apps.attractions.serializers import (
    AttractionImagesSerializer,
    AttractionSerializer,
    CategorySerializer,
)
from apps.attractions.schemas import attraction_examples, attraction_parameters


class CategoryView(
    generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin
):
    queryset = Attraction.objects.all()
    serializer_class = CategorySerializer

    @extend_schema(
        tags=["categories"],
        responses={200: CategorySerializer(many=True)},
        request=CategorySerializer(many=True),
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @extend_schema(
        tags=["categories"],
        responses={201: CategorySerializer},
        request=CategorySerializer,
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CategoryDetailView(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    queryset = Attraction.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "id"

    @extend_schema(tags=["categories"], responses={200: CategorySerializer})
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @extend_schema(
        tags=["categories"],
        request=CategorySerializer,
        responses={200: CategorySerializer},
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @extend_schema(
        tags=["categories"],
        request=CategorySerializer,
        responses={200: CategorySerializer},
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @extend_schema(tags=["categories"], responses={204: None})
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class AttractionListView(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer

    @extend_schema(
        tags=["attractions"],
        responses={200: AttractionSerializer(many=True)},
        request=AttractionSerializer(many=True),
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class AttractionCreateView(generics.GenericAPIView, mixins.CreateModelMixin):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer

    @extend_schema(
        tags=["attractions"],
        responses={201: AttractionSerializer},
        request=AttractionSerializer,
        examples=attraction_examples["attraction-create"],
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AttractionRetrieveView(generics.GenericAPIView, mixins.RetrieveModelMixin):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer
    lookup_field = "id"

    @extend_schema(tags=["attractions"], responses={200: AttractionSerializer})
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class AttractionUpdateView(generics.GenericAPIView, mixins.UpdateModelMixin):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer
    lookup_field = "id"

    @extend_schema(
        tags=["attractions"],
        request=AttractionSerializer,
        responses={200: AttractionSerializer},
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @extend_schema(
        tags=["attractions"],
        request=AttractionSerializer,
        responses={200: AttractionSerializer},
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class AttractionDestroyView(generics.GenericAPIView, mixins.DestroyModelMixin):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer
    lookup_field = "id"

    @extend_schema(tags=["attractions"], responses={204: None})
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class AttractionImagesView(generics.GenericAPIView):
    queryset = Attraction.objects.prefetch_related("media").all()
    serializer_class = AttractionImagesSerializer

    def get_object(self):
        return self.queryset.get(id=self.kwargs["id"])

    @extend_schema(
        tags=["attractions"],
        responses={200: AttractionImagesSerializer(many=True)},
        request=AttractionImagesSerializer(many=True),
    )
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class AttractionFilterView(generics.ListAPIView):
    serializer_class = AttractionSerializer

    def get_queryset(self):
        queryset = Attraction.objects.all()

        country = self.request.query_params.get("country")
        city = self.request.query_params.get("city")
        category = self.request.query_params.get("category")
        if country:
            queryset = queryset.filter(country=country)
        if city:
            queryset = queryset.filter(city=city)
        if category:
            queryset = queryset.filter(categories__name=category)

        latitude = self.request.query_params.get("latitude")
        longitude = self.request.query_params.get("longitude")
        radius = self.request.query_params.get("radius", 10000)
        if latitude and longitude:
            location = Point(float(longitude), float(latitude), srid=4326)
            queryset = (
                Attraction.objects.annotate(distance=Distance("location", location))
                .filter(distance__lte=radius)
                .order_by("distance")
            )

        sort_by = self.request.query_params.get("sort_by", "topRated")
        sort_direction = self.request.query_params.get("sort_direction", "desc")

        if sort_by == "topRated":
            queryset = (
                queryset.filter(reviews__isnull=False)
                .annotate(avg_rating=Avg("reviews__rating"))
                .order_by(f"-avg_rating" if sort_direction == "desc" else "avg_rating")
            )
        elif sort_by == "mostRated":
            queryset = (
                queryset.filter(reviews__isnull=False)
                .annotate(num_ratings=Count("reviews"))
                .order_by(
                    f"-num_ratings" if sort_direction == "desc" else "num_ratings"
                )
            )

        return queryset

    @extend_schema(
        summary="Retrieve attractions with filters",
        description=(
            "Retrieve a list of attractions with optional filters for location, category, and sorting options."
        ),
        parameters=attraction_parameters["attraction-retrieve"],
        responses={
            200: AttractionSerializer(many=True),
        },
    )
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
