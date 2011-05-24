from django.contrib.gis.db import models

class Waypoint(models.Model):

	name     = models.CharField(max_length=32)
	geometry = models.PointField(srid=4326)

	objects  = models.GeoManager()
	
	def __unicode__(self):
		return '%s %s %s' % (self.name, self.geometry.x, self.geometry.y)
	
	# Custom latitude property
	def _get_latitude(self): return self.geometry.y
	def _set_latitude(self, value): self.geometry.y = value
	latitude = property(_get_latitude,_set_latitude)
	
	# Custom longitude property
	def _get_longitude(self): return self.geometry.x
	def _set_longitude(self, value): self.geometry.x = value
	longitude = property(_get_longitude,_set_longitude)
