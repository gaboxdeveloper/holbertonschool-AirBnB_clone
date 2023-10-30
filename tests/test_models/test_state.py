#!/usr/bin/python3
import unittest
from models.state import State


class TestState(unittest.TestCase):

    def test_state_name(self):
        # Verificar que el atributo 'name' se inicializa correctamente
        state = State()
        self.assertTrue(hasattr(state, "name"))
