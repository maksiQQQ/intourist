from django.test import TestCase
from django.urls import reverse
from django.db.models import QuerySet
from places.models import Place
from .factories import PlaceFactory

class PlaceListTestCase(TestCase):
    def test_open_list_success(self):
        place_1 = PlaceFactory(name='Cool place', description='Visit any time')
        place_2 = PlaceFactory()

        url = reverse('places-list') #/places/
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        places = response.context.get('places')
        self.assertIsInstance(places, QuerySet )
        # print(places)
        # print(response.context)
        # print(response.status_code)
        # places_2_db = Place.objects.get(name='Place number 1')
        self.assertEqual('Location - 1', places[1].location)
        self.assertEqual(places[0].description, 'Visit any time')


class PlaceCreateTestCase(TestCase):
    def test_create_place_success(self):
        url = reverse('create-place')
        data = {
            'name': 'Issyk-Kul',
            'location': 'Kara-Kol region',
            'description': 'Lake in KG'
        }
        response = self.client.post(url, data)
        place = Place.objects.last()
        self.assertEqual(place.name, 'Issyk-Kul')