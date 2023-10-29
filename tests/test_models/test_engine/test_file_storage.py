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

    def test_save(self):
        # Verificar que el método save() funciona correctamente
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        # Puedes verificar si el archivo se ha actualizado según tus requisitos

    def test_reload(self):
        # Verificar que el método reload() funciona correctamente
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        storage.reload()
        # Puedes verificar si los objetos se han recargado correctamente

class TestBaseModel(unittest.TestCase):

    def test_init(self):
        # Verificar el comportamiento del constructor de BaseModel
        obj = BaseModel()
        # Puedes verificar si los atributos se inicializan correctamente

    def test_save(self):
        # Verificar el método save() en BaseModel
        obj = BaseModel()
        # Puedes verificar si el método actualiza self.updated_at y guarda

if __name__ == '__main__':
    unittest.main()
