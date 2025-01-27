from django.contrib.gis.db.models import PointField
from django.contrib.gis.geos import Point
from django.db import models
from django.db.models import Avg, Count


class Attraction(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    location = PointField(srid=4326, null=True, blank=True)
    open_hours = models.JSONField(
        null=True,
        blank=True,
        help_text="""
        {
            "monday": ["08:00", "17:00"],
            "tuesday": ["08:00", "17:00"],
            "wednesday": ["08:00", "17:00"],
            "thursday": ["08:00", "17:00"],
            "friday": ["08:00", "17:00"],
            "saturday": ["08:00", "17:00"],
            "sunday": ["08:00", "17:00"]}
    """,
    )
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    user = models.ForeignKey(
        "users.User",  # noqa
        related_name="attractions",
        on_delete=models.CASCADE,
    )
    categories = models.ManyToManyField(
        "attractions.Category",  # noqa
        related_name="attractions",
        blank=True,
    )

    @property
    def rating(self):
        return self.reviews.aggregate(rating_avg=Avg("rating")).get("rating_avg") or 0

    @property
    def time_spent(self):
        return (
            self.reviews.aggregate(time_spent_avg=Avg("time_spent")).get(
                "time_spent_avg"
            )
            or 0
        )

    @property
    def price(self):
        return self.reviews.aggregate(price_avg=Avg("price")).get("price_avg") or 0

    @property
    def visits(self):
        return self.reviews.aggregate(visits_count=Count("id")).get("visits_count") or 0

    class Meta:
        verbose_name = "attraction"
        verbose_name_plural = "attractions"
        db_table = "attractions"
        constraints = [
            models.UniqueConstraint(
                fields=["name", "longitude", "latitude"], name="unique_attraction"
            )
        ]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.longitude and self.latitude:
            self.location = Point(self.longitude, self.latitude, srid=4326)
        super().save(*args, **kwargs)
