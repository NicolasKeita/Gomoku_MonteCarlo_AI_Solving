
import time
import copy
from srcs.UCT import UCT
import random
from srcs.Tnode import Tree, Tnode
from srcs.macros import *


class MonteCarloTreeSearch:
    def __init__(self, timeout=4.8, size_board=19):
        self.level = None
        self.opponent = None
        random.seed()
        self.timeout = timeout
        self.visit_board = [[0] * size_board for _ in range(size_board)]
        self.score_board = [[0] * size_board for _ in range(size_board)]
        self.root_node = Tnode()

    def findNextMove(self, board, player_no):
        self.opponent = 3 - player_no
        tree = Tree()
        root_node = tree.root
        root_node.state.board = copy.deepcopy(board)
        root_node.state.player_no = self.opponent
        self.root_node = root_node
        self.counter = 0

        start = time.time()
        while time.time() - start < self.timeout:
            promising_node = self._select_promising_node(root_node)
            if promising_node.state.board.check_status() == IN_PROGRESS:
                self._expand_node(promising_node)
            node_to_explore = promising_node
            if len(promising_node.childs) > 0:
                node_to_explore = promising_node.get_random_child_node()
            my_copy = copy.deepcopy(node_to_explore)
            playout_result = self._simulate_random_playout(my_copy)
            self._back_propagation(node_to_explore, playout_result)
            self.counter += 1
        winner_node = root_node.get_child_with_max_score()
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
        while board_status == IN_PROGRESS:
            temp_node.state.toggle_player()
            temp_node.state.random_play()
            board_status = temp_node.state.board.check_status()
        return board_status

    def _back_propagation(self, node_to_explore, player_no):
        temp_node = node_to_explore
        while temp_node is not None:
            temp_node.state.visit_count += 1
            if temp_node.state.player_no == player_no:
                temp_node.state.add_score(WIN_SCORE)
            temp_node = temp_node.parent

