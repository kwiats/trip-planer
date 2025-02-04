from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from drf_spectacular.utils import OpenApiExample, extend_schema
from rest_framework import generics, mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.users.models import User
from apps.users.serializers import (
    ChangeEmailSerializer,
    ChangePasswordSerializer,
    UserSerializer,
)


class ChangeEmailView(generics.GenericAPIView, mixins.UpdateModelMixin):
    permission_classes = [IsAuthenticated]
    serializer_class = ChangeEmailSerializer

    def get_object(self):
        return User.objects.get(id=self.request.user.id)

    @extend_schema(
        tags=["users"],
        request=ChangeEmailSerializer,
        examples=[
            OpenApiExample(
                "Change password example",
                value={
                    "new_email": "example@example.com",
                    "old_email": "old@old.com",
                    "password": "examplePassword1234",
                    "rewrite_password": "examplePassword1234",
                },
            )
        ],
    )
    def put(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
            partial=True,
            instance=self.get_object(),
            context={"request": request},
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"detail": "Email changed successfully"},
                status=status.HTTP_200_OK,
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class ChangePasswordView(generics.GenericAPIView, mixins.UpdateModelMixin):
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer

    def get_object(self):
        return User.objects.get_user_by_id(user_id=self.request.user.id)

    @extend_schema(
        tags=["users"],
        request=ChangePasswordSerializer,
        examples=[
            OpenApiExample(
                "Change password example",
                value={
                    "old_password": "examplePassword123",
                    "new_password": "examplePassword1234",
                    "rewrite_new_password": "examplePassword1234",
                },
            )
        ],
    )
    def put(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
            partial=True,
            instance=self.get_object(),
            context={"request": request},
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"detail": "Password changed successfully"},
                status=status.HTTP_200_OK,
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class UserDetailView(
    generics.RetrieveAPIView,
    generics.DestroyAPIView,
    generics.UpdateAPIView,
):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return User.objects.get_user_by_id(user_id=self.request.user.id)

    @extend_schema(tags=["users"])
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("Authorization"))
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @extend_schema(tags=["users"], responses={204: None})
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    @extend_schema(
        tags=["users"], request=UserSerializer, responses={200: UserSerializer}
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @extend_schema(
        tags=["users"], request=UserSerializer, responses={200: UserSerializer}
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class UserCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @extend_schema(
        tags=["users"],
        examples=[
            OpenApiExample(
                name="Create user example",
                value={
                    "first_name": "John",
                    "last_name": "Doe",
                },
            )
        ],
        request=UserSerializer,
        responses={
            201: UserSerializer,
            400: {
                "detail": "User already has a profile",
            },
        },
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
