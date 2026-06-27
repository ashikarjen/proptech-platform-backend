from rest_framework import permissions, viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

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