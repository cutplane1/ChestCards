import internal
import random

class Deck:
    def __init__(self, factory: internal.CardFactory) -> None:
        self.factory = factory
        self.cells = {}
        self.i = 0
        self.last_cell = 1
        self.y_offset = 400
        self.score = 0


    def spawn_card_to_cell(self, cell: int, rank: str|int) -> None:
        if cell != self.last_cell:
            self.last_cell = cell
            self.i = 0
        try:
            self.i = len(self.cells[cell]) * 30
        except KeyError:
            self.i = 0

        sp = self.factory.spawn_card(internal.Suit.random(), rank, 70 * cell, self.i + 400)
        try:
            self.cells[cell].append(sp)
        except KeyError:
            self.cells[cell] = [sp]


    def find_cell_by_rank(self, rank: str|int) -> int|None:
        for cell_id in self.cells:
            for card in self.cells[cell_id]:
                if card.rank == str(rank):
                    return cell_id
                else:
                    end = False
        if end:
            return None
        
    def init_game(self) -> None:
        # rework this
        for _ in range(7):
            rand_rank = random.choice(list(range(1, 9 + 1)))
            for _ in range(0, random.randint(0, 2 + 1)):
                self.spawn_card_to_cell(rand_rank, rand_rank)


    def draw_cards(self) -> None:
        for d in self.cells:
            for card in self.cells[d]:
                card.draw()

    def is_card_pack_completed(self) -> None:
        for cell_id in self.cells:
            if len(self.cells[cell_id]) >= 4:
                self.i = 0
                self.cells[cell_id] = []
                self.score += 1

    def take_one_random_card(self) -> None:
        rand_rank = random.randint(1, 9)
        cell = self.find_cell_by_rank(rand_rank)
        if cell == None:
            cell = random.choice(self.get_free_cells())
        self.spawn_card_to_cell(cell, rand_rank)

    def get_free_cells(self) -> list[int]:
        a = []
        for cell_id in range(1, 9 + 1):
            try:
                if self.cells[cell_id] == [] or self.cells[cell_id] == None:
                    a.append(cell_id)
            except KeyError:
                a.append(cell_id)
        return a

