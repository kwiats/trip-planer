import uuid

from django.db import models


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(
        "users.User",  # noqa
        related_name="comments",
        on_delete=models.CASCADE,
    )
    review = models.ForeignKey(
        "threads.Review",  # noqa
        related_name="comments",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "comment"
        verbose_name_plural = "comments"
        db_table = "comments"
        ordering = ["-created_at"]

    def __str__(self):
        return self.content
