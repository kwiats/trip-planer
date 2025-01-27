from django.urls import path

from apps.media.views import (
    MediaByAttractionView,
    MediaByCommentView,
    MediaByReviewView,
    MediaCreateView,
    MediaDetailView,
    MediaListView,
)

urlpatterns = [
    path("", MediaListView.as_view(), name="media-list"),
    path("create/", MediaCreateView.as_view(), name="media-create"),
    path("<str:media_id>/", MediaDetailView.as_view(), name="media-detail"),
    path(
        "by-attraction/<str:attraction_id>/",
        MediaByAttractionView.as_view(),
        name="media-by-attraction",
    ),
    path(
        "by-comment/<str:comment_id>/",
        MediaByCommentView.as_view(),
        name="media-by-comment",
    ),
    path(
        "by-review/<str:review_id>/",
        MediaByReviewView.as_view(),
        name="media-by-review",
    ),
]
