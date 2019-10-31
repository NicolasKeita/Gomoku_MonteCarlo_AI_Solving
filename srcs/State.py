import copy
import random
from srcs.Board import Board
from srcs.macros import *
import numpy as np
import time


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
        #print("The board:")
        #self.board.print()
        #print("all empty pos ")
        #for pos in self.board.empty_pos:
        #    print("y = ", pos.y, "x = ", pos.x)
        #print("le board avant")
        #self.board.print()
        i = 0
        start_3 = time.time()
        for pos in self.board.empty_pos:
            start_2 = time.time()
            #new_state = State(Board(self.board.board.copy()))

            #new_state = State(board=self.board, copy=True)
            new_state = self.copy()
#            if i > 2:
#                re.re()
            #new_state = State(copy.deepcopy(self.board))
            #print("Temps pour copy : ", time.time() - start_2)
            new_state.player_no = 3 - self.player_no
            start = time.time()
            new_state.board.perform_move(new_state.player_no, pos)
            #print("temps pour perform move", time.time() - start)
            possible_states.append(new_state)
            #print("temps pour loop_all_posible_states", time.time() - start_2, " I = ", i, "size empty pos : ", len(self.board.empty_pos))
            i += 1
        print("Temps pour recup all possible states : ", time.time() - start_3)
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
