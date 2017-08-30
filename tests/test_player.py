from unittest import TestCase

from player import Player

class TestPlayer(TestCase):
    def test_create_player(self):
        p = Player()
        self.assertTrue(isinstance(p, Player))

    def test_draw_card(self):
        p = Player()
        c = p.draw()
        self.assertTrue(isinstance(c, None))
