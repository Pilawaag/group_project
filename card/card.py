#!/usr/bin/env python3

class Card():
    def __init__(self, name, element):
        self._name = name
        self._element = element

    @property
    def name(self):
        return self._name

    @property
    def element(self):
        return self._element
