import copy

X_WINS = 2
O_WINS = 1
DRAW = 0
UNDEFINED = "Undefined"

BLANK = ' '
X_SQUARE = 'X'
O_SQUARE = 'O'
WIN_CONDITION = 5

INFINITY = 9999
WIN_SCORE = 10

IN_PROGRESS = -1
DRAW = 0
P1 = 1
P2 = 2
END = 10


class Position:
    def __init__(self, y, x):
        self.x = x
        self.y = y


class Board:
    def __init__(self, board=None):
        self.board = [] if board is None else copy.deepcopy(board)
        self.map_size = 3
        self.total_moves = 0

    def perform_move(self, player, p):
        symbol = O_SQUARE if player == P1 else X_SQUARE
        self.total_moves += 1
        self.board[p.y][p.x] = symbol

    def check_status(self):
        result = self._get_static_eval(self.board)
        return result

    def get_empty_positions(self):
        empty_positions = []
        for y in range(len(self.board)):
            for x in range(len(self.board)):
                if self.board[y][x] == ' ':
                    empty_positions.append(Position(y, x))
        return empty_positions

    def print(self):
        for row in self.board:
            print(row)
        print('\n')

    def _get_static_eval(self, board):
        result = self._test_rows(copy.deepcopy(board))
        if result != IN_PROGRESS:
            return result
        result = self._test_columns(copy.deepcopy(board))
        if result != IN_PROGRESS:
            return result
        """
        result = self._test_diagonals(copy.deepcopy(board))
        if result != IN_PROGRESS:
            return result
        """
        if self._is_full():
            return DRAW
        return result

    def _is_full(self):
        for row in self.board:
            for char in row:
                if char == BLANK:
                    return False
        return True

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

    def _test_columns(self, board):
        # Transpose matrix
        board = [*zip(*board)]
        return self._test_rows(board)

    def _test_rows(self, board):
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
                if counter_X == WIN_CONDITION:
                    return X_WINS
                elif counter_O == WIN_CONDITION:
                    return O_WINS
        return IN_PROGRESS
