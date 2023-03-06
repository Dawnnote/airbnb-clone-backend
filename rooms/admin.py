from django.contrib import admin
from .models import Room, Amenity

@admin.register(Room)
class RommAdmin(admin.ModelAdmin):
    pass

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    pass