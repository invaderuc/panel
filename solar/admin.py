from django.contrib.gis import admin
from models import Predios 

admin.site.register(Predios, admin.GeoModelAdmin)
#admin.site.register(Predios, admin.OSMGeoAdmin)
