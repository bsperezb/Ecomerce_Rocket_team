from rest_framework.routers import DefaultRouter
from ecommerce.views.products import ProductViewSet

router = DefaultRouter()

router.register(r'products', ProductViewSet, basename='products')

urlpatterns = router.urls