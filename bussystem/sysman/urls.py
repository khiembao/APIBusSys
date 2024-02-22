
from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('destinations', views.DestinationViewSet, basename='destinations')
router.register('trip-paths', views.TripPathViewSet, basename='trip-paths')
urlpatterns = [
    path('', include(router.urls)),

]
