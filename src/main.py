from pyray import *
from internal import *

change_directory(get_main_py_directory())

init_window(800, 600, 'demo')

set_target_fps(60)

deck = Deck(CardFactory())
log("OK")
deck.init_game()
# deck.spawn_card_to_cell(2, 4)

debug_button_rect = Rectangle(100, 100, 30, 30)
debug2_button_rect = Rectangle(140, 100, 30, 30)
debug_button_is_clicked = 0
debug2_button_is_clicked = 0

class Client:
    def take_cards(self):
        pass

while not window_should_close():
    if debug_button_is_clicked:
        deck.take_one_random_card()
        deck.is_card_pack_completed()
    if debug2_button_is_clicked:
        pass
    begin_drawing()
    clear_background(BLACK)
    draw_fps(0,0)
    draw_text(str(deck.score), 200, 200, 16, WHITE)
    debug_button_is_clicked = gui_button(debug_button_rect, "d")
    debug2_button_is_clicked = gui_button(debug2_button_rect, "2")
    deck.draw_cards()
    end_drawing()



close_window()
