import time
import copy
import math
import random
from Board import Board
import numpy as np

INFINITY = 99999
IN_PROGRESS = -1
DRAW = 0
P1 = 1
P2 = 2

BLANK = ' '
X_SQUARE = 'X'
O_SQUARE = 'O'


class State:
    def __init__(self, board=None):
        self.board = Board(board) if board is None else board
        self.score = 0
        self.player_no = 0
        self.visit_count = 0
        self.win_score = 0

    def get_all_possible_states(self):
        possible_states = []
        available_positions = self.board.get_empty_positions()
        for pos in available_positions:
            #new_state = State(Board(self.board.board.copy()))
            new_state = State(copy.deepcopy(self.board))
            new_state.player_no = 3 - self.player_no
            new_state.board.perform_move(new_state.player_no, pos)
            possible_states.append(new_state)
        return possible_states

    def get_opponent(self):
        return 3 - self.player_no

    def random_play(self):
        available_positions = self.board.get_empty_positions()
        total_possibilities = len(available_positions)
        r = int(random.random() * total_possibilities)
        self.board.perform_move(self.player_no, available_positions[r])

    def toggle_player(self):
        self.player_no = 3 - self.player_no

    def add_score(self, score_to_add):
        if self.win_score != -INFINITY:
            self.win_score += score_to_add
