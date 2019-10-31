from copy import deepcopy
import numpy as np
from srcs.macros import *


class Position:
    def __init__(self, y, x):
        self.x = x
        self.y = y

    def to_string(self):
        return str(self.x) + "," + str(self.y)


class Board:
    def __init__(self, two_dim_board, copy=False, empty_pos=None):
        self.IN_PROGRESS = -1
        self.DRAW = 0
        self.P1 = 1
        self.P2 = 2
        self.WIN_CONDITION = 5
        self.lastest_move = None

            #self.board = np.full(shape=(self.size, self.size),
             #                    fill_value=BLANK)
        if copy:
            self.board = np.copy(two_dim_board)
            self.size = np.shape(self.board)[0]
            #print("le board")
            #self.print()
            #print("les pos empty : len", len(empty_pos))
            self.empty_pos = empty_pos.copy()
        else:
            self.board = two_dim_board
            self.size = np.shape(self.board)[0]
            self._update_empty_positions()
            #self.empty_pos = empty_pos.copy()

    def perform_move(self, player, p):
        symbol = O_SQUARE if player == self.P1 else X_SQUARE
        self.board[p.y][p.x] = symbol
        self.lastest_move = Position(p.y, p.x)
#        self._update_empty_positions()
        for i in range(len(self.empty_pos)):
            if self.empty_pos[i].y == p.y and self.empty_pos[i].x == p.x:
                self.empty_pos.pop(i)
                return
#        self.empty_pos = list(filter(lambda x: not (x.y == p.y and x.x == p.x),
 #                                    self.empty_pos))

    def check_status(self):
        result = self._test_rows(self.board)
        if result != self.IN_PROGRESS:
            return result
        result = self._test_columns()
        if result != self.IN_PROGRESS:
            return result
        result = self.test_diagonals()
        if result != self.IN_PROGRESS:
            return result
        if self._is_full():
            return self.DRAW
        return result

    def _update_empty_positions(self):
        self.empty_pos = []
        for y in range(self.size):
            for x in range(self.size):
                if self.board[y][x] == BLANK:
                    self.empty_pos.append(Position(y, x))

    def print(self):
        for row in self.board:
            print(row)
        print('\n')

    def _is_full(self):
        for row in self.board:
            for char in row:
                if char == BLANK:
                    return False
        return True

    def _test_one_diagonal(self, y, x, symbol, symbol_win):
        if self.board[y][x] == symbol:
            if y + self.WIN_CONDITION <= self.size and \
                    x + self.WIN_CONDITION <= self.size:
                if self.board[y + 1][x + 1] == symbol and \
                        self.board[y + 2][x + 2] == symbol and \
                        self.board[y + 3][x + 3] == symbol and \
                        self.board[y + 4][x + 4] == symbol:
                    return symbol_win

    def test_diagonals(self):
        for y in range(self.size):
            for x in range(self.size):
                result = self._test_one_diagonal(y, x, X_SQUARE, X_WINS)
                if result:
                    return result
                result = self._test_one_diagonal(y, x, O_SQUARE, O_WINS)
                if result:
                    return result
        return self.IN_PROGRESS

    def _test_columns(self):
        return self._test_rows(self.board.transpose())

    def _test_rows(self, board):
        for y in range(self.size):
            counter_O = 0
            counter_X = 0
            for x in range(self.size):
                if board[y][x] == X_SQUARE:
                    counter_X += 1
                else:
                    counter_X = 0
                if board[y][x] == O_SQUARE:
                    counter_O += 1
                else:
                    counter_O = 0
                if counter_X == self.WIN_CONDITION:
                    return X_WINS
                elif counter_O == self.WIN_CONDITION:
                    return O_WINS
        return self.IN_PROGRESS

