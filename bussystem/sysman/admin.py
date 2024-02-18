from django.contrib import admin
from .models import Destination


class DestinationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_filter = ['id', 'name']





# Register your models here.
admin.site.register(Destination, DestinationAdmin)