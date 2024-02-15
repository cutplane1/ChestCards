from pyray import *
from internal import *

init_window(800, 600, 'demo')

set_target_fps(60)

deck = Deck(CardFactory())
log("Game INIT")
deck.init_game()

while not window_should_close():
        begin_drawing()
        clear_background(BLACK)
        draw_fps(0,0)
        deck.draw_cards()
        end_drawing()

close_window()
