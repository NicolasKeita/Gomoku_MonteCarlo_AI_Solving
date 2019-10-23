X_WINS = "X_wins!"
O_WINS = "O_wins!"
DRAW = "Draw!"


class Brain:
    def __init__(self):
        self.map_size = 0
        self.board = []

    def think(self, stdin_input):
        if stdin_input[0] == "START":
            self.map_size = int(stdin_input[1])
            return "OK"
        else:
            return "ERROR"

    def reset(self):
        self.map_size = 0

    def _solve(self, board):
        static_eval = self._get_static_eval(board)
        if static_eval == X_WINS or static_eval == O_WINS:
            return static_eval
        if self._is_full(board):
            return DRAW
        boards = self._get_all_possible_next_moves(board)
        board_evals = [self._solve(board_tmp) for board_tmp in boards]
        if X_WINS in board_evals:
            return X_WINS
        elif DRAW in board_evals:
            return DRAW
        else:
            return O_WINS

    def _is_full(self, board):
        #TODO
        return False

    def _tuples(self, matrix):
        try:
            return tuple(self._tuples(a) for a in matrix)
        except TypeError:
            return matrix

    def _get_static_eval(self, board):
        board_tmp = [[1, 4, 4], [1, 4, 4], [1, 4, 2], [1, 2, 1], [1, 5, 10]]
        # Test row
        board_unique = set(self._tuples(board_tmp))
#        for char in
        for char in board_unique:
            pass

        # potential_wins = list(potential_wins)
        # print(potential_wins)

        return X_WINS

    def _get_all_possible_next_moves(self, board):
        return [board, board] # TODO
