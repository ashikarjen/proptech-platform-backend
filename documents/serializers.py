from rest_framework import serializers

from .models import ProjectDocument


class ProjectDocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectDocument
        fields = "__all__"
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )