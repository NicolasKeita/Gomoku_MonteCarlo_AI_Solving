import random
import time

from srcs.State import State
from srcs.Tnode import Tnode
from srcs.UCT import UCT
from srcs.macros import *


class MonteCarloTreeSearch:
    def __init__(self, timeout=8, size_board=19):
        self.level = None
        self.opponent = None
        random.seed()
        self.timeout = timeout
        self.visit_board = [[0] * size_board for _ in range(size_board)]
        self.score_board = [[0] * size_board for _ in range(size_board)]
        self.root_node = None

    def execute_the_four_steps(self):
        promising_node = self._select_promising_node(self.root_node)
        if promising_node.state.board.check_status() == IN_PROGRESS:
            self._expand_node(promising_node)
        node_to_explore = promising_node
        if len(promising_node.childs) > 0:
            node_to_explore = promising_node.get_random_child_node()
        playout_result = self._simulate_random_playout(node_to_explore)
        self._back_propagation(node_to_explore, playout_result)

    def findNextMove(self, board, player_no):
        self.opponent = 3 - player_no
        self.root_node = Tnode(State(board=board))
        self.root_node.state.player_no = self.opponent

        #import time
        #import sys
        #start_2 = time.time()

        start = time.time()
        while time.time() - start < self.timeout:
            self.execute_the_four_steps()
        winner_node = self.root_node.get_child_with_max_score()

        #print("Temps pour resoudre : ", time.time() - start_2, file=sys.stderr)

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
        depth = 0
        node = root_node
        while len(node.childs) != 0:
            node = UCT.find_best_node_with_uct(node)
            depth += 1
            #if depth == 1:
            #    return node
        return node

    def _simulate_random_playout(self, node_to_explore):
        board_status = node_to_explore.state.board.check_status()

        # if board_status != -1:
            # print("Board display !!!!!!!!")
            # node_to_explore.state.board.print()
            # print("Board_status : ", board_status, "L opponent : ", self.opponent)

        if board_status == self.opponent:
            for child in self.root_node.childs:
                if child.state.board.lastest_move == node_to_explore.state.board.lastest_move:
                    child.state.add_score(WIN_SCORE * 10)
                    child.state.visit_count += 1
                    break
            return board_status
        elif board_status == 3 - self.opponent:
            for child in self.root_node.childs:
                if child.state.board.lastest_move == node_to_explore.state.board.lastest_move:
                    child.state.add_score(WIN_SCORE * 100)
                    child.state.visit_count += 1
                    break
            return board_status
        node_being_simulated = node_to_explore.copy()
        while board_status == IN_PROGRESS:
            node_being_simulated.state.toggle_player()
            node_being_simulated.state.random_play()
            board_status = node_being_simulated.state.board.check_status()
        return board_status

    def _back_propagation(self, node_to_explore, player_no):
        temp_node = node_to_explore
        while temp_node is not None:
            temp_node.state.visit_count += 1
            # self._debug_visit(temp_node)
            # print("player_no_temp_node : ", temp_node.state.player_no, " player no : ", player_no)
            if temp_node.state.player_no == player_no:
                # self._debug_score(temp_node)
                temp_node.state.add_score(WIN_SCORE)
            temp_node = temp_node.parent

    def _debug_visit(self, node):
        last_move = node.state.board.lastest_move
        if not last_move:
            # print("main parent!!Cancel")
            return
        self.visit_board[last_move.y][last_move.x] += 1
        print("Debug visit. Last move : ", last_move.to_string())
        for row in self.visit_board:
            print(row)
        print("\n")

    def _debug_score(self, node):
        print("Debug score. Last move : ", node.state.board.last_move.to_string())
        last_move = node.state.board.lastest_move
        if not last_move:
            return
        self.score_board[last_move.y][last_move.x] += WIN_SCORE
        for row in self.score_board:
            print(row)
        print("\n")
