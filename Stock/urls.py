from django.urls import path,include
from .views import All_StockViewSet,User_Stock_Set,Individual_StockSet
from Stock import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('stock', views.All_StockViewSet, basename="stock")
router.register('user-stock', views.All_StockViewSet, basename="user-stock")
router.register('individual_stock', views.All_StockViewSet, basename="individual-stock")


urlpatterns = [
    path('', include(router.urls)),
]