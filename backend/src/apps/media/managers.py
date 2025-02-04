from typing import TYPE_CHECKING, BinaryIO, Optional, Type

from django.db import models

if TYPE_CHECKING:
    from apps.attractions.models import Attraction
    from apps.media.models import Media
    from apps.threads.models import Comment, Review


class MediaManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def create_media(
        self,
        media_id: str,
        bucket_name: str,
        file_name: str,
        file_url: str,
        file_type: str | None = None,
        attraction: Optional["Attraction"] = None,
        review: Optional["Review"] = None,
        comment: Optional["Comment"] = None,
    ):
        media = self.model(
            id=media_id,
            bucket_name=bucket_name,
            file_name=file_name,
            file_url=file_url,
            file_type=file_type,
            attraction=attraction,
            review=review,
            comment=comment,
        )
        media.save()
        return media

    @staticmethod
    def update_media(
        media: "Media",
        **kwargs,
    ):
        for key, value in kwargs.items():
            setattr(media, key, value)
        media.save()
        return media

    def get_media(self, bucket_name: str, filename: str, **kwargs):
        return self.get(bucket_name=bucket_name, filename=filename, **kwargs)

    def delete_media(self, bucket_name: str, filename: str, **kwargs):
        return self.get(bucket_name=bucket_name, filename=filename, **kwargs).delete()

    def filter_by_attraction(self, attraction_id: str):
        return self.filter(attraction_id=attraction_id)

    def filter_by_reviews(self, review_id: str):
        return self.filter(review_id=review_id)

    def filter_by_comments(self, comment_id: str):
        return self.filter(comment_id=comment_id)
