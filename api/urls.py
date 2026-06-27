from django.urls import include, path

from django.urls import include, path

urlpatterns = [
    path("auth/", include("accounts.urls")),
    path("projects/", include("projects.urls")),
    path("leads/", include("leads.urls")),
    path("documents/", include("documents.urls")),
    path("timeline/", include("timeline.urls")),
]
