import unittest
from srcs.UCT import UCT
from srcs.Tnode import Tree
from srcs.Board import Board, Position
from srcs.MonteCarlo import MonteCarloTreeSearch
from srcs.macros import *
import numpy as np


class TestMonteCarlo(unittest.TestCase):
    def test_uct_value(self):
        uct_value = 15.79
        self.assertAlmostEqual(UCT.uct_value(600, 300, 20), uct_value, delta=0.01)

    def test_all_possibles_states(self):
        t = Tree()
        initState = t.root.state
        possibleStates = initState.get_all_possible_states()
        self.assertTrue(len(possibleStates) > 0)

    def test_perform_move(self):
        board = Board()
        init_available_positions = len(board.get_empty_positions())
        board.perform_move(1, Position(1, 1))
        available_positions = len(board.get_empty_positions())
        self.assertTrue(init_available_positions > available_positions)

    def test_diago(self):
        b = Board(np.array([
            [O_SQUARE, X_SQUARE, BLANK, BLANK, BLANK],
            [BLANK, O_SQUARE, X_SQUARE, BLANK, BLANK],
            [BLANK, BLANK, O_SQUARE, X_SQUARE, BLANK],
            [X_SQUARE, BLANK, BLANK, O_SQUARE, BLANK],
            [BLANK, BLANK, BLANK, BLANK, O_SQUARE],
        ]))
        result = b.test_diagonals()
        self.assertTrue(result == b.P1)

    def test_find_next_move_one_shoot_5_1(self):
        mcts = MonteCarloTreeSearch(timeout=4.8, size_board=5)
        board = Board(size=5)
        board.board = [
            [O_SQUARE, X_SQUARE, BLANK, BLANK, BLANK],
            [BLANK, O_SQUARE, X_SQUARE, BLANK, BLANK],
            [BLANK, BLANK, O_SQUARE, X_SQUARE, BLANK],
            [X_SQUARE, BLANK, BLANK, O_SQUARE, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK],
        ]
        expected = [
            [O_SQUARE, X_SQUARE, BLANK, BLANK, BLANK],
            [BLANK, O_SQUARE, X_SQUARE, BLANK, BLANK],
            [BLANK, BLANK, O_SQUARE, X_SQUARE, BLANK],
            [X_SQUARE, BLANK, BLANK, O_SQUARE, BLANK],
            [BLANK, BLANK, BLANK, BLANK, O_SQUARE],
        ]
        board = mcts.findNextMove(board, board.P1)
        print("Final board : ")
        board.print()
        self.assertTrue(board.board == expected)


    def test_find_next_move_one_shoot_5(self):
        mcts = MonteCarloTreeSearch(timeout=4.8, size_board=5)
        board = Board(size=5)
        board.board = [
            [X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK],
            [X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK],
            [X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK],
            [X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK],
        ]
        expected = [
            [X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK],
            [X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK],
            [X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK],
            [X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK],
            [BLANK, O_SQUARE, BLANK, BLANK, BLANK],
        ]
        board = mcts.findNextMove(board, board.P1)
        print("Final board : ")
        board.print()
        self.assertTrue(board.board == expected)

    def test_find_next_move_one_shoot(self):
        mcts = MonteCarloTreeSearch(timeout=30, size_board=7)
        board_2 = Board(size=7)
        board_2.board = [
            [X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK, BLANK, BLANK],
            [X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK, BLANK, BLANK],
            [X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK, BLANK, BLANK],
            [X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
        ]
        expected = [
            [X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK, BLANK, BLANK],
            [X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK, BLANK, BLANK],
            [X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK, BLANK, BLANK],
            [X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, O_SQUARE, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
        ]
        board = mcts.findNextMove(board_2, board_2.P1)

        print("Final board : ")
        board.print()

        self.assertTrue(board.board == expected)

    def test_find_next_move_one_shoot_7_2(self):
        mcts = MonteCarloTreeSearch(timeout=30, size_board=7)
        board_2 = Board(size=7)
        board_2.board = [
            [X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK, BLANK, BLANK],
            [X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK, BLANK, BLANK],
            [X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK, BLANK, BLANK],
            [X_SQUARE, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, O_SQUARE, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
        ]
        expected = [
            [X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK, BLANK, BLANK],
            [X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK, BLANK, BLANK],
            [X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK, BLANK, BLANK],
            [X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, O_SQUARE, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
        ]
        board = mcts.findNextMove(board_2, board_2.P1)

        print("Final board : ")
        board.print()

        self.assertTrue(board.board == expected)


    def test_find_next_move_one_shoot_7_3(self):
        return
        mcts = MonteCarloTreeSearch(timeout=1800, size_board=19)
        board_2 = Board(size=19)
        board_2.board = [
            [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, O_SQUARE, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, O_SQUARE, O_SQUARE, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, O_SQUARE, X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, X_SQUARE, X_SQUARE, X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, O_SQUARE, X_SQUARE, X_SQUARE, X_SQUARE, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
        ]

        expected = [
            [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, O_SQUARE, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, O_SQUARE, O_SQUARE, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, O_SQUARE, X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, X_SQUARE, X_SQUARE, X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, O_SQUARE, X_SQUARE, X_SQUARE, X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
        ]
        board = mcts.findNextMove(board_2, board_2.P1)

        print("Final board : ")
        board.print()

        self.assertTrue(board.board == expected)


    def test_find_next_move(self):
        return
        board = Board(size=19)
        player = board.P1
        mcts = MonteCarloTreeSearch(timeout=4.8)
        total_move = board.size * board.size
        for i in range(total_move):
            print("i = ", i)
            board.print()
            board = mcts.findNextMove(board, player)
            if board.check_status() != -1:
                break
            player = 3 - player
        win_status = board.check_status()
        board.print()
        self.assertTrue(win_status == board.DRAW)


if __name__ == '__main__':
    unittest.main()