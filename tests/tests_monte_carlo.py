import unittest
from srcs.UCT import UCT
from srcs.Board import Board, Position
from srcs.MonteCarlo import MonteCarloTreeSearch
from srcs.macros import *
import numpy as np


class TestMonteCarlo(unittest.TestCase):
    def test_find_next_move_one_shoot_5_1(self):
        return
        mcts = MonteCarloTreeSearch(timeout=4.3, size_board=5)
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
        return
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
        return
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

    def test_find_next_move_one_shoot(self):
        return
        mcts = MonteCarloTreeSearch(timeout=4.3, size_board=7)
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
        return
        mcts = MonteCarloTreeSearch(timeout=4.8, size_board=7)
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

    def test_find_next_move_one_shoot_7_4(self):
        return
        mcts = MonteCarloTreeSearch(timeout=4.8, size_board=19)
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

        print("Final board : Lastest move : ", board.lastest_move.to_string())
        board.print()
        self.assertTrue(np.array_equal(board.board, expected))

    def test_find_next_move_one_shoot_7_3(self):
        while True:
            mcts = MonteCarloTreeSearch(timeout=4.8, size_board=19)
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

            print("Final board : Lastest move : ", board.lastest_move.to_string())
            board.print()
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
        board.print()
        self.assertTrue(win_status == board.DRAW)


if __name__ == '__main__':
    unittest.main()
