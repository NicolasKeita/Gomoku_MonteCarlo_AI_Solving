
import time
import copy
from srcs.UCT import UCT
import random
from srcs.Tnode import Tnode
from srcs.macros import *
import numpy as np
from srcs.State import State


class MonteCarloTreeSearch:
    def __init__(self, timeout=4.8, size_board=19):
        self.level = None
        self.opponent = None
        random.seed()
        self.timeout = timeout
        self.visit_board = [[0] * size_board for _ in range(size_board)]
        self.score_board = [[0] * size_board for _ in range(size_board)]
        self.root_node = None

    def findNextMove(self, board, player_no):
        self.opponent = 3 - player_no
        self.root_node = Tnode(State(board=board))
#        root_node.state.board = board
        self.root_node.state.player_no = self.opponent
        self.counter = 0

        start = time.time()
        while time.time() - start < self.timeout:
            print("wtf1")
            promising_node = self._select_promising_node(self.root_node)
            #print("promissing node:")
            #promising_node.state.board.print()
            print("wtf2")
            if promising_node.state.board.check_status() == IN_PROGRESS:
                self._expand_node(promising_node)
            node_to_explore = promising_node
            print("wtf3")
            #if self.counter > 2:
                #re.re()
            if len(promising_node.childs) > 0:
                node_to_explore = promising_node.get_random_child_node()
            print("wtf4")
            #print("node_to_explore")
            #node_to_explore.state.board.print()
            my_copy = node_to_explore.copy()
            print("wtf4.3")
            playout_result = self._simulate_random_playout(my_copy)
            print("wtf5")
            self._back_propagation(node_to_explore, playout_result)
            print("wtf6")
            self.counter += 1
        winner_node = self.root_node.get_child_with_max_score()
        return winner_node.state.board

    def _expand_node(self, promising_node):
        print("wtf2.1")
        possible_states = promising_node.state.get_all_possible_states()
        #print("all possibles states")
        #for state in possible_states:
        #    print("state")
        #    state.board.print()
        print("wtf2.2")
        for state in possible_states:
            new_node = Tnode(state)
            new_node.parent = promising_node
            new_node.state.player_no = promising_node.state.get_opponent()
            promising_node.childs.append(new_node)
        return promising_node

    def _select_promising_node(self, root_node):
        node = root_node
        while len(node.childs) != 0:
            node = UCT.find_best_node_with_uct(node)
        return node

    def _simulate_random_playout(self, node_to_explore):
        temp_node = node_to_explore
        board_status = temp_node.state.board.check_status()
        if board_status == self.opponent:
            node_to_explore.parent.state.win_score = -INFINITY
            return board_status
        start2 = time.time()
        i = 0
        #self.counter +=1
        while board_status == IN_PROGRESS:
            #print("Loop number :", i)
            start = time.time()
            temp_node.state.toggle_player()
            temp_node.state.random_play()
            #print("Time to do random play", time.time() - start)
            start3 = time.time()
            board_status = temp_node.state.board.check_status()
            #print("Time to do check_status", time.time() - start3)
            #print("Time to do oneloop", time.time() - start)
            i+=1
        #print("TIME TO finish one simulation", time.time() - start2)
        #print("counter = ", self.counter)
        return board_status

    def _back_propagation(self, node_to_explore, player_no):
        temp_node = node_to_explore
        while temp_node is not None:
            temp_node.state.visit_count += 1
            #self._debug_visit(temp_node)
            if temp_node.state.player_no == player_no:
                #self._debug_score(temp_node)
                temp_node.state.add_score(WIN_SCORE)
            temp_node = temp_node.parent

    def _debug_visit(self, node):
        print("Debug visit")
        last_move = node.state.board.lastest_move
        if not last_move:
            print("main parent!!Cancel")
            return
        self.visit_board[last_move.y][last_move.x] += 1
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

