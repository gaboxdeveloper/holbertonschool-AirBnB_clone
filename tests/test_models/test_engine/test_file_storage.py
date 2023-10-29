#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def test_file_path(self):
        # Verificar que el atributo __file_path exista y sea una cadena
        storage = FileStorage()
        self.assertTrue(hasattr(storage, "_FileStorage__file_path"))
        self.assertIsInstance(storage._FileStorage__file_path, str)

    def test_objects(self):
        # Verificar que el atributo __objects exista y sea un diccionario
        storage = FileStorage()
        self.assertTrue(hasattr(storage, "_FileStorage__objects"))
        self.assertIsInstance(storage._FileStorage__objects, dict)

    def test_all(self):
        # Verificar que el método all() devuelve un diccionario
        storage = FileStorage()
        objects = storage.all()
        self.assertIsInstance(objects, dict)

    def test_new(self):
        # Verificar que el método new() funcione correctamente
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        objects = storage.all()
        self.assertIn(obj, objects.values())

    def setUp(self):
        # Crear una instancia de FileStorage para las pruebas
        self.storage = FileStorage()
        # Crear una instancia de BaseModel para las pruebas
        self.base_model = BaseModel()

    def test_save(self):
        # Verificar que el método save() funcione correctamente
        # Agregar un objeto a __objects
        key = "{}.{}".format(self.base_model.__class__.__name__, self.base_model.id)
        self.storage.new(self.base_model)
        self.storage.save()
        # Cargar los objetos nuevamente desde el archivo
        self.storage.reload()
        objects = self.storage.all()
        self.assertTrue(key in objects)
        saved_object = objects[key]
        self.assertEqual(saved_object.id, self.base_model.id)

    def test_reload(self):
        # Verificar que el método reload() funcione correctamente
        # Agregar un objeto a __objects
        key = "{}.{}".format(self.base_model.__class__.__name__, self.base_model.id)
        self.storage.new(self.base_model)
        self.storage.save()
        # Borrar el objeto existente en __objects
        del self.storage._FileStorage__objects[key]
        # Cargar los objetos nuevamente desde el archivo
        self.storage.reload()
        objects = self.storage.all()
        self.assertTrue(key in objects)
        reloaded_object = objects[key]
        self.assertEqual(reloaded_object.id, self.base_model.id)


if __name__ == '__main__':
    unittest.main()
