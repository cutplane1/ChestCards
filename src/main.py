from pyray import *

from internal import Suit 

init_window(800, 600, 'demo')

set_target_fps(60)

class draw:
    def __enter__(self) -> None:
        begin_drawing()
    
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        end_drawing()

class Card:
    def __init__(self, suit: Suit, rank: str, x: int, y: int, texture: Texture) -> None:
        self.suit = suit
        self.rank = rank
        self.x = x
        self.y = y
        self.texture = texture
        
        if suit.name == "Clubs" or suit.name == "Spades":
            self.color = BLACK
        elif suit.name == "Hearts" or suit.name == "Diamonds":
            self.color = RED

    def draw(self) -> None:
        draw_rectangle(self.x, self.y, 50, 70, WHITE)
        draw_text(self.rank, self.x + 2, self.y + 2, 20, self.color)
        draw_texture(self.texture, self.x + 30, self.y + 50, WHITE)

class CardFactory:
    def __init__(self) -> None:
        self.Clubs_texture = load_texture(".\\textures\\Clubs.png")
        self.Spades_texture = load_texture(".\\textures\\Spades.png")
        self.Hearts_texture = load_texture(".\\textures\\Hearts.png")
        self.Diamonds_texture = load_texture(".\\textures\\Diamonds.png")

    def spawn_card(self, suit: Suit, rank: str, x: int, y: int) -> Card:
        t = (eval("self.{}_texture".format(suit.name)))

        return Card(suit, rank, x, y, t)


class Deck:
    def __init__(self, factory: CardFactory) -> None:
        self.factory = factory
        self.cells = {}
        self.i = 0
        self.last_cell = 1
    
    def place_card(card: Card) -> None:
        pass

    def in_this_cell(cell: int, card: Card) -> None:
        # factory.spawn_card()
        pass

    def debug_input(self, cell: int):
        if cell != self.last_cell:
            self.i = 0
            self.last_cell = cell
        self.i = self.i + 30
        try:
            self.cells[cell].append(self.factory.spawn_card(Suit.random(), "69", 70 * cell, self.i + 400))
        except KeyError:
            self.cells[cell] = [self.factory.spawn_card(Suit.random(), "69", 70 * cell, self.i + 400)]
    
    def multi_debug_input(self, cell: int, t: int):
        for _ in range(0, t):
            self.debug_input(cell)


factory = CardFactory()

deck = Deck(factory)
deck.multi_debug_input(1, 4)
deck.multi_debug_input(2, 4)
deck.multi_debug_input(3, 4)
deck.multi_debug_input(4, 4)
deck.multi_debug_input(5, 4)
deck.multi_debug_input(6, 4)
deck.multi_debug_input(7, 4)
deck.multi_debug_input(8, 4)
deck.multi_debug_input(9, 4)


while not window_should_close():

    with draw():
        clear_background(BLACK)
        draw_fps(0,0)
        for d in deck.cells:
            for card in deck.cells[d]:
                card.draw()

close_window()
