from rest_framework import permissions, viewsets

from .models import ProjectDocument
from .serializers import ProjectDocumentSerializer


class ProjectDocumentViewSet(viewsets.ModelViewSet):
    queryset = ProjectDocument.objects.all()
    serializer_class = ProjectDocumentSerializer
    permission_classes = [permissions.IsAuthenticated]