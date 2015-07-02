from django.contrib.gis.db import models
from django.utils.translation import ugettext, ugettext_lazy as _


class State(models.Model):

    name = models.CharField(max_length=50)
    code = models.CharField(max_length=2)
    geom = models.MultiPolygonField(srid=4674)
    simple_geom = models.MultiPolygonField(srid=4674, null=True)
    objects = models.GeoManager()

    def __str__(self):
        return '%s' % self.code

    class Meta:
        verbose_name = _('State')
        verbose_name_plural = _('States')


class City(models.Model):

    name = models.CharField(max_length=100)
    state = models.ForeignKey(State)
    geom = models.MultiPolygonField(srid=4674)
    objects = models.GeoManager()

    def __str__(self):
        return '%s - %s' % (self.name, self.state.code)

    class Meta:
        verbose_name = _('City')
        verbose_name_plural = _('Cities')