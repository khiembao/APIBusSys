from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Destination, Bus, TripPath, SpecialOccasion, Seat, Trip
from  ckeditor_uploader.widgets import CKEditorUploadingWidget

class DestinationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_filter = ['id', 'name']

class BussAdmin(admin.ModelAdmin):
    readonly_fields = ['image']

    def avatar(self, bus):
        if bus:
            return mark_safe(
                '<img src="/static/busses" width="120" />' \
                    .format(url=bus.image.name)
            )

class TripPathAdmin(admin.ModelAdmin):
    list_display = ['id', 'departure_destination', 'arrival_destination', 'price']

class TripAdmin(admin.ModelAdmin):
    list_select_related = (
        'trip_path',
        'bus'
    )
    list_display = ['id', 'trip_depart_time', 'trip_arrive_time', 'bus', 'trip_path']



# Register your models here.
admin.site.register(Destination, DestinationAdmin)
admin.site.register(Bus)
admin.site.register(TripPath, TripPathAdmin)
admin.site.register(Trip, TripAdmin)
