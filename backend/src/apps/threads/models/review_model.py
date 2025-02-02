import datetime
import uuid

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    time_spent = models.TimeField(default=datetime.time(00, 00), null=True, blank=True, help_text="HH:MM:SS")
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)

    user = models.ForeignKey(
        "users.User",  # noqa
        related_name="reviews",
        on_delete=models.CASCADE,
    )
    attraction = models.ForeignKey(
        "attractions.Attraction",  # noqa
        related_name="reviews",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "review"
        verbose_name_plural = "reviews"
        db_table = "reviews"

    def __str__(self):
        return self.title
