import unittest
from srcs.Board import Board
from srcs.MonteCarlo import MonteCarloTreeSearch
from srcs.macros import *
import numpy as np
from copy import deepcopy
from srcs.brain import Brain


class TestCommandBoard(unittest.TestCase):
    def test_command_board(self):
        brain = Brain()
        brain.think("START 19".split(' '))
        decision = brain.think("BOARD".split(' '))
        for row in brain.board:
            for number in row:
                self.assertTrue(number == 0, "Board is not empty at the beginning")
        self.assertTrue(decision is None)
        decision = brain.think("10,10,1".split(' '))
        for y in range(len(brain.board)):
            for x in range(len(brain.board[0])):
                if y == 10 and x == 10:
                    continue
                self.assertTrue(brain.board[y][x] == BLANK, "Board command added extra numbers")
        self.assertTrue(brain.board[10][10] == O, "Board command failed")
        self.assertTrue(decision is None)

    def test_command_board_fill_entire_board(self):
        brain = Brain()
        brain.think("START 19".split(' '))
        brain.think("BOARD".split(' '))
        brain.think("10,10,1".split(' '))
        brain.think("10,10,2".split(' '))
        self.assertTrue(brain.board[10][10] == X, "Board command failed")
        brain.think("10,10,1".split(' '))
        self.assertTrue(brain.board[10][10] == O, "Board command failed")
        brain.think("10,11,2".split(' '))
        self.assertTrue(brain.board[11][10] == X, "Board command failed")
        brain.think("11,11,1".split(' '))
        self.assertTrue(brain.board[11][11] == O, "Board command failed")
        brain.think("9,10,2".split(' '))
        self.assertTrue(brain.board[10][9] == X, "Board command failed")
        for y in range(len(brain.board)):
            for x in range(len(brain.board[0])):
                if (y == 10 and x == 10) or \
                        (y == 11 and x == 10) or \
                        (y == 11 and x == 11) or \
                        (y == 10 and x == 9):
                    continue
                self.assertTrue(brain.board[y][x] == BLANK, "Board command added extra numbers")


if __name__ == '__main__':
    unittest.main()
