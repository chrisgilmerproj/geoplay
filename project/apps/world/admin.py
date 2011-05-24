from django.conf import settings
from django.contrib.gis import admin
from django.contrib.gis.maps.google import GoogleMap

from world.models import WorldBorders

GMAP = GoogleMap(key=settings.GOOGLE_MAPS_API_KEY)

class WorldBordersAdmin(admin.OSMGeoAdmin):
	extra_js     = [GMAP.api_url + GMAP.key]
	map_template = 'gis/admin/google.html'

admin.site.register(WorldBorders, WorldBordersAdmin)
