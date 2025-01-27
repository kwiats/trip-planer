from django.urls import path

from apps.attractions.views import (
    AttractionCreateView,
    AttractionDestroyView,
    AttractionFilterView,
    AttractionImagesView,
    AttractionListView,
    AttractionRetrieveView,
    AttractionUpdateView,
    # category
    CategoryDetailView,
    CategoryView,
)

urlpatterns = [
    path(
        "filter",
        AttractionFilterView.as_view(),
        name="attraction-filter",
    ),
    path(
        "<str:id>/",
        AttractionRetrieveView.as_view(),
        name="attraction-detail",
    ),
    path(
        "<str:id>/update/",
        AttractionUpdateView.as_view(),
        name="attraction-update",
    ),
    path(
        "<str:id>/delete/",
        AttractionDestroyView.as_view(),
        name="attraction-delete",
    ),
    path(
        "<str:id>/images/",
        AttractionImagesView.as_view(),
        name="attraction-images",
    ),
    path("all", AttractionListView.as_view(), name="attraction-list"),
    path("create", AttractionCreateView.as_view(), name="attraction-create"),
    # category
    path("category/", CategoryView.as_view(), name="category-list"),
    path(
        "category/<str:id>/",
        CategoryDetailView.as_view(),
        name="category-detail",
    ),
]
