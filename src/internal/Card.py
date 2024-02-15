import internal

class Card:
    def __init__(self, suit: internal.Suit, rank: str, x: int, y: int, texture: internal.pyray.Texture) -> None:
        self.suit = suit
        self.rank = rank
        self.x = x
        self.y = y
        self.texture = texture
        
        if suit.name == "Clubs" or suit.name == "Spades":
            self.color = internal.pyray.BLACK
        elif suit.name == "Hearts" or suit.name == "Diamonds":
            self.color = internal.pyray.RED

    def draw(self) -> None:
        internal.pyray.draw_rectangle(self.x, self.y, 50, 70, internal.pyray.WHITE)
        internal.pyray.draw_text(self.rank, self.x + 2, self.y + 2, 20, self.color)
        internal.pyray.draw_texture(self.texture, self.x + 30, self.y + 50, internal.pyray.WHITE)