from rest_framework.routers import DefaultRouter

from .views import ProjectDocumentViewSet

router = DefaultRouter()
router.register("", ProjectDocumentViewSet, basename="documents")

urlpatterns = router.urls