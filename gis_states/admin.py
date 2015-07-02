from django.contrib.gis import admin

from .models import State, City


admin.site.register(State, admin.OSMGeoAdmin)
admin.site.register(City, admin.OSMGeoAdmin)
