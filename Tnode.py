import time
import copy
import math
import random
from Board import Board
from State import State
from UCT import UCT

INFINITY = 9999
WIN_SCORE = 10

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

    def findNextMove(self, board, player_no):
        self.opponent = 3 - player_no
        tree = Tree()
        root_node = tree.root
        root_node.state.board = copy.deepcopy(board)
        root_node.state.player_no = self.opponent

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


class Tree:
    def __init__(self):
        self.root = Tnode()


class Tnode:
    def __init__(self, state=None):
        self.state = State() if state is None else copy.deepcopy(state)
        self.parent = None
        self.childs = []

    def get_child_with_max_score(self):
        """
        print("affichage child scores")
        for child in self.childs:
            print(child.state.visit_count)
            print("Affichage board")
            print(child.state.board.print())
        """
        func = lambda x: x.state.visit_count
        return max(self.childs, key=func)
        """
        if len(self.childs) == 0:
            return self
        highest = (self.childs[0].state.win_score, 0)
        for i in range(len(self.childs)):
            if self.childs[i].state.win_score > highest[0]:
                highest = (self.childs[i].state.win_score, i)
        return self.childs[highest[1]]
        """

    def get_random_child_node(self):
        possible_moves_count = len(self.childs)
        random.seed()
        return self.childs[int(random.random() * possible_moves_count)]
