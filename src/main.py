from internal import *

pyray.change_directory(get_main_py_directory())

pyray.init_window(800, 600, 'demo')

pyray.set_target_fps(60)

deck = Deck(CardFactory())
log("Deck initiated")
# deck.init_game()
deck.spawn_card_to_cell(2, 4)
deck.spawn_card_to_cell(2, 5)
deck.spawn_card_to_cell(2, 6)

while not pyray.window_should_close():
    deck.card_selection()

    pyray.begin_drawing()
    pyray.clear_background(pyray.BLACK)
    pyray.draw_fps(0,0)
    deck.draw_cards()
    pyray.end_drawing()

deck.factory.unload()
log("Deck deinitiated")
pyray.close_window()
