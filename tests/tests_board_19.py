import unittest
from srcs.Board import Board
from srcs.MonteCarlo import MonteCarloTreeSearch
from srcs.macros import *
import numpy as np


class TestMonteCarlo(unittest.TestCase):
    def test_find_next_move_one_shoot_7_4(self):
        return
        mcts = MonteCarloTreeSearch(timeout=4.3, size_board=19)
        board_2 = Board(np.array([[B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
                                  [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
                                  [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
                                  [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
                                  [B, B, B, B, X, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
                                  [B, B, B, B, B, O, B, B, B, B, B, B, B, B, B, B, B, B, B],
                                  [B, B, B, B, B, O, O, B, B, B, B, B, B, B, B, B, B, B, B],
                                  [B, B, B, B, B, O, X, O, B, B, B, B, B, B, B, B, B, B, B],
                                  [B, B, B, B, B, X, X, X, O, B, B, B, B, B, B, B, B, B, B],
                                  [B, B, B, B, B, O, X, X, X, B, B, B, B, B, B, B, B, B, B],
                                  [B, B, B, B, O, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
                                  [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
                                  [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
                                  [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
                                  [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
                                  [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
                                  [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
                                  [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
                                  [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B], ]))
        expected = np.array([
            [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, X, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, O, B, B, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, O, O, B, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, O, X, O, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, X, X, X, O, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, O, X, X, X, O, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, O, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
        ])
        board = mcts.findNextMove(board_2, board_2.P1)

        #print("Final board : Lastest move : ", board.lastest_move.to_string())
        #board.print()
        self.assertTrue(np.array_equal(board.board, expected))

    def test_find_next_move_one_shoot_7_3(self):
        return
        mcts = MonteCarloTreeSearch(timeout=4.3, size_board=19)
        board_2 = Board(np.array([[B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
                                  [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
                                  [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
                                  [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
                                  [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
                                  [B, B, B, B, B, O, B, B, B, B, B, B, B, B, B, B, B, B, B],
                                  [B, B, B, B, B, O, O, B, B, B, B, B, B, B, B, B, B, B, B],
                                  [B, B, B, B, B, O, X, O, B, B, B, B, B, B, B, B, B, B, B],
                                  [B, B, B, B, B, X, X, X, O, B, B, B, B, B, B, B, B, B, B],
                                  [B, B, B, B, B, O, X, X, X, B, B, B, B, B, B, B, B, B, B],
                                  [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
                                  [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
                                  [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
                                  [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
                                  [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
                                  [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
                                  [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
                                  [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
                                  [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B], ]))
        expected = np.array([
            [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, O, B, B, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, O, O, B, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, O, X, O, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, X, X, X, O, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, O, X, X, X, O, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
        ])
        expected_2 = np.array([
            [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, O, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, O, B, B, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, O, O, B, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, O, X, O, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, X, X, X, O, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, O, X, X, X, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
        ])
        board = mcts.findNextMove(board_2, board_2.P1)

        #print("Final board : Lastest move : ", board.lastest_move.to_string())
        #board.print()
        self.assertTrue(np.array_equal(board.board, expected) or np.array_equal(board.board, expected_2))

    def test_find_next_move(self):
        # computer vs computer
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
        #board.print()
        self.assertTrue(win_status == board.DRAW)


if __name__ == '__main__':
    unittest.main()
