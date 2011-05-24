from django.conf import settings
from django.contrib.gis import admin
from django.contrib.gis.maps.google import GoogleMap

from waypoints.models import Waypoint

GMAP = GoogleMap(key=settings.GOOGLE_MAPS_API_KEY)

class WaypointAdmin(admin.OSMGeoAdmin):
	#default_lat  = 39.5
	#default_lon  = 89.35
	#default_zoom = 4
	extra_js     = [GMAP.api_url + GMAP.key]
	list_display = ('name','geometry')
	map_template = 'gis/admin/google.html'
	modifiable   = True

admin.site.register(Waypoint, WaypointAdmin)
