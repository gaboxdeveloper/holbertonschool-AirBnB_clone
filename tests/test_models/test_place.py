#!/usr/bin/python3
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):

    def test_place_attributes(self):
        # Verificar que los atributos de City se inicializan correctamente
        place = Place()
        self.assertTrue(hasattr(place, "name"))

        self.assertTrue(hasattr(place, "city_id"))

        self.assertTrue(hasattr(place, "user_id"))
