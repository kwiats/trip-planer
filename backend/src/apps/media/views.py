from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import (
    OpenApiExample,
    OpenApiResponse,
    extend_schema,
    inline_serializer,
)
from rest_framework import generics, mixins, serializers, status
from rest_framework.parsers import (
    FormParser,
    MultiPartParser,
)
from rest_framework.response import Response
from rest_framework.serializers import ListSerializer

from apps.media.models import Media
from apps.media.serializers import (
    FileUrlListSerializer,
    MediaCreateSerializer,
    MediaSerializer,
)
from apps.media.services import MediaService
from core.storages import MediaS3Boto3Storage


class MediaCreateView(
    generics.GenericAPIView,
):
    parser_classes = (
        MultiPartParser,
        FormParser,
    )

    def get_serializer_class(self):
        return MediaCreateSerializer

    @extend_schema(
        tags=["media"],
        request={
            "multipart/form-data": {
                "type": "object",
                "properties": {
                    "file": {
                        "type": "string",
                        "format": "binary",
                    },
                    "bucket_name": {"type": "string", "nullable": True},
                    "file_name": {"type": "string", "nullable": True},
                    "file_type": {"type": "string", "nullable": True},
                    "attraction_id": {"type": "integer", "nullable": True},
                    "review_id": {"type": "string", "format": "uuid", "nullable": True},
                    "comment_id": {
                        "type": "string",
                        "format": "uuid",
                        "nullable": True,
                    },
                },
                "required": [
                    "file",
                    "file_name",
                ],
            },
        },
        examples=[
            OpenApiExample(
                "multipart/form-data",
                value={
                    "id": "4334c077-0ed8-4bea-851e-f53e2fe81062",
                    "bucket_name": "attractions",
                    "file_name": "string",
                    "file_type": "image/webp",
                    "created_at": "2025-01-25T19:34:03.174593Z",
                    "updated_at": "2025-01-25T19:34:03.199366Z",
                    "attraction_id": 3,
                    "review_id": None,
                    "comment_id": None,
                    "file_url": "http://localhost:9000/attractions/3/string",
                },
            ),
        ],
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MediaListView(
    generics.ListAPIView,
):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

    @extend_schema(
        tags=["media"],
    )
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("Authorization"))
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class MediaDetailView(
    generics.GenericAPIView,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

    def get_object(self):
        service = MediaService(storage=MediaS3Boto3Storage())
        return service.get_media(media_id=str(self.kwargs["media_id"]))

    @extend_schema(
        tags=["media"],
        responses={
            200: MediaSerializer,
        },
    )
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("Authorization"))
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @extend_schema(
        tags=["media"],
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def perform_destroy(self, instance):
        service = MediaService(storage=MediaS3Boto3Storage())
        service.delete_media(instance)


class MediaByCommentView(generics.GenericAPIView):
    def get_serializer_class(self):
        return FileUrlListSerializer

    def get_queryset(self):
        return Media.objects.filter_by_comments(
            comment_id=str(self.kwargs["comment_id"])
        )

    @extend_schema(
        tags=["media"],
        request=FileUrlListSerializer,
        responses={
            200: OpenApiResponse(
                response=FileUrlListSerializer,
                examples=[
                    OpenApiExample(
                        "Comment media example",
                        value=[
                            "http://localhost:9000/comments/3fa85f64-5717-4562-b3fc-2c963f66afa6/string",
                            "http://localhost:9000/comments/3fa85f64-5717-4562-b3fc-2c963f66afa6/string",
                        ],
                    )
                ],
            )
        },
    )
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("Authorization"))
    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class MediaByReviewView(generics.GenericAPIView):
    def get_serializer_class(self):
        return FileUrlListSerializer

    def get_queryset(self):
        return Media.objects.filter_by_reviews(review_id=str(self.kwargs["review_id"]))

    @extend_schema(
        tags=["media"],
        request=FileUrlListSerializer,
        responses={
            200: OpenApiResponse(
                response=FileUrlListSerializer,
                examples=[
                    OpenApiExample(
                        "Review media example",
                        value=[
                            "http://localhost:9000/reviews/3fa85f64-5717-4562-b3fc-2c963f66afa6/string",
                            "http://localhost:9000/reviews/3fa85f64-5717-4562-b3fc-2c963f66afa6/string",
                        ],
                    )
                ],
            )
        },
    )
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("Authorization"))
    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class MediaByAttractionView(generics.GenericAPIView):
    def get_serializer_class(self):
        return FileUrlListSerializer

    def get_queryset(self):
        return Media.objects.filter_by_attraction(
            attraction_id=str(self.kwargs["attraction_id"])
        )

    @extend_schema(
        tags=["media"],
        request=FileUrlListSerializer,
        responses={
            200: OpenApiResponse(
                response=FileUrlListSerializer,
                examples=[
                    OpenApiExample(
                        "Attraction media example",
                        value=[
                            "http://localhost:9000/attractions/3/string",
                            "http://localhost:9000/attractions/3/string",
                        ],
                    )
                ],
            )
        },
    )
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("Authorization"))
    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)
