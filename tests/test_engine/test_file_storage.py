import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        # Crear una instancia de FileStorage para las pruebas
        self.storage = FileStorage()

    def test_file_path(self):
        # Verificar que el atributo __file_path exista y sea una cadena
        self.assertTrue(hasattr(self.storage, "_FileStorage__file_path"))
        self.assertIsInstance(self.storage._FileStorage__file_path, str)

    def test_objects(self):
        # Verificar que el atributo __objects exista y sea un diccionario
        self.assertTrue(hasattr(self.storage, "_FileStorage__objects"))
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_all(self):
        # Verificar que el método all() devuelve un diccionario
        objects = self.storage.all()
        self.assertIsInstance(objects, dict)

    def test_new(self):
        # Verificar que el método new() funcione correctamente
        obj = BaseModel()
        self.storage.new(obj)
        objects = self.storage.all()
        self.assertIn(obj, objects.values())

    def test_save(self):
        # Verificar que el método save() funcione correctamente
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        # Puedes verificar si el archivo se ha actualizado según tus requisitos

    def test_reload(self):
        # Verificar que el método reload() funcione correctamente
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        # Puedes verificar si los objetos se han recargado correctamente

if __name__ == '__main__':
    unittest.main()
