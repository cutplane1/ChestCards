from pyray import *
import random
from internal import Suit 

init_window(800, 600, 'demo')

set_target_fps(60)

class draw:
    def __enter__(self) -> None:
        begin_drawing()
    
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        end_drawing()


class Card:
    def __init__(self, suit: Suit, rank: int, x: int, y: int) -> None:
        self.suit = suit
        self.rank = str(rank)
        self.x = x
        self.y = y
        
        if suit.name is "Clubs" or suit.name is "Spades":
            self.color = BLACK
        else:
            self.color = RED

    def draw(self) -> None:
        draw_rectangle(self.x, self.y, 50, 70, WHITE)
        draw_text(self.rank, self.x + 2, self.y + 2, 20, self.color)


cards = []

# for i in range(1, 9 + 1):
#     cards.append(Card("lol", str(i), i * 10 * 6 + 50, 10))

# card spawn

for i in range(1, 9 + 1):
    cards.append(Card(random.choice(list(Suit)), i, i * 10 * 6 + 50, 500))

while not window_should_close():

    with draw():
        clear_background(BLACK)

        draw_rectangle(100, 10, 600, 100, BROWN)
        draw_text("enemy deck", 350, 50, 24, WHITE)

        draw_circle(500, 300, 60, GRAY)
        draw_text("card pack", 460, 290, 16, WHITE)
        
        for c in cards:
            c.draw()

close_window()
