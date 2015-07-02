# -*- coding: utf-8 -*-

import simplejson

from django.core.management.base import BaseCommand
from django.contrib.gis.geos import MultiPolygon, Polygon

from ...models import State, City


class Command(BaseCommand):
    args = 'filename'
    help = 'Import cities from a GeoJSON file'

    def handle(self, *args, **options):
        for filename in args:
            data_json = open(filename, 'r').read()
            data = simplejson.loads(data_json)

            for feature in data['features']:
                city = City(
                    name=feature['properties'].get('name'),
                    state=State.objects.get(name=feature['properties'].get('state')),
                    id=feature['properties'].get('ibge_geocode'),
                    )
                if feature['geometry'].get('type') == 'MultiPolygon':
                    city.geom = MultiPolygon(
                        [Polygon(poly) for poly in feature['geometry'].get('coordinates')[0]]
                        )
                else:
                    city.geom = MultiPolygon(Polygon(feature['geometry'].get('coordinates')[0]))
                city.save()