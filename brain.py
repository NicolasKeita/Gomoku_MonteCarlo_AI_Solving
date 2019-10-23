X_WINS = "X_wins!"
O_WINS = "O_wins!"
DRAW = "Draw!"


class Brain:
    def __init__(self):
        self.map_size = 42

    def think(self, stdin_input):
        print(stdin_input)
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

    def _get_static_eval(self, board):
        # TODO
        return X_WINS

    def _get_all_possible_next_moves(self, board):
        return [board, board] # TODO
