
import unittest
from player import Discard

class TestDiscard(unittest.TestCase):

    def test_discard(self):
        pile = Discard()
        pile.discard("my soul")
        print(pile)

if __name__ == "__main__":
    unittest.main()
