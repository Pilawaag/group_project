
class Deck(object):
    def __init__(self):
        self.deck = []

    @property    
    def count(self):
        return len(self.deck)

