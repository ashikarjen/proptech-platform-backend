from django.db import models

from common.models import BaseModel
from accounts.models import User
from projects.models import Project


class Investment(BaseModel):

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    ]

    investor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="investments",
    )

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="investments",
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending",
    )

    investment_date = models.DateField()

    notes = models.TextField(
        blank=True,
    )

    class Meta:
        ordering = ["-investment_date"]

    def __str__(self):
        return f"{self.investor.email} - {self.project.title}"