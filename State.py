import random
from srcs.Board import Board
from srcs.macros import *
import numpy as np


class State:
    def __init__(self, board):
        self.board = board
        self.score = 0
        self.player_no = 0
        self.visit_count = 0
        self.win_score = 0

    def copy(self):
        new_state = State(Board(self.board.board, copy=True, empty_pos=self.board.empty_pos))
        new_state.win_score = self.win_score
        new_state.visit_count = self.visit_count
        new_state.player_no = self.player_no
        new_state.score = self.score
        return new_state

    def get_all_possible_states(self):
        possible_states = []
        for pos in self.board.empty_pos:
            new_state = self.copy()
            new_state.player_no = 3 - self.player_no
            new_state.board.perform_move(new_state.player_no, pos)
            possible_states.append(new_state)
        return np.array(possible_states)

    def get_opponent(self):
        return 3 - self.player_no

    def random_play(self):
        self.board.perform_move(self.player_no,
                                random.choice(self.board.empty_pos))

    def toggle_player(self):
        self.player_no = 3 - self.player_no

    def add_score(self, score_to_add):
        if self.win_score != -INFINITY:
            self.win_score += score_to_add
