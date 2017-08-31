
import unittest
from player import Discard

class TestDiscard(unittest.TestCase):

    def test_discard(self):
        pile = Discard()
        pile.discard("my soul")
        self.assertEqual(pile.__str__(), "my soul\n")

if __name__ == "__main__":
    unittest.main()
