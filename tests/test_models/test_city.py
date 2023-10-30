#!/usr/bin/python3
import unittest
from models.city import City


class TestCity(unittest.TestCase):

    def test_city_name(self):
        # Verificar que los atributos de City se inicializan correctamente
        city = City()
        self.assertTrue(hasattr(city, "name"))
