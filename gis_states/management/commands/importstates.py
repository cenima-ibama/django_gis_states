# -*- coding: utf-8 -*-

import simplejson

from django.core.management.base import BaseCommand
from django.contrib.gis.geos import MultiPolygon, Polygon

from ...models import State


class Command(BaseCommand):
    args = 'filename'
    help = 'Import states from a GeoJSON file'

    def handle(self, *args, **options):
        for filename in args:
            data_json = open(filename, 'r').read()
            data = simplejson.loads(data_json)

            for feature in data['features']:
                state = State(
                    id=feature['properties'].get('id'),
                    name=feature['properties'].get('name'),
                    code=feature['properties'].get('code'),
                    )
                if feature['geometry'].get('type') == 'MultiPolygon':
                    state.geom = MultiPolygon(
                        [Polygon(poly) for poly in feature['geometry'].get('coordinates')[0]]
                        )
                else:
                    state.geom = MultiPolygon(Polygon(feature['geometry'].get('coordinates')[0]))
                state.save()