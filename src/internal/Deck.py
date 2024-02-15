import internal
import random

class Deck:
    def __init__(self, factory: internal.CardFactory) -> None:
        self.factory = factory
        self.cells = {}
        self.i = 0
        self.last_cell = 1

    def in_this_cell(cell: int, card: internal.Card) -> None:
        pass

    def spawn_card_to_cell(self, cell: int, rank: str) -> None:
        if cell != self.last_cell:
            self.i = 0
            self.last_cell = cell
        self.i = self.i + 30
        sp = self.factory.spawn_card(internal.Suit.random(), rank, 70 * cell, self.i + 400)
        try:
            self.cells[cell].append(sp)
        except KeyError:
            self.cells[cell] = [sp]
    
    def multi_debug_input(self, cell: int, t: int) -> None:
        for _ in range(0, t):
            self.spawn_card_to_cell(cell, "4") # debug number

    def get_card(self) -> None:
        pass

    def find_cell_by_rank(self, rank: str) -> int|None:
        for cell_id in self.cells:
            for card in self.cells[cell_id]:
                if card.rank == rank:
                    return cell_id
                else:
                    end = True
        if end:
            return None
        
    def init_game(self):
        for d in range(7):
            rand_rank = random.choice(list(range(1, 9 + 1)))
            for i in range(0, random.randint(0, 2)):
                self.spawn_card_to_cell(rand_rank, str(rand_rank))


    def draw_cards(self):
        for d in self.cells:
            for card in self.cells[d]:
                card.draw()