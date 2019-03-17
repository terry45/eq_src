from django.contrib import admin
from .models import Device, EquipmentModel, Manufacturer, Location
# Register your models here.

admin.site.register(Device)
admin.site.register(EquipmentModel)
admin.site.register(Manufacturer)
admin.site.register(Location)
