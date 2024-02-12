from pyray import *
from raylib import colors
from internal import Suit 

init_window(800, 600, 'demo')

set_target_fps(60)

class draw:
    def __enter__(self) -> None:
        begin_drawing()
    
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        end_drawing()

class Card:
    def __init__(self, suit: Suit, rank: int, x: int, y: int, texture: Texture) -> None:
        self.suit = suit
        self.rank = str(rank)
        self.x = x
        self.y = y
        self.texture = texture
        
        if suit.name == "Clubs" or suit.name == "Spades":
            self.color = colors.BLACK
        elif suit.name == "Hearts" or suit.name == "Diamonds":
            self.color = colors.RED

    def draw(self) -> None:
        draw_rectangle(self.x, self.y, 50, 70, WHITE)
        draw_text(self.rank, self.x + 2, self.y + 2, 20, self.color)
        draw_texture(self.texture, self.x + 30, self.y + 50, colors.WHITE)

class CardFactory:
    def __init__(self) -> None:
        self.Clubs_texture = load_texture(".\\textures\\Clubs.png")
        self.Spades_texture = load_texture(".\\textures\\Spades.png")
        self.Hearts_texture = load_texture(".\\textures\\Hearts.png")
        self.Diamonds_texture = load_texture(".\\textures\\Diamonds.png")

    def spawn_card(self, suit: Suit, rank: int, x: int, y: int) -> Card:
        t = (eval("self.{}_texture".format(suit.name)))

        return Card(suit, rank, x, y, t)


class Deck:
    def __init__(self, factory: CardFactory) -> None:
        self.factory = factory
        self.cells = {}
    
    def place_card(card: Card) -> None:
        pass

    def in_this_cell(cell: int, card: Card) -> None:
        # factory.spawn_card()
        pass

    def debug_init(self, cell: int):
        try:
            self.cells[cell].append(self.factory.spawn_card(Suit.random(), 7, 100, 100))
        except KeyError:
            self.cells[cell] = [self.factory.spawn_card(Suit.random(), 7, 100, 100)]





# card spawn
# cards = []
factory = CardFactory()

deck = Deck(factory)
deck.debug_init(1)
deck.debug_init(1)
deck.debug_init(1)
# try:
#     print(deck.cells[1])
# except KeyError:
#     deck.cells[1] = []

print(deck.cells)


# deck.in_this_cell(1, factory.spawn_card(random.choice(list(Suit)), i, i * 10 * 6 + 50, 500)))

# for i in range(2, 9 + 1):
    # cards.append(factory.spawn_card(random.choice(list(Suit)), i, i * 10 * 6 + 50, 500))

while not window_should_close():

    with draw():
        clear_background(BLACK)

        # draw_rectangle(100, 10, 600, 100, colors.BROWN)
        draw_text("enemy side", 0, 0, 24, colors.WHITE)
        for d in deck.cells:
            for i in deck.cells[d]:
                i.draw()



        # draw_circle(500, 300, 60, GRAY)
        # draw_text("card pack", 460, 290, 16, colors.WHITE)
        
        # for c in cards:
        #     c.draw()

close_window()
