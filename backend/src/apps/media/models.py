import uuid

from django.db import models

from apps.media.managers import MediaManager
from core.mixins.models import TimeStampedModel


class Media(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file_url = models.URLField(blank=True, null=True)
    bucket_name = models.CharField(max_length=255, db_index=True, blank=True, null=True)
    file_name = models.CharField(max_length=255)
    file_type = models.CharField(max_length=50, default="image/webp")

    attraction = models.ForeignKey(
        "attractions.Attraction",  # noqa
        related_name="media",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    review = models.ForeignKey(
        "threads.Review",  # noqa
        related_name="media",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    comment = models.ForeignKey(
        "threads.Comment",  # noqa
        related_name="media",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    objects = MediaManager()

    class Meta:
        verbose_name = "media"
        verbose_name_plural = "media"
        db_table = "media"
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["file_url"]),
            models.Index(fields=["bucket_name"]),
            models.Index(fields=["file_type"]),
        ]

    def __str__(self):
        return self.file_name
