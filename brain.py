from queue import Queue
import math
import copy
import time
from Tnode import Tnode, Tree
from Board import Board
from MonteCarlo import MonteCarloTreeSearch

X_WINS = -1
O_WINS = 1
UNDEFINED = "Undefined"

BLANK = ' '
X_SQUARE = 'X'
O_SQUARE = 'O'
WIN_CONDITION = 3

IN_PROGRESS = -1
DRAW = 0
P1 = 1
P2 = 2


class Brain:
    def __init__(self):
        self.map_size = 0
        self.board = []
        self.in_board = False
        self.started = False
        self._pos_to_do = "BUG"
        self.debug = 0

    def _create_board_(self):
        add = []
        for i in range(0, self.map_size):
            for j in range(0, self.map_size):
                add.append(BLANK)
                j += 1
            self.board.append(add.copy())
            add.clear()
            i += 1

    def _add_char_to_board(self, char, positions):
        positions = positions.split(',')
        self.board[int(positions[1])][int(positions[0])] = char

    def _board_fill_(self, stdin_input):
        if stdin_input[0] == "DONE":
            self.in_board = False
            return "DONE"
        else:
            new_input = stdin_input[0].split(',')
            if int(new_input[2]) == 1:
                self.board[int(new_input[0])][int(new_input[1])] = O_SQUARE
                print(self.board)
                return "1010"
            elif int(new_input[2]) == 2:
                self.board[int(new_input[0])][int(new_input[1])] = X_SQUARE
                print(self.board)
                return "1111"

    def think(self, stdin_input):
        if not self.in_board:
            if stdin_input[0] == "START":
                if int(stdin_input[1]) < 5:
                    return "ERROR"
                self.map_size = int(stdin_input[1])
                self._create_board_()
                self.started = True
                return "OK"
            elif stdin_input[0] == "TURN":
                self._add_char_to_board(X_SQUARE, stdin_input[1])
                result = self._solve(self.board)
                self._add_char_to_board(O_SQUARE, result)
                return result
            elif stdin_input[0] == "BEGIN":
                pos = str(math.floor(self.map_size / 2)) + "," + \
                      str(math.floor(self.map_size / 2))
                self._add_char_to_board(O_SQUARE, pos)
                return pos
            elif stdin_input[0] == "BOARD":
                if not self.started:
                    return "ERROR"
                self.in_board = True
                return "BOARD"
            elif stdin_input[0] == "END":
                return "END"
            elif stdin_input[0] == "ABOUT":
                return 'name="EPIC BRAIN", version = "1.0", authors="Nicolas Keita" and "Warren OConnor", ' \
                       'country="France" '
            else:
                return "ERROR"
        else:
            return self._board_fill_(stdin_input)

    def _board_diff(self, board_1, board_2):
        for y in range(len(board_1)):
            for x in range(len(board_2)):
                if board_1[y][x] != board_2[y][x]:
                    return str(x) + "," + str(y)
        return None

    def _solve(self, board):
        mcts = MonteCarloTreeSearch()
        tmp_board = Board(board)
        new_board = Board(board)
        new_board = mcts.findNextMove(new_board, P1)
        return self._board_diff(new_board.board, tmp_board.board)

    """
    def _test_diagonals(self, board):
        for i in range(0, self.map_size):
            for j in range(0, self.map_size):
                if board[i][j] == "X":
                    if (i + 4 <= self.map_size and j + 4 <= self.map_size
                            and board[i + 1][j + 1] == "X" and board[i + 2][j + 2] == "X"
                            and board[i + 3][j + 3] == "X" and board[i + 4][j + 4] == "X"):
                        return X_WINS
                    elif (i - 4 >= 0 and j - 4 >= 0
                          and board[i - 1][j - 1] == "X" and board[i - 2][j - 2] == "X"
                          and board[i - 3][j - 3] == "X" and board[i - 4][j - 4] == "X"):
                        return X_WINS
                elif board[i][j] == "O":
                    if (i + 4 <= self.map_size and j + 4 <= self.map_size
                            and board[i + 1][j + 1] == "O" and board[i + 2][j + 2] == "O"
                            and board[i + 3][j + 3] == "O" and board[i + 4][j + 4] == "O"):
                        return O_WINS
                    elif (i - 4 >= 0 and j - 4 >= 0
                          and board[i - 1][j - 1] == "O" and board[i - 2][j - 2] == "O"
                          and board[i - 3][j - 3] == "O" and board[i - 4][j - 4] == "O"):
                        return O_WINS
        return
    """

    def board_loop(self):
        queue = Queue()
        # x = Thread(target=get_input, daemon=True)
        # x.start()
        while True:
            # print("while")
            if not queue.empty():
                stdin_input = queue.get()
                if stdin_input[0] == "DONE":
                    break
                try:
                    print("in try")
                    if int(stdin_input[2]) == 1:
                        self.board[int(stdin_input[0])][int(stdin_input[1])] = 'O'
                        print(self.board)
                    elif int(stdin_input[2]) == 2:
                        self.board[int(stdin_input[0])][int(stdin_input[1])] = 'X'
                        print(self.board)
                except (ValueError, IndexError):
                    print("ERROR")
