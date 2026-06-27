from django.db import models

from common.models import BaseModel
from projects.models import Project


class Lead(BaseModel):

    STATUS_CHOICES = [
        ("new", "New"),
        ("contacted", "Contacted"),
        ("qualified", "Qualified"),
        ("closed", "Closed"),
    ]

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="leads",
    )

    name = models.CharField(max_length=150)

    email = models.EmailField()

    phone = models.CharField(max_length=20)

    message = models.TextField(
        blank=True,
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="new",
    )

    class Meta:
        ordering = ["-created_at"]
        
        constraints = [
            models.UniqueConstraint(
                fields=["project", "email"],
                name="unique_project_email",
            )
        ]

    def __str__(self):
        return self.name