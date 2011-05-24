from django.contrib.gis import admin
from world.models import WorldBorders

#admin.site.register(WorldBorders, admin.GeoModelAdmin)
admin.site.register(WorldBorders, admin.OSMGeoAdmin)
