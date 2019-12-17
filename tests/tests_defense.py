import unittest
from srcs.Board import Board
from srcs.MonteCarlo import MonteCarloTreeSearch
from srcs.macros import *
import numpy as np
from copy import deepcopy
from srcs.brain import Brain


class TestCommandBoard(unittest.TestCase):
    def test_defense_diagonal_up_left_5x5(self):
        # Defense diagonal up left
        i = 0
        while i < 10:
            brain = Brain()
            brain.think("START 6".split(' '))
            brain.think("BOARD".split(' '))
            brain.think("4,4,1".split(' '))
            brain.think("4,5,2".split(' '))
            brain.think("5,5,1".split(' '))
            brain.think("3,4,2".split(' '))
            brain.think("5,3,1".split(' '))
            brain.think("2,3,2".split(' '))
            brain.think("3,2,1".split(' '))
            brain.think("1,2,2".split(' '))
            decision = brain.think("DONE".split(' '))
            self.assertTrue(decision == "0,1")
            i += 1

    def test_defense_vertical_up(self):
        # Defense vertical_down
        i = 0
        while i < 10:
            brain = Brain()
            brain.think("START 19".split(' '))
            brain.think("BOARD".split(' '))
            brain.think("0,0,1".split(' '))
            brain.think("1,0,2".split(' '))
            brain.think("0,1,1".split(' '))
            brain.think("1,1,2".split(' '))
            brain.think("0,2,1".split(' '))
            brain.think("1,2,2".split(' '))
            brain.think("2,2,1".split(' '))
            brain.think("1,3,2".split(' '))
            decision = brain.think("DONE".split(' '))
            self.assertTrue(decision == "1,4")
            i += 1

    def test_defense_diagonal_up_left(self):
        # Defense diagonal up left
        return
        i = 0
        while i < 5:
            brain = Brain()
            brain.think("START 19".split(' '))
            brain.think("BOARD".split(' '))
            """
            brain.think("10,10,1".split(' '))
            brain.think("10,11,2".split(' '))
            brain.think("11,11,1".split(' '))
            brain.think("9,10,2".split(' '))
            brain.think("11,9,1".split(' '))
            brain.think("8,9,2".split(' '))
            brain.think("11,12,1".split(' '))
            brain.think("7,8,2".split(' '))
            """
            brain.think("4,4,1".split(' '))
            brain.think("4,5,2".split(' '))
            brain.think("5,5,1".split(' '))
            brain.think("3,4,2".split(' '))
            brain.think("5,3,1".split(' '))
            brain.think("2,3,2".split(' '))
            brain.think("3,2,1".split(' '))
            brain.think("1,2,2".split(' '))
            brain.think("5,6,1".split(' '))
            brain.think("4,0,2".split(' '))
            print("DEBUT")
            Board(brain.board).print()
            decision = brain.think("DONE".split(' '))
            print(decision)
            print(decision)
            print(decision)
            Board(brain.board).print()
            self.assertTrue(decision == "6,7")
            i += 1


if __name__ == '__main__':
    unittest.main()
