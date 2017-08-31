#!/usr/bin/env python3

import unittest
from card import Card

class TestCard(unittest.TestCase):
    def test_create_card(self):
        c = Card("name", "fire")
        self.assertTrue(isinstance(c, Card))

    def test_get_card_properties(self):
        c = Card("name", "fire")
        self.assertEqual(c.name, "name")
        self.assertEqual(c.element, "fire")

    def test_cannot_change_name_or_element(self):
        c = Card("name", "fire")
        with self.assertRaises(AttributeError):
            c.name = "ben"
        with self.assertRaises(AttributeError):
            c.element = "water"

if __name__ == "__main__":
    unittest.main()
