#!/usr/bin/python3
import unittest
from models.review import Review


class TestReview(unittest.TestCase):

    def test_review_text(self):
        # Verificar que los atributos de City se inicializan correctamente
        review = Review()
        self.assertTrue(hasattr(review, "name"))
        self.assertIsInstance(review.text, str)
        self.assertEqual(review.text, "")
