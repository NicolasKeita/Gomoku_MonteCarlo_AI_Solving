from queue import Queue
import numpy as np

X_WINS = "X_wins!"
O_WINS = "O_wins!"
DRAW = "Draw!"


class Brain:
    def __init__(self):
        self.map_size = 0
        self.board = []
        self.in_board = False

    def _create_board_(self):
        add = []
        for i in range(0, self.map_size):
            for j in range(0, self.map_size):
                add.append(' ')
                j += 1
            self.board.append(add)
            add = []
            i += 1

    def _add_X_(self, x, y):
        self.board[x][y] = "X"

    def think(self, stdin_input):
        if stdin_input[0] == "START":
            self.map_size = int(stdin_input[1])
            self._create_board_()
            print(self._get_static_eval(self.board))
            return "OK"
        elif stdin_input[0] == "TURN":
            opp_x = int(stdin_input[1])
            opp_y = int(stdin_input[2])
            self._add_X_(opp_x, opp_y)
            return "TURN"
        elif stdin_input[0] == "BEGIN":
            return "BEGIN"
        elif stdin_input[0] == "BOARD":
            self.board_loop()
            return "BOARD"
        elif stdin_input[0] == "END":
            return "END"
        elif stdin_input[0] == "ABOUT":
            print('name="EPIC BRAIN", version = "1.0", authors="Nicolas Keita" and "Warren OConnor", country="France"')
            return "ABOUT"

    def _board_fill_(self, stdin_input):
        if (stdin_input[0] == "DONE"):
            self.in_board = False
            return "DONE"
        else:
            input = stdin_input[0].split(',')
            if int(input[2]) == 1:
                self.board[int(input[0])][int(input[1])] = 'O'
                print(self.board)
                return ("1010")
            elif int(input[2]) == 2:
                self.board[int(input[0])][int(input[1])] = 'X'
                print(self.board)
                return ("1111")

    def think(self, stdin_input):
        if self.in_board == False:
            if stdin_input[0] == "START":
                self.map_size = int(stdin_input[1])
                self._create_board_()
                return "OK"
            elif stdin_input[0] == "TURN":
                opp_x = int(stdin_input[1])
                opp_y = int(stdin_input[2])
                self._add_X_(opp_x, opp_y)
                return "TURN"
            elif stdin_input[0] == "BEGIN":
                return "BEGIN"
            elif stdin_input[0] == "BOARD":
                self.in_board = True
                return "BOARD"
            elif stdin_input[0] == "END":
                return "END"
            elif stdin_input[0] == "ABOUT":
                print(
                    'name="EPIC BRAIN", version = "1.0", authors="Nicolas Keita" and "Warren OConnor", country="France"')
                return "ABOUT"
            else:
                return "ERROR2"
        else:
            return self._board_fill_(stdin_input)

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
        # TODO
        return False

    def _tuples(self, matrix):
        try:
            return tuple(self._tuples(a) for a in matrix)
        except TypeError:
            return matrix

    def _get_static_eval(self, board):
        board_tmp = [[1, 4, 4, 5, 9],
                     [1, 4, 4, 5, 9],
                     [1, 4, 2, 1, 1],
                     [1, 2, 1, 59, 10],
                     [1, 5, 10, 4, 65],
                     [1, 10, 20, 30, 40, 50]]
        board_tmp = list(set(self._tuples(board_tmp)))

        result = self._test_rows(board_tmp.copy())
        if result != DRAW:
            return result
        result = self._test_columns(board_tmp.copy())
        if result != DRAW:
            return result
        result = self._test_diagonals(board_tmp.copy())
        return result

    def _test_diagonals(self, board):
        return DRAW

    def _test_columns(self, board):
        board = np.matrix(board).T
        # print("BEFORE TRANSPOSE")
        # print(board)
        # board = np.transpose(board)
        # print("APTRES")
        # print(board)
        return self._test_rows(board)

    def _test_rows(self, board):
        print(board)
        print("END")
        counter_X = 0
        counter_O = 0
        for row_board in board:
            for char in row_board:
                if char == "X":
                    counter_X += 1
                else:
                    counter_X = 0
                if char == "O":
                    counter_O += 1
                else:
                    counter_O = 0
                if counter_X == 5:
                    return X_WINS
                elif counter_O == 5:
                    return O_WINS
        return DRAW

    def _get_all_possible_next_moves(self, board):
        return [board, board]  # TODO

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
