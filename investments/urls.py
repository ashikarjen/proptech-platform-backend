from rest_framework.routers import DefaultRouter

from .views import InvestmentViewSet

router = DefaultRouter()

router.register("", InvestmentViewSet, basename="investments")

urlpatterns = router.urls