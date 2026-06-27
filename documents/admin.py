from django.contrib import admin

from .models import ProjectDocument


@admin.register(ProjectDocument)
class ProjectDocumentAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "project",
        "created_at",
    )

    search_fields = (
        "title",
    )