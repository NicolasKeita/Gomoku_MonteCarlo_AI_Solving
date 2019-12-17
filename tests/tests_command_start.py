import unittest
from srcs.Board import Board
from srcs.MonteCarlo import MonteCarloTreeSearch
from srcs.macros import *
import numpy as np
from copy import deepcopy
from srcs.brain import Brain


class TestCommandStart(unittest.TestCase):
    def test_command_start(self):
        brain = Brain()
        decision = brain.think("START 19".split(' '))
        for y in range(19):
            for x in range(19):
                self.assertTrue(brain.board[y][x] == BLANK, "Board is not empty at the beginning")
        self.assertTrue(decision == "OK")
