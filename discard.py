#!/usr/bin/env python3

class Discard:

    def __init__(self):
        self.discard_pile = []

    def discard(self,card):
        self.discard_pile.append(card)

    def __str__(self):
        result = []
        for card in self.discard_pile:
            result.append(str(card))
            result.append("\n")
            return "".join(result)

