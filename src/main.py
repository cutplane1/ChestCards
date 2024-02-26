from internal import *

pyray.change_directory(get_main_py_directory())

pyray.init_window(800, 600, 'demo')

pyray.set_target_fps(60)

deck = Deck(CardFactory())
log("Deck initiated")
# deck.starter_cards()
deck.card_to_cell(2, deck.generate_card(77, 2))
deck.card_to_cell(2, deck.generate_card(88, 2))
deck.card_to_cell(2, deck.generate_card(99, 2))
# deck.card_to_cell(2, deck.generate_card(7, 2))

while not pyray.window_should_close():
    deck.card_selection()
    if pyray.is_key_pressed(pyray.KeyboardKey.KEY_D):
        pass

    pyray.begin_drawing()
    pyray.clear_background(pyray.BLACK)
    pyray.draw_fps(0,0)
    deck.draw_cards()
    pyray.end_drawing()

deck.factory.unload()
pyray.close_window()
