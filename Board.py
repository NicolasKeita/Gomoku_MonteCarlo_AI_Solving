import copy

X_WINS = 2
O_WINS = 1

BLANK = ' '
X_SQUARE = 'X'
O_SQUARE = 'O'


class Position:
    def __init__(self, y, x):
        self.x = x
        self.y = y


class Board:
    def __init__(self, board=None, size=19):
        self.IN_PROGRESS = -1
        self.DRAW = 0
        self.P1 = 1
        self.P2 = 2
        self.WIN_CONDITION = 5

        self.size = size
        if board is None:
            self.board = [[BLANK] * self.size for _ in range(self.size)]
        else:
            self.board = board

    def perform_move(self, player, p):
        symbol = O_SQUARE if player == self.P1 else X_SQUARE
        self.board[p.y][p.x] = symbol

    def check_status(self):
        result = self._get_static_eval()
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

    def board_diff(self, board_2):
        for y in range(len(self.board)):
            for x in range(len(board_2.board)):
                if self.board[y][x] != board_2.board[y][x]:
                    return str(x) + "," + str(y)

    def _get_static_eval(self):
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

    def _is_full(self):
        for row in self.board:
            for char in row:
                if char == BLANK:
                    return False
        return True

    def _test_one_diagonal(self, board, y, x, symbol, symbol_win):
        if self.board[y][x] == symbol:
            if y + self.WIN_CONDITION <= len(board) and \
                    x + self.WIN_CONDITION <= len(board):
                if self.board[y + 1][x + 1] == symbol and \
                        self.board[y + 2][x + 2] == symbol and \
                        self.board[y + 3][x + 3] == symbol and \
                        self.board[y + 4][x + 4] == symbol:
                    return symbol_win

    def test_diagonals(self):
        board_size = len(self.board)
        for y in range(board_size):
            for x in range(board_size):
                result = self._test_one_diagonal(self.board, y, x, X_SQUARE, X_WINS)
                if result:
                    return result
                result = self._test_one_diagonal(self.board, y, x, O_SQUARE, O_WINS)
                if result:
                    return result
        return self.IN_PROGRESS

    def _test_columns(self):
        # Transpose matrix
        board = [*zip(*self.board)]
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
                if counter_X == self.WIN_CONDITION:
                    return X_WINS
                elif counter_O == self.WIN_CONDITION:
                    return O_WINS
        return self.IN_PROGRESS

