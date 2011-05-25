from django.conf import settings
from django.contrib.gis import admin
from django.contrib.gis.geos import Point
from django.contrib.gis.maps.google import GoogleMap

from waypoints.forms import WaypointAdminForm
from waypoints.models import Waypoint

GMAP = GoogleMap()

class WaypointAdmin(admin.GeoModelAdmin):
	# Set a default location
	pnt = Point(-98.3,39.5, srid=4326)
	#pnt.transform(3857) #fallback (900913) # Use with OSMModelAdmin

	debug        = True
	default_lon, default_lat = pnt.coords	
	#extra_js     = [GMAP.api_url + GMAP.key]
	#form         = WaypointAdminForm
	list_display = ('name','geometry')
	#map_template = 'gis/admin/google.html'

admin.site.register(Waypoint, WaypointAdmin)
