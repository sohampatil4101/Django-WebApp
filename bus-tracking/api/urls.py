from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register('loc', views.BusLocViewSet)
router.register('bus', views.BusViewSet)
router.register('route', views.RouteViewSet)
router.register('bpoint', views.BPointViewSet)

urlpatterns = [
    path('', include(router.urls))
]
