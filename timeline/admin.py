from django.contrib import admin

from .models import ProjectTimeline


@admin.register(ProjectTimeline)
class ProjectTimelineAdmin(admin.ModelAdmin):

    list_display = (
        "project",
        "title",
        "event_date",
    )

    search_fields = (
        "title",
    )

    list_filter = (
        "project",
    )