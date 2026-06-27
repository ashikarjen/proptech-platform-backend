from django.db import models

from common.models import BaseModel
from projects.models import Project


class ProjectDocument(BaseModel):

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="documents",
    )

    title = models.CharField(max_length=255)

    file = models.FileField(
        upload_to="projects/documents/",
    )

    description = models.TextField(
        blank=True,
    )

    def __str__(self):
        return self.title