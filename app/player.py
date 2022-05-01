from typing import NamedTuple


class Player(NamedTuple):
    def __init__(self, name, nog):
        self.name = nog
        self.nog = nog