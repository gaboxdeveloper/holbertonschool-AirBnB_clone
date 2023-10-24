#!/usr/bin/python3
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_to_dict(self):
        model = BaseModel()
        model.my_number = 42  # Establece un valor para my_number
        model.name = "Sample"  # Establece un valor para name

        expected_dict = {
            'my_number': 42,
            'name': 'Sample',
            '__class__': 'BaseModel',
            'updated_at': model.updated_at.isoformat(),
            'id': model.id,
            'created_at': model.created_at.isoformat()
        }

        self.assertEqual(model.to_dict(), expected_dict)

    def test_save(self):
        model = BaseModel()
        original_updated_at = model.updated_at
        model.save()
        new_updated_at = model.updated_at

        self.assertNotEqual(original_updated_at, new_updated_at)

if __name__ == '__main__':
    unittest.main()
