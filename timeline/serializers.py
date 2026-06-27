from rest_framework import serializers

from .models import ProjectTimeline


class ProjectTimelineSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectTimeline
        fields = "__all__"
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )