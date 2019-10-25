

import time
import copy
from UCT import UCT
import random
from Tnode import Tree, Tnode

INFINITY = 9999
WIN_SCORE = 10

X_WINS = 2
O_WINS = 1
UNDEFINED = "Undefined"

IN_PROGRESS = -1
DRAW = 0
P1 = 1
P2 = 2
END = 4.8

BLANK = ' '
X_SQUARE = 'X'
O_SQUARE = 'O'


class MonteCarloTreeSearch:
    def __init__(self):
        self.level = None
        self.opponent = None
        random.seed()

    def findNextMove(self, board, player_no):
        self.opponent = 3 - player_no
        tree = Tree()
        root_node = tree.root
        root_node.state.board = copy.deepcopy(board)
        root_node.state.player_no = self.opponent

        immediat_victory_detected = self._detect_immediat_victory(root_node)
        if immediat_victory_detected:
            return immediat_victory_detected

        start = time.time()
        while time.time() - start < END:
            promising_node = self._select_promising_node(root_node)
            if promising_node.state.board.check_status() == IN_PROGRESS:
                self._expand_node(promising_node)
            node_to_explore = promising_node
            if len(promising_node.childs) > 0:
                node_to_explore = promising_node.get_random_child_node()
            playout_result = self._simulate_random_playout(node_to_explore)
            self._back_propagation(node_to_explore, playout_result)
        winner_node = root_node.get_child_with_max_score()
        tree.root = winner_node
        return winner_node.state.board

    def _expand_node(self, promising_node):
        possible_states = promising_node.state.get_all_possible_states()
        for state in possible_states:
            new_node = Tnode(copy.deepcopy(state))
            new_node.parent = promising_node
            new_node.state.player_no = promising_node.state.get_opponent()
            promising_node.childs.append(new_node)

    def _detect_immediat_victory(self, node):
        states = node.state.get_all_possible_states()
        for state in states:
            if state.board.check_status() == O_WINS:
                return state.board

    def _select_promising_node(self, root_node):
        node = root_node
        while len(node.childs) != 0:
            node = UCT.find_best_node_with_uct(node)
        return node

    def _simulate_random_playout(self, node_to_explore):
        temp_node = copy.deepcopy(node_to_explore)
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
                temp_node.state.win_score = WIN_SCORE
            temp_node = temp_node.parent
