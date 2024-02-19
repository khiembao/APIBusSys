from django.contrib import admin
from .models import Destination, Bus, TripPath, SpecialOccasion, Seat, Trip


class DestinationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_filter = ['id', 'name']


class TripPathAdmin(admin.ModelAdmin):
    list_display = ['id', 'departure_destination', 'arrival_destination', 'price']

class TripAdmin(admin.ModelAdmin):
    list_select_related = (
        'trip_path',
        'bus'
    )

# Register your models here.
admin.site.register(Destination, DestinationAdmin)
admin.site.register(Bus)
admin.site.register(TripPath, TripPathAdmin)
admin.site.register(Trip, TripAdmin)
