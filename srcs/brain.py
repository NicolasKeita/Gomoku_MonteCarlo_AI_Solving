from queue import Queue
import math
from srcs.Board import Board
from srcs.MonteCarlo import MonteCarloTreeSearch
import numpy as np
from srcs.macros import *


class Brain:
    def __init__(self):
        self.map_size = 19
        self.board = np.zeros(shape=(self.map_size, self.map_size))
        self.in_board = False
        self.started = False

    def _add_char_to_board(self, char, positions):
        positions = positions.split(',')
        self.board[int(positions[1])][int(positions[0])] = char

    def _board_fill(self, stdin_input):
        if stdin_input[0] == "DONE":
            self.in_board = False
            result = self._solve(self.board)
            self._add_char_to_board(O_SQUARE, result)
            return result
        else:
            new_input = stdin_input[0].split(',')
            x = int(new_input[0])
            y = int(new_input[1])
            player = int(new_input[2])
            self.board[y][x] = player
            return None

    def think(self, stdin_input):
        if not self.in_board:
            if stdin_input[0] == "START":
                if int(stdin_input[1]) < 5:
                    return "ERROR"
                self.map_size = int(stdin_input[1])
                self.board = np.zeros(shape=(self.map_size, self.map_size))
                self.started = True
                return "OK"
            elif stdin_input[0] == "TURN":
                #start = time.time()
                self._add_char_to_board(X_SQUARE, stdin_input[1])
                result = self._solve(self.board)
                self._add_char_to_board(O_SQUARE, result)
                #print("Temps pour resoudre : ", time.time() - start, file=sys.stderr)
                return result
            elif stdin_input[0] == "BEGIN":
                pos = str(math.floor(self.map_size / 2)) + "," + \
                      str(math.floor(self.map_size / 2))
                self._add_char_to_board(O_SQUARE, pos)
                self.started = True
                return pos
            elif stdin_input[0] == "BOARD":
                if not self.started:
                    return "ERROR"
                self.in_board = True
                return None
            elif stdin_input[0] == "END":
                return "END"
            elif stdin_input[0] == "ABOUT":
                return 'name="EPIC BRAIN", version = "1.0", authors="Nicolas Keita" and "Warren OConnor", ' \
                       'country="France" '
            elif stdin_input[0] == "INFO":
                return ""
            else:
                return "ERROR"
        else:
            return self._board_fill(stdin_input)

    def _solve(self, board):
        mcts = MonteCarloTreeSearch(size_board=len(board))
        new_board = mcts.findNextMove(Board(board), P1)
        return new_board.lastest_move.to_string()

    """
    def board_loop(self):
        queue = Queue()
        while True:
            if not queue.empty():
                stdin_input = queue.get()
                if stdin_input[0] == "DONE":
                    break
                try:
                    if int(stdin_input[2]) == 1:
                        self.board[int(stdin_input[1])][int(stdin_input[0])] = 'O'
                    elif int(stdin_input[2]) == 2:
                        self.board[int(stdin_input[1])][int(stdin_input[0])] = 'X'
                except (ValueError, IndexError):
                    print("ERROR")
    """