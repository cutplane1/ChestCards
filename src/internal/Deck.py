from typing import Dict, List
import internal


class Deck:
    def __init__(self, factory: internal.CardFactory) -> None:
        self.factory = factory
        self.cells: Dict[int, List[internal.Card]] = {}
        self.i = 0
        self.last_cell = 1
        self.y_offset = 300
        self.score = 0
        self.selected_cards: List[internal.Card] = []
        self.last_ct = internal.pyray.Vector2(0, 0)
        self.now_ct = internal.pyray.Vector2(0, 0)
        self.n_cell = 0

        for i in range(1, 9 + 1):
            self.cells[i] = []

    def card_to_cell(self, cell: int, sp: internal.Card) -> None:
        if cell != self.last_cell:
            self.last_cell = cell
            self.i = 0
        try:
            self.i = len(self.cells[cell]) * 30
        except KeyError:
            self.i = 0
        try:
            sp.x = 70 * cell
            sp.y = self.i + self.y_offset
            sp.cell_temp = cell
            self.cells[cell].append(sp)
        except KeyError:
            self.cells[cell] = [sp]

    def generate_card(self, rank, cell) -> internal.Card:
        return self.factory.spawn_card(
            internal.Suit.random(), rank, 70 * cell, self.i + self.y_offset
        )

    def find_cell_by_rank(self, rank: str | int) -> int | None:
        for cell_id in self.cells:
            for card in self.cells[cell_id]:
                if card.rank == str(rank):
                    return cell_id
        return None

    def starter_cards(self) -> None:
        import random

        # rework this
        for _ in range(7):
            rand_rank = random.choice(list(range(1, 9 + 1)))
            for _ in range(0, random.randint(0, 2 + 1)):
                self.card_to_cell(rand_rank, self.generate_card(rand_rank, rand_rank))

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

    def get_free_cells(self) -> list[int]:
        a = []
        for cell_id in range(1, 9 + 1):
            try:
                if self.cells[cell_id] == [] or self.cells[cell_id] == None:
                    a.append(cell_id)
            except KeyError:
                a.append(cell_id)
        return a

    def all_cards(self) -> list[internal.Card]:
        all = []
        for d in self.cells:
            all += self.cells[d]

        return all

    def identify_card(self) -> None:
        rel_cards = []
        for card in self.all_cards():
            if internal.pyray.check_collision_point_rec(
                internal.pyray.get_mouse_position(), card.rectangle
            ):
                rel_cards.append(card)
        try:
            base_card = rel_cards[-1]
            base_card_id = self.cells[base_card.cell_temp].index(base_card)
            self.last_ct.x, self.last_ct.y = base_card.x, base_card.y
            self.selected_cards = self.cells[base_card.cell_temp][base_card_id:]
            for card in self.selected_cards:
                card.ct_temp.x, card.ct_temp.y = card.x, card.y
        except IndexError:
            pass

    def reset_selected_card(self) -> None:
        try:
            self.now_ct = self.last_ct
        except AttributeError:
            pass
        self.selected_cards = []

    def selected_card_follow_mouse(self) -> None:
        pass

    def card_selection(self) -> None:
        cell = self.find_cell_by_ct(internal.pyray.get_mouse_position())

        if internal.pyray.is_mouse_button_pressed(
            internal.pyray.MouseButton.MOUSE_BUTTON_LEFT
        ):
            self.n_cell = cell
            self.identify_card()

        if internal.pyray.is_mouse_button_released(
            internal.pyray.MouseButton.MOUSE_BUTTON_LEFT
        ):
            if self.selected_cards != False:
                sc = self.selected_cards
                for card in sc:
                    if self.n_cell != cell:
                        self.cells[card.cell_temp].remove(card)
                        self.reset_selected_card()
                        self.card_to_cell(cell, card)
                    else:
                        self.reset_selected_card()
                        card.x, card.y = int(card.ct_temp.x), int(card.ct_temp.y)

        if self.selected_cards != False:
            self.now_ct.x = internal.pyray.get_mouse_x() - 30
            self.now_ct.y = internal.pyray.get_mouse_y() - 30
            for card_id, card in enumerate(self.selected_cards):
                card.x = int(self.now_ct.x)
                card.y = int(self.now_ct.y) + card_id * 30

    def find_cell_by_ct(self, ct_v: internal.pyray.Vector2) -> int:
        return int(round(ct_v.x / 70))
