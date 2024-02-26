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
        self.selected_card = False
        self.last_ct = (0, 0)


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
    
    def all_cards(self) -> list[internal.Card]:
        all = []
        for d in self.cells:
            all += self.cells[d]
        
        return all

    def identify_card(self) -> None:
        rel_cards = []
        for card in self.all_cards():
            if internal.pyray.check_collision_point_rec(internal.pyray.get_mouse_position(), card.rectangle):
                rel_cards.append(card)
        try:
            self.last_ct = (rel_cards[-1].x, rel_cards[-1].y)
            self.selected_card = rel_cards[-1]
        except IndexError:
            pass

    def reset_selected_card(self) -> None:
        try:
            self.selected_card.x, self.selected_card.y = self.last_ct
        except AttributeError:
            pass
        self.selected_card = False
    
    def selected_card_follow_mouse(self) -> None:
        if self.selected_card != False:
            self.selected_card.x = internal.pyray.get_mouse_x() - 30
            self.selected_card.y = internal.pyray.get_mouse_y() - 30

    def card_selection(self) -> None:
        if internal.pyray.is_mouse_button_pressed(internal.pyray.MouseButton.MOUSE_BUTTON_LEFT):
            self.identify_card()
    
        # if internal.pyray.is_mouse_button_down(internal.pyray.MouseButton.MOUSE_BUTTON_RIGHT):
        #     self.reset_selected_card()

        if internal.pyray.is_mouse_button_released(internal.pyray.MouseButton.MOUSE_BUTTON_LEFT):
            self.reset_selected_card()
    
        self.selected_card_follow_mouse()