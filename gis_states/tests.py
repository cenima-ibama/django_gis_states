from django.test import TestCase
from django.contrib.gis.geos import Polygon, MultiPolygon

from .models import State, City


class TestStateCityModels(TestCase):
    def setUp(self):
        poly1 = Polygon([[0, 0], [0, 1], [1, 1], [1, 0], [0, 0]])
        self.state1 = State(name='State One', code='01', geom=MultiPolygon(poly1))
        self.state1.save()

        poly2 = Polygon([[0, 0], [0, -1], [1, -1], [1, 0], [0, 0]])
        self.state2 = State(name='State Two', code='02', geom=MultiPolygon(poly2))
        self.state2.save()

        poly3 = Polygon([[0, 0], [0, 0.6], [0.6, 0.6], [0.6, 0], [0, 0]])
        self.city1 = City(name='City One', state=self.state1,
            geom=MultiPolygon(poly3)
            )
        self.city1.save()

        poly4 = Polygon([[0, 0], [0, -0.6], [0.6, -0.6], [0.6, 0], [0, 0]])
        self.city2 = City(name='City Two', state=self.state2,
            geom=MultiPolygon(poly4)
            )
        self.city2.save()

    def test_state_creation(self):
        self.assertEqual(self.state1.__str__(), '01')
        self.assertEqual(State.objects.all().count(), 2)

    def test_city_creation(self):
        self.assertEqual(self.city1.__str__(), 'City One - 01')
        self.assertEqual(City.objects.all().count(), 2)
