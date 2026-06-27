from django.urls import include, path

from django.urls import include, path

urlpatterns = [
    path("auth/", include("accounts.urls")),
    path("projects/", include("projects.urls")),
    path("leads/", include("leads.urls")),
]
