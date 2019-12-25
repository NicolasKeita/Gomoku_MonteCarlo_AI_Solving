import unittest
from srcs.UCT import UCT
from srcs.Board import Board, Position
from srcs.MonteCarlo import MonteCarloTreeSearch
from srcs.macros import *
import numpy as np


class TestMonteCarlo_board_7(unittest.TestCase):
    def test_find_next_move_one_shoot(self):
        mcts = MonteCarloTreeSearch(size_board=7)
        board_2 = Board(np.array([
            [X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK, BLANK, BLANK],
            [X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK, BLANK, BLANK],
            [X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK, BLANK, BLANK],
            [X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
        ]))
        expected = np.array([
            [X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK, BLANK, BLANK],
            [X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK, BLANK, BLANK],
            [X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK, BLANK, BLANK],
            [X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, O_SQUARE, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
        ])
        board = mcts.findNextMove(board_2, board_2.P1)

        #print("Final board : ")
        #board.print()
        self.assertTrue(np.array_equal(board.board, expected))

    def test_find_next_move_one_shoot_7_2(self):
        mcts = MonteCarloTreeSearch(size_board=7)
        board_2 = Board(np.array([
            [X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK, BLANK, BLANK],
            [X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK, BLANK, BLANK],
            [X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK, BLANK, BLANK],
            [X_SQUARE, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, O_SQUARE, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
        ]))
        expected = np.array([
            [X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK, BLANK, BLANK],
            [X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK, BLANK, BLANK],
            [X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK, BLANK, BLANK],
            [X_SQUARE, O_SQUARE, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, O_SQUARE, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
        ])
        board = mcts.findNextMove(board_2, board_2.P1)

        #print("Final board : ")
        #board.print()
        self.assertTrue(np.array_equal(board.board, expected))


if __name__ == '__main__':
    unittest.main()
