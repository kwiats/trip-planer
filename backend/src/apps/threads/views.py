from drf_spectacular.utils import OpenApiExample, extend_schema
from requests import Response
from rest_framework import generics, mixins, permissions

from apps.attractions.models import Attraction
from apps.threads.models import Comment, Review
from apps.threads.serializers import CommentSerializer, ReviewSerializer


class ReviewCreateView(
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Review.objects.prefetch_related("attraction").all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @extend_schema(
        tags=["reviews"],
        request=ReviewSerializer,
        responses=ReviewSerializer,
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ReviewDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "id"

    @extend_schema(
        tags=["reviews"],
        request=ReviewSerializer,
        responses=ReviewSerializer,
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @extend_schema(
        tags=["reviews"],
        request=ReviewSerializer,
        responses=ReviewSerializer,
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @extend_schema(
        tags=["reviews"],
        request=ReviewSerializer,
        responses=ReviewSerializer,
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @extend_schema(
        tags=["reviews"],
        responses={204: None},
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CommentCreateView(
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        tags=["comments"],
        request=CommentSerializer,
        responses=CommentSerializer,
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "id"

    @extend_schema(
        tags=["comments"],
        request=CommentSerializer,
        responses=CommentSerializer,
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @extend_schema(
        tags=["comments"],
        request=CommentSerializer,
        responses=CommentSerializer,
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @extend_schema(
        tags=["comments"],
        request=CommentSerializer,
        responses=CommentSerializer,
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @extend_schema(
        tags=["comments"],
        responses={204: None},
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)