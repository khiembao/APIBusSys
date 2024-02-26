from django.shortcuts import render
from django import forms
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime
from rest_framework import viewsets, generics, parsers, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from . import serializers, paginators
from .models import Destination, TripPath, User, Bus, Trip


class DestinationViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Destination.objects.all()
    serializer_class = serializers.DestinationSerializer

class TripPathViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = TripPath.objects.all()
    serializer_class = serializers.TripPathSerializer
    pagination_class = paginators.TripPathPaginator


    @action(methods=['get'], detail=True)
    def departure(self, request, pk):
        departure = self.get_object().departure_destination_set.filter(active=True).all()

        return Response(serializers.DestinationSerializer(departure, many=True, context={'request': request}).data,
                        status=status.HTTP_200_OK)



class BusViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Bus.objects.all()
    serializer_class = serializers.BusSerializer


    # def get_permissions(self):
    #     if self.action in ['add_buss']:
    #         return [permissions.IsAuthenticated()]
    #
    #     return self.permission_classes

class TripViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Trip.objects.all()
    serializer_class = serializers.TripSerializer

    def get_queryset(self):
        queries = self.queryset

        q = self.request.query_params.get("q")
        if q:
            queries = queries.filter(trip_path__icontains=q)

        return queries



class UserViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = User.objects.filter(is_active=True).all()
    serializer_class = serializers.UserSerializer
    parser_classes = [parsers.MultiPartParser]

    def get_permissions(self):
        if self.action.__eq__('current_user'):
            return [permissions.IsAuthenticated()]

        return [permissions.AllowAny()]
    @action(methods=['get'], url_name='current-user', detail=False)
    def current_user(self, request):
        return Response(serializers.UserSerializer(request.user).data)