from pyray import *
from internal import *

change_directory(get_main_py_directory())

init_window(800, 600, 'demo')

set_target_fps(60)

deck = Deck(CardFactory())
log("INIT: OK")
deck.init_game()

debug_button_rect = Rectangle(100, 100, 30, 30)
debug_button_is_clicked = 0

class Client:
    def take_cards():
        pass

while not window_should_close():
    
    if debug_button_is_clicked:
        deck.spawn_card_to_cell(4, 69)
        deck.is_card_pack_completed()
    begin_drawing()
    clear_background(BLACK)
    draw_fps(0,0)
    debug_button_is_clicked = gui_button(debug_button_rect, "d")
    deck.draw_cards()
    end_drawing()



close_window()
