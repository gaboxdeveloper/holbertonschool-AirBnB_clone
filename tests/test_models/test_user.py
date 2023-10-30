#!/usr/bin/python3
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    def test_user_inherits_from_base_model(self):
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_user_attributes_default_values(self):
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_attributes_custom_values(self):
        custom_email = "test@example.com"
        custom_password = "my_password"
        custom_first_name = "John"
        custom_last_name = "Doe"

        user = User(email=custom_email, password=custom_password,
                    first_name=custom_first_name, last_name=custom_last_name)

        self.assertEqual(user.email, custom_email)
        self.assertEqual(user.password, custom_password)
        self.assertEqual(user.first_name, custom_first_name)
        self.assertEqual(user.last_name, custom_last_name)
