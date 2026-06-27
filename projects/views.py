from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, viewsets

from .models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = [
        "status",
        "location",
        "is_active",
    ]

    search_fields = [
        "title",
        "location",
    ]

    ordering_fields = [
        "created_at",
        "investment_amount",
        "expected_roi",
    ]

    ordering = ["-created_at"]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Project.objects.all()

        return Project.objects.filter(is_active=True)

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [permissions.AllowAny()]

        return [permissions.IsAuthenticated()]