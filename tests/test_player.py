from unittest import TestCase

from player import Player

class TestPlayer(TestCase):
    def test_create_player(self):
        p = Player()
        self.assertTrue(isinstance(p, Player))
