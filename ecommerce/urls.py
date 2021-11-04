from django.urls import path
from django.urls.conf import include
from django.urls.resolvers import URLPattern

from ecommerce.views.products import (
    ProductListCreateAPIView,ProductRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('products/', include('ecommerce.routers'))
]
