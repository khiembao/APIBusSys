from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path
from django.utils.safestring import mark_safe
from sysman import dao

from .models import Destination, Bus, TripPath, SpecialOccasion, Seat, Trip
from  ckeditor_uploader.widgets import CKEditorUploadingWidget

class BussAppAdminSite(admin.AdminSite):
    site_header = 'iBussCorp'

    def get_urls(self):
        return [
                path('bus-stats/', self.stats_view)
        ] + super().get_urls()

    def stats_view(self, request):
        return TemplateResponse(request, 'admin/stats.html',{
                    'stats_departure': dao.count_departure_by_destination(),
                    'stats_arrival': dao.count_arrival_by_destination()
            })

admin_site = BussAppAdminSite(name='buss_app')

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
admin_site.register(Destination, DestinationAdmin)
admin_site.register(Bus)
admin_site.register(TripPath, TripPathAdmin)
admin_site.register(Trip, TripAdmin)
admin_site.register(SpecialOccasion)
