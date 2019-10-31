import random
from srcs.State import State
from copy import deepcopy


class Tnode:
    def __init__(self, state):
        self.state = state
        self.parent = None
        self.childs = []

    def get_child_with_max_score(self):
        func = lambda x: x.state.visit_count
        return max(self.childs, key=func)

    def get_random_child_node(self):
        return random.choice(self.childs)

    def copy(self):
        #new_node = Tnode(deepcopy(self.state))
        new_node = Tnode(self.state.copy())
        new_node.parent = self.parent
        new_node.childs = self.childs
        return new_node
