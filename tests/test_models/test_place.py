#!/usr/bin/python3
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):

    def test_place_attributes(self):
        # Verificar que los atributos de City se inicializan correctamente
        place = Place()
        self.assertTrue(hasattr(place, "name"))
        self.assertIsInstance(place.name, str)
        self.assertEqual(place.name, "")

        self.assertTrue(hasattr(place, "city_id"))
        self.assertIsInstance(place.city_id, str)
        self.assertEqual(place.city_id, "")

        self.assertTrue(hasattr(place, "user_id"))
        self.assertIsInstance(place.user_id, str)
        self.assertEqual(place.user_id, "")
