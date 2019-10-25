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


class Tree:
    def __init__(self):
        self.root = Tnode()


class Tnode:
    def __init__(self, state=None):
        self.state = State() if state is None else copy.deepcopy(state)
        self.parent = None
        self.childs = []

    def get_child_with_max_score(self):
        func = lambda x: x.state.visit_count
        return max(self.childs, key=func)

    def get_random_child_node(self):
        possible_moves_count = len(self.childs)
        r = int(random.random() * possible_moves_count)
        return self.childs[r]
