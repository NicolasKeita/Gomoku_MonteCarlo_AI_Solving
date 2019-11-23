import unittest
from srcs.Board import Board
from srcs.MonteCarlo import MonteCarloTreeSearch
from srcs.macros import *
import numpy as np
from copy import deepcopy


class TestMonteCarlo_board_5(unittest.TestCase):
    def test_find_next_move_one_shoot_5_1(self):
        mcts = MonteCarloTreeSearch(timeout=3, size_board=5)
        board = Board(np.array([
            [O_SQUARE, X_SQUARE, BLANK, BLANK, BLANK],
            [BLANK, O_SQUARE, X_SQUARE, BLANK, BLANK],
            [BLANK, BLANK, O_SQUARE, X_SQUARE, BLANK],
            [X_SQUARE, BLANK, BLANK, O_SQUARE, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK],
        ]))
        expected = np.array([
            [O_SQUARE, X_SQUARE, BLANK, BLANK, BLANK],
            [BLANK, O_SQUARE, X_SQUARE, BLANK, BLANK],
            [BLANK, BLANK, O_SQUARE, X_SQUARE, BLANK],
            [X_SQUARE, BLANK, BLANK, O_SQUARE, BLANK],
            [BLANK, BLANK, BLANK, BLANK, O_SQUARE],
        ])
        board = mcts.findNextMove(board, board.P1)
        #print("Final board : ")
        #board.print()
        self.assertTrue(np.array_equal(board.board, expected))

    def test_find_next_move_one_shoot_5_2(self):
        mcts = MonteCarloTreeSearch(timeout=4.3, size_board=5)
        board = Board(np.array([
            [O_SQUARE, O_SQUARE, BLANK, BLANK, BLANK],
            [BLANK, X_SQUARE, X_SQUARE, BLANK, BLANK],
            [BLANK, BLANK, X_SQUARE, X_SQUARE, X_SQUARE],
            [X_SQUARE, BLANK, BLANK, O_SQUARE, BLANK],
            [O_SQUARE, O_SQUARE, O_SQUARE, O_SQUARE, BLANK],
        ]))
        expected = np.array([
            [O_SQUARE, O_SQUARE, BLANK, BLANK, BLANK],
            [BLANK, X_SQUARE, X_SQUARE, BLANK, BLANK],
            [BLANK, BLANK, X_SQUARE, X_SQUARE, X_SQUARE],
            [X_SQUARE, BLANK, BLANK, O_SQUARE, BLANK],
            [O_SQUARE, O_SQUARE, O_SQUARE, O_SQUARE, O_SQUARE],
        ])
        board = mcts.findNextMove(board, board.P1)
        #print("Final board : ")
        #board.print()
        self.assertTrue(np.array_equal(board.board, expected))

    def test_find_next_move_one_shoot_5(self):
        mcts = MonteCarloTreeSearch(timeout=4.3, size_board=5)
        board = Board(two_dim_board=np.array([
            [X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK],
            [X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK],
            [X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK],
            [X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK],
        ]))
        expected = np.array([
            [X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK],
            [X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK],
            [X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK],
            [X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK],
            [BLANK, O_SQUARE, BLANK, BLANK, BLANK],
        ])
        board = mcts.findNextMove(board, board.P1)
        #print("Final board : ")
        #board.print()
        self.assertTrue(np.array_equal(board.board, expected))

    def test_find_next_move_one_shoot_5_3(self):
        # Defense
        mcts = MonteCarloTreeSearch(timeout=4.3, size_board=5)
        board = Board(two_dim_board=np.array([
            [X, O, B, B, B],
            [X, B, B, B, B],
            [X, O, B, B, B],
            [X, B, B, B, B],
            [B, B, B, O, O],
        ]))
        expected = np.array([
            [X, O, B, B, B],
            [X, B, B, B, B],
            [X, O, B, B, B],
            [X, B, B, B, B],
            [O, B, B, O, O],
        ])
        initial_board = deepcopy(board)
        board = mcts.findNextMove(board, board.P1)
        #print("initial board : ")
        #initial_board.print()
        #print("Final board : ")
        #board.print()
        self.assertTrue(np.array_equal(board.board, expected))


if __name__ == '__main__':
    unittest.main()
