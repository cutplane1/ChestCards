from pyray import *
from internal import *

change_directory(get_main_py_directory())

init_window(800, 600, 'demo')

set_target_fps(60)

deck = Deck(CardFactory())
log("Deck initiated")
# deck.init_game()
deck.spawn_card_to_cell(2, 4)
deck.spawn_card_to_cell(2, 5)
deck.spawn_card_to_cell(2, 6)

last_card = False

while not window_should_close():
    deck.card_selection()

    begin_drawing()
    clear_background(BLACK)
    draw_fps(0,0)
    deck.draw_cards()
    end_drawing()


deck.factory.unload()
close_window()
