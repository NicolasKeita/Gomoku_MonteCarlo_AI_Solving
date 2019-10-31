import numpy as np
from srcs.macros import INFINITY


class UCT:
    @staticmethod
    def uct_value(total_visit, node_win_score, node_visit):
        if node_visit == 0:
            return INFINITY
        return ((node_win_score / node_visit) +
                1.41 * np.sqrt(np.log(total_visit) / node_visit))

    @staticmethod
    def find_best_node_with_uct(node):
        parent_visit = node.state.visit_count
        """
        for child in node.childs:
            print("pos :", child.state.board.lastest_move.to_string(), "visit count : ", child.state.visit_count)
        """


        def func(x): return UCT.uct_value(parent_visit,
                                          x.state.win_score,
                                          x.state.visit_count)

        return max(node.childs, key=func)
