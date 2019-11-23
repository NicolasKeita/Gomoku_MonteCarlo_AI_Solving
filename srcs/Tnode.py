import random


class Tnode:
    def __init__(self, state):
        self.state = state
        self.parent = None
        self.childs = []

    def get_child_with_max_score(self):
        #self._debug_display_all_scores()
        def func(x): return x.state.visit_count
        return max(self.childs, key=func)

    def get_random_child_node(self):
        return random.choice(self.childs)

    def copy(self):
        new_node = Tnode(self.state.copy())
        new_node.parent = self.parent
        new_node.childs = self.childs
        return new_node

    def _debug_display_all_scores(self):
        for child in self.childs:
            print(child.state.win_score, child.state.visit_count, child.state.board.lastest_move.to_string())
