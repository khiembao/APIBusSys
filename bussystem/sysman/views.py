from django.shortcuts import render
from django import forms
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime
from rest_framework import viewsets, generics

from . import serializers, paginators
from .models import Destination, TripPath


class DestinationViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Destination.objects.all()
    serializer_class = serializers.DestinationSerializer

class TripPathViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = TripPath.objects.all()
    serializer_class = serializers.TripPathSerializer
    pagination_class = paginators.TripPathPaginator