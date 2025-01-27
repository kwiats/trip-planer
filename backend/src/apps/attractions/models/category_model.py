from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "categories"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name
