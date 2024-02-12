from enum import Enum
from random import choice

class Suit(Enum):
    Clubs = 0
    Spades = 1
    Hearts = 2
    Diamonds = 3

    def random():
        return choice(list(Suit))