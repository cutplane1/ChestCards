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
    if is_mouse_button_pressed(0):
        rel_cards = []
        for card in deck.all_cards():
            if check_collision_point_rec(get_mouse_position(), card.rectangle):
                rel_cards.append(card)
        try:
            last_card = rel_cards[-1]
        except IndexError:
            pass
        print("-------")
    
    if is_mouse_button_down(1):
        last_card = False
    
    if last_card != False:
        last_card.x = get_mouse_x() - 30
        last_card.y = get_mouse_y() - 30

    begin_drawing()
    clear_background(BLACK)
    draw_fps(0,0)
    draw_text(str(deck.score), 200, 200, 16, WHITE)
    deck.draw_cards()
    end_drawing()


deck.factory.unload()
close_window()
