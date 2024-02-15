import internal

class CardFactory:
    def __init__(self) -> None:
        self.Clubs_texture = internal.pyray.load_texture(".\\textures\\Clubs.png")
        self.Spades_texture = internal.pyray.load_texture(".\\textures\\Spades.png")
        self.Hearts_texture = internal.pyray.load_texture(".\\textures\\Hearts.png")
        self.Diamonds_texture = internal.pyray.load_texture(".\\textures\\Diamonds.png")
        if self.Diamonds_texture.format == 0 or self.Spades_texture.format == 0 or self.Hearts_texture.format == 0 or self.Clubs_texture.format == 0:
            raise IOError("Failed to load texture")

    def spawn_card(self, suit: internal.Suit, rank: str|int, x: int, y: int) -> internal.Card:
        t = (eval("self.{}_texture".format(suit.name)))

        return internal.Card(suit, rank, x, y, t)