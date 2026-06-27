from django.db import models

from common.models import BaseModel
from projects.models import Project


class ProjectTimeline(BaseModel):

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="timeline",
    )

    title = models.CharField(max_length=255)

    description = models.TextField()

    event_date = models.DateField()

    class Meta:
        ordering = ["event_date"]

    def __str__(self):
        return f"{self.project.title} - {self.title}"