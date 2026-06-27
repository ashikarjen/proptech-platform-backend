from django.db import models
from django.utils.text import slugify

from common.models import BaseModel


class Project(BaseModel):

    STATUS_CHOICES = [
        ("upcoming", "Upcoming"),
        ("ongoing", "Ongoing"),
        ("completed", "Completed"),
    ]

    title = models.CharField(max_length=255)

    slug = models.SlugField(
        unique=True,
        blank=True,
    )

    description = models.TextField()

    location = models.CharField(max_length=255)

    thumbnail = models.ImageField(
        upload_to="projects/thumbnails/",
        blank=True,
        null=True,
    )

    video_url = models.URLField(
        blank=True,
        null=True,
    )

    investment_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    expected_roi = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="upcoming",
    )

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProjectImage(BaseModel):

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="images",
    )

    image = models.ImageField(
        upload_to="projects/gallery/",
    )

    caption = models.CharField(
        max_length=255,
        blank=True,
    )

    def __str__(self):
        return f"{self.project.title} Image"