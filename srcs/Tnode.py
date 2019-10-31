import random


class Tnode:
    def __init__(self, state):
        self.state = state
        self.parent = None
        self.childs = []

    def get_child_with_max_score(self):
        #print("Child with high score")
        #for child in self.childs:
            #print(child.state.visit_count)
        def func(x): return x.state.visit_count
        return max(self.childs, key=func)

    def get_random_child_node(self):
        # Game specific choice. Hum, not so random after all?
        print("who is the parant")
        self.state.board.print()
        return random.choice(self.childs)
        while True:
            c = random.choice(self.childs)
            if c.state.board.is_there_coin_around_last_move():
                return c

    def copy(self):
        new_node = Tnode(self.state.copy())
        new_node.parent = self.parent
        new_node.childs = self.childs
        return new_node
