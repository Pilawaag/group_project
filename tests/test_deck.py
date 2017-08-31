from unittest import TestCase

from deck import Deck

class TestDeck(TestCase):
    def test_deck(self):
        d = Deck()
        self.assertIsInstance(d, Deck)

    def test_deck_length(self):
        d = Deck()
        self.assertEqual(len(d), 0)
