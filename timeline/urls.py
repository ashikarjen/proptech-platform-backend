from rest_framework.routers import DefaultRouter

from .views import ProjectTimelineViewSet

router = DefaultRouter()

router.register("", ProjectTimelineViewSet, basename="timeline")

urlpatterns = router.urls