from queue import Queue
import math
from Board import Board
from MonteCarlo import MonteCarloTreeSearch

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

    def _board_fill(self, stdin_input):
        if stdin_input[0] == "DONE":
            self.in_board = False
            result = self._solve(self.board)
            self._add_char_to_board(O_SQUARE, result)
            return result
        else:
            new_input = stdin_input[0].split(',')
            if int(new_input[2]) == 1:
                self.board[int(new_input[0])][int(new_input[1])] = O_SQUARE
                return "WAIT"
            elif int(new_input[2]) == 2:
                self.board[int(new_input[0])][int(new_input[1])] = X_SQUARE
                return "WAIT"

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
                return "WAIT"
            elif stdin_input[0] == "END":
                return "END"
            elif stdin_input[0] == "ABOUT":
                return 'name="EPIC BRAIN", version = "1.0", authors="Nicolas Keita" and "Warren OConnor", ' \
                       'country="France" '
            else:
                return "ERROR"
        else:
            return self._board_fill(stdin_input)

    def _board_diff(self, board_1, board_2):
        for y in range(len(board_1)):
            for x in range(len(board_2)):
                if board_1[y][x] != board_2[y][x]:
                    return str(x) + "," + str(y)

    def _solve(self, board):
        mcts = MonteCarloTreeSearch()
        tmp_board = Board(board)
        new_board = Board(board)
        new_board = mcts.findNextMove(new_board, P1)
        return self._board_diff(new_board.board, tmp_board.board)

    def board_loop(self):
        queue = Queue()
        while True:
            if not queue.empty():
                stdin_input = queue.get()
                if stdin_input[0] == "DONE":
                    break
                try:
                    if int(stdin_input[2]) == 1:
                        self.board[int(stdin_input[0])][int(stdin_input[1])] = 'O'
                    elif int(stdin_input[2]) == 2:
                        self.board[int(stdin_input[0])][int(stdin_input[1])] = 'X'
                except (ValueError, IndexError):
                    print("ERROR")
