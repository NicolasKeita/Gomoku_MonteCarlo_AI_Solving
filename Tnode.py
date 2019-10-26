import random
from State import State


class Tree:
    def __init__(self):
        self.root = Tnode()


class Tnode:
    def __init__(self, state=None):
        self.state = State() if state is None else state
        self.parent = None
        self.childs = []

    def get_child_with_max_score(self):
        func = lambda x: x.state.visit_count
        return max(self.childs, key=func)

    def get_random_child_node(self):
        possible_moves_count = len(self.childs)
        r = int(random.random() * possible_moves_count)
        return self.childs[r]
