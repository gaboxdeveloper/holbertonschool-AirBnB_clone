#!/usr/bin/python3
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    def test_amenity_name(self):
        # Verificar que el atributo 'name' se inicializa correctamente
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertIsInstance(amenity.name, str)
        self.assertEqual(amenity.name, "")
