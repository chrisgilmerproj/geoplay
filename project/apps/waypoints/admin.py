from django.contrib.gis import admin
from waypoints.models import Waypoint

class WaypointAdmin(admin.OSMGeoAdmin):
	list_display = ('name','geometry')

admin.site.register(Waypoint, WaypointAdmin)
