from django.urls import path

from apps.threads.views import (
    CommentCreateView,
    CommentDetailView,
    ReviewCreateView,
    ReviewDetailView,
)

urlpatterns = [
    path("create", ReviewCreateView.as_view(), name="review-create"),
    path("<str:id>/", ReviewDetailView.as_view(), name="review-detail"),
    path("comment", CommentCreateView.as_view(), name="comment-create"),
    path("comment/<str:id>/", CommentDetailView.as_view(), name="comment-detail"),
]
