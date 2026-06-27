from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, viewsets

from .models import ProjectTimeline
from .serializers import ProjectTimelineSerializer


class ProjectTimelineViewSet(viewsets.ModelViewSet):
    queryset = ProjectTimeline.objects.all()
    serializer_class = ProjectTimelineSerializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = [
        "project",
    ]

    search_fields = [
        "title",
    ]

    ordering = [
        "event_date",
    ]