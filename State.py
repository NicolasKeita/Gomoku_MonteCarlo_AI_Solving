import time
import copy
import math
import random
from Board import Board

INFINITY = 9999
WIN_SCORE = 10

MAP_SIZE = 3
IN_PROGRESS = -1
DRAW = 0
P1 = 1
P2 = 2
END = 4.5

BLANK = ' '
X_SQUARE = 'X'
O_SQUARE = 'O'


class State:
    def __init__(self, board=None):
        self.board = Board() if board is None else copy.deepcopy(board)
        self.score = None
        self.player_no = None
        self.visit_count = 0
        self.win_score = 0

    def get_all_possible_states(self):
        possible_states = []
        available_positions = self.board.get_empty_positions()
        for pos in available_positions:
            new_state = State(Board(copy.deepcopy(self.board.board)))
            new_state.player_no = 3 - self.player_no
            new_state.board.perform_move(new_state.player_no, pos)
            possible_states.append(new_state)
        return possible_states

    def get_opponent(self):
        return 3 - self.player_no

    def random_play(self):
        available_positions = self.board.get_empty_positions()
        total_possibilities = len(available_positions)
        random.seed()
        r = int(random.random() * total_possibilities)
        self.board.perform_move(self.player_no, available_positions[r])

    def toggle_player(self):
        self.player_no = MAP_SIZE - self.player_no
