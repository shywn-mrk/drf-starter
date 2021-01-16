from rest_framework import routers
from api.views import ProductViewSet

router = routers.DefaultRouter()

router.register('products', ProductViewSet, basename='products')
