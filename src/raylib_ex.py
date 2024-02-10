from pyray import *

init_window(800, 600, 'demo')

set_target_fps(60)

class draw:
    def __enter__(self):
        begin_drawing()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        end_drawing()


class Card:
    def __init__(self, suit, rank, x, y) -> None:
        self.suit = suit
        self.rank = rank
        self.x = x
        self.y = y


    def draw(self) -> None:
        draw_rectangle(self.x, self.y,50,70,RED)

c = Card("bc", 8, 5, 5)


while not window_should_close():
    c.x += 2

    with draw():
        clear_background(RAYWHITE)
        c.draw()



close_window()