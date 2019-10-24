from queue import Queue
import math
import numpy as np
import copy

X_WINS = "X_wins!"
O_WINS = "O_wins!"
DRAW = "Draw!"
UNDEFINED = "Undefined"

BLANK = ' '
X_SQUARE = 'X'
O_SQUARE = 'O'


class Brain:
    def __init__(self):
        self.map_size = 0
        self.board = []
        self.in_board = False
        self._pos_to_do = "BUG"

    def _create_board_(self):
        add = []
        for i in range(0, self.map_size):
            for j in range(0, self.map_size):
                add.append(BLANK)
                j += 1
            self.board.append(add)
            add = []
            i += 1

    def _add_char_to_board(self, char, positions):
        positions = positions.split(',')
        self.board[int(positions[0])][int(positions[1])] = char

    def think(self, stdin_input):
        if stdin_input[0] == "START":
            self.map_size = int(stdin_input[1])
            self._create_board_()
            return "OK"
        elif stdin_input[0] == "TURN":
            self._add_char_to_board(X_SQUARE, stdin_input[1])
            self._solve(self.board)
            return self._pos_to_do
        elif stdin_input[0] == "BEGIN":
            pos = str(math.floor(self.map_size / 2)) + "," + \
                  str(math.floor(self.map_size / 2))
            self._add_char_to_board('O', pos)
            return pos
        elif stdin_input[0] == "BOARD":
            self.board_loop()
            return "BOARD"
        elif stdin_input[0] == "END":
            return "END"
        elif stdin_input[0] == "ABOUT":
            print('name="EPIC BRAIN", version = "1.0", authors="Nicolas Keita" and "Warren OConnor", country="France"')
            return "ABOUT"

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

    def reset(self):
        self.map_size = 0

    def _is_X_turn(self, board):
        x_count = 0
        for row in board:
            x_count += row.count(X_SQUARE)
            x_count -= row.count(O_SQUARE)
        return x_count == 0

    def _board_diff(self, board_1, board_2):
        for y in range(len(board_1)):
            for x in range(len(board_2)):
                if board_1[y][x] != board_2[y][x]:
                    return str(x) + "," + str(y)
        return None

    def _solve(self, board):
        static_eval = self._get_static_eval(board)
        if static_eval == X_WINS or static_eval == O_WINS:
            return static_eval
        if self._is_full(board):
            return DRAW
        X_turn = self._is_X_turn(board)
        boards = self._get_all_possible_next_moves(board, X_turn)
        board_evals = [self._solve(board_tmp) for board_tmp in boards]
        for i in range(len(board_evals)):
            if board_evals[i] == O_WINS:
                self._pos_to_do = self._board_diff(boards[i], board)
                return O_WINS
        for i in range(len(board_evals)):
            if board_evals[i] == DRAW:
                self._pos_to_do = self._board_diff(boards[i], board)
                return DRAW
        for i in range(len(board_evals)):
            if board_evals[i] == X_WINS:
                self._pos_to_do = self._board_diff(boards[i], board)
                return X_WINS

    def _is_full(self, board):
        for row in board:
            for char in row:
                if char == BLANK:
                    return False
        return True

    def _get_static_eval(self, board):
        # remove duplicate rows
        board = [list(t) for t in set(tuple(element) for element in board)]

        result = self._test_rows(copy.deepcopy(board))
        if result != UNDEFINED:
            return result
        result = self._test_columns(copy.deepcopy(board))
        if result != UNDEFINED:
            return result
        result = self._test_diagonals(copy.deepcopy(board))
        return result

    def _test_diagonals(self, board):
        return UNDEFINED

    def _test_columns(self, board):
        # Transpose matrix
        board = [*zip(*board)]
        return self._test_rows(board)

    def _test_rows(self, board):
        win_condition = 3
        for row_board in board:
            counter_O = 0
            counter_X = 0
            for char in row_board:
                if char == X_SQUARE:
                    counter_X += 1
                else:
                    counter_X = 0
                if char == O_SQUARE:
                    counter_O += 1
                else:
                    counter_O = 0
                if counter_X == win_condition:
                    return X_WINS
                elif counter_O == win_condition:
                    return O_WINS
        return UNDEFINED

    def _get_all_possible_next_moves(self, board, X_turn):
        symbol = X_SQUARE if X_turn else O_SQUARE
        boards = []
        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x] == BLANK:
                    tmp_board = copy.deepcopy(board)
                    tmp_board[y][x] = symbol
                    boards.append(tmp_board)
        return boards

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
