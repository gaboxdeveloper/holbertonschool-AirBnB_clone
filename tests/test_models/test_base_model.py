#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        # Crear una instancia de BaseModel para las pruebas
        self.base_model = BaseModel()

    def test_save(self):
        # Verificar que el método save actualice self.updated_at
        updated_at_before = self.base_model.updated_at
        self.base_model.save()
        updated_at_after = self.base_model.updated_at
        self.assertNotEqual(updated_at_before, updated_at_after)

    def test_to_dict(self):
        # Verificar que el método to_dict devuelve un diccionario con atributos correctos
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')

    def test_self_id(self):
        # Verificar que self.id sea una cadena
        self.assertIsInstance(self.base_model.id, str)

    def test_self_created_at(self):
        # Verificar que self.created_at sea una instancia de datetime
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_str(self):
        # Verificar que el método __str__ devuelve una cadena
        obj_str = str(self.base_model)
        self.assertIsInstance(obj_str, str)

    def setUp(self):
        # Crear una instancia de FileStorage para las pruebas
        self.storage = FileStorage()
        # Crear una instancia de BaseModel para las pruebas
        self.base_model = BaseModel()
        # Agregar un objeto a __objects en FileStorage
        self.storage.new(self.base_model)

    def test_save(self):
        # Verificar que el método save() actualice self.updated_at
        updated_at_before = self.base_model.updated_at
        self.base_model.save()
        updated_at_after = self.base_model.updated_at
        self.assertNotEqual(updated_at_before, updated_at_after)
