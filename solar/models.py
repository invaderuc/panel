from django.db import models

# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models

class Predios(models.Model):
    rol_manzan = models.CharField(max_length=11)
    numero_pre = models.CharField(max_length=250)
    otro = models.CharField(max_length=50)
    fid = models.IntegerField()
    geom = models.MultiPolygonField(srid=32718)
    objects = models.GeoManager()

# Auto-generated `LayerMapping` dictionary for Predios model
#predios_mapping = {
#    'rol_manzan' : 'ROL_MANZAN',
#    'numero_pre' : 'NUMERO_PRE',
#    'otro' : 'OTRO',
#    'fid' : 'FID',
#    'geom' : 'MULTIPOLYGON',
#}
