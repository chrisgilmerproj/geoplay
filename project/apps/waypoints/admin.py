from django.conf import settings
from django.contrib.gis import admin
from django.contrib.gis.geos import Point
from django.contrib.gis.maps.google import GoogleMap

from waypoints.forms import WaypointAdminForm
from waypoints.models import Waypoint

GMAP = GoogleMap(key=settings.GOOGLE_MAPS_API_KEY)

class WaypointAdmin(admin.OSMGeoAdmin):
	# Set a default location
	pnt = Point(-99.263813,19.370405, srid=4326)
	pnt.transform(900913)

	default_lon, default_lat = pnt.coords	
	default_zoom = 4
	extra_js     = [GMAP.api_url + GMAP.key]
	form         = WaypointAdminForm
	list_display = ('name','geometry')
	map_template = 'gis/admin/google.html'

admin.site.register(Waypoint, WaypointAdmin)
