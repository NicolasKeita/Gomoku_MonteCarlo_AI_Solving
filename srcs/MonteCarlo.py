import time
from srcs.UCT import UCT
import random
from srcs.Tnode import Tnode
from srcs.macros import *
import numpy as np
from srcs.State import State
from multiprocessing import Process, Pool, Lock, Value, Manager
from concurrent.futures import ThreadPoolExecutor

mutex = Lock()


class MonteCarloTreeSearch:
    def __init__(self, timeout=4.8, size_board=19):
        self.level = None
        self.opponent = None
        random.seed()
        self.timeout = timeout
        self.visit_board = [[0] * size_board for _ in range(size_board)]
        self.score_board = [[0] * size_board for _ in range(size_board)]
        self.root_node = None

    def execute_the_four_steps(self):
        start = time.time()
        #print("Step 1")
        promising_node = self._select_promising_node(self.root_node)
        start_2 = time.time()
        #print("Step 2, time for step 1 was : ", time.time() - start)
        if promising_node.state.board.check_status() == IN_PROGRESS:
            self._expand_node(promising_node)
        node_to_explore = promising_node
        if len(promising_node.childs) > 0:
            node_to_explore = promising_node.get_random_child_node()
        start_3 = time.time()
        #print("Step 3", "time for step 2 was : ", time.time() - start_2)
        my_copy = node_to_explore.copy()
        playout_result = self._simulate_random_playout(my_copy)
        start_4 = time.time()
        #print("Step 4 time for step 3 was : ", time.time() - start_3)
        self._back_propagation(node_to_explore, playout_result)
        #print("End : ", time.time() - start_4)

    def findNextMove(self, board, player_no):
        self.opponent = 3 - player_no
        self.root_node = Tnode(State(board=board))
        self.root_node.state.player_no = self.opponent

        start = time.time()
        while time.time() - start < self.timeout:
            self.execute_the_four_steps()
        winner_node = self.root_node.get_child_with_max_score()
        return winner_node.state.board

    def _expand_node(self, promising_node):
        possible_states = promising_node.state.get_all_possible_states()
        for state in possible_states:
            new_node = Tnode(state)
            new_node.parent = promising_node
            new_node.state.player_no = promising_node.state.get_opponent()
            promising_node.childs.append(new_node)
        return promising_node

    def _select_promising_node(self, root_node):
        depth = 0
        node = root_node
        while len(node.childs) != 0:
            node = UCT.find_best_node_with_uct(node)
            depth += 1
            if depth == 1:
                return node
        return node

    def _simulate_random_playout(self, node_to_explore):
        board_status = node_to_explore.state.board.check_status()
        if board_status == self.opponent:
            node_to_explore.parent.state.win_score = -INFINITY
            return board_status
        while board_status == IN_PROGRESS:
            node_to_explore.state.toggle_player()
            node_to_explore.state.random_play()
            board_status = node_to_explore.state.board.check_status()
        return board_status

    def _back_propagation(self, node_to_explore, player_no):
        temp_node = node_to_explore
        while temp_node is not None:
            temp_node.state.visit_count += 1
            self._debug_visit(temp_node)
            if temp_node.state.player_no == player_no:
                #self._debug_score(temp_node)
                temp_node.state.add_score(WIN_SCORE)
            temp_node = temp_node.parent

    def _debug_visit(self, node):
        last_move = node.state.board.lastest_move
        if not last_move:
            #print("main parent!!Cancel")
            return
        self.visit_board[last_move.y][last_move.x] += 1
        print("Debug visit", last_move.to_string())
        for row in self.visit_board:
            print(row)
        print("\n")

    def _debug_score(self, node):
        print("Debug score")
        last_move = node.state.board.lastest_move
        if not last_move:
            return
        self.score_board[last_move.y][last_move.x] += WIN_SCORE
        for row in self.score_board:
            print(row)
        print("\n")
