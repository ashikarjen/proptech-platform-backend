from django.contrib import admin

from .models import Investment


@admin.register(Investment)
class InvestmentAdmin(admin.ModelAdmin):

    list_display = (
        "investor",
        "project",
        "amount",
        "status",
        "investment_date",
    )

    search_fields = (
        "investor__email",
        "project__title",
    )

    list_filter = (
        "status",
        "project",
    )