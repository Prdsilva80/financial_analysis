# core/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from financial_analysis import views as financial_views

# Criação do router para o Django REST framework
router = routers.DefaultRouter()
router.register(r'stocks', financial_views.StockViewSet, basename='stocks')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
