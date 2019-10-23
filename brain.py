from queue import Queue
from threading import Thread

X_WINS = "X_wins!"
O_WINS = "O_wins!"
DRAW = "Draw!"

class Brain:
    def __init__(self):
        self.map_size = 0
        self.board = []
    
    def _create_board_(self):
        add = []
        for i in range (0, self.map_size):
            for j in range (0, self.map_size):
                add.append(' ')
                j+=1
            self.board.append(add)
            add = []
            i += 1
    def _add_X_(self, x, y):
        self.board[x][y] = "X"
        
    def think(self, stdin_input):
        if stdin_input[0] == "START":
            self.map_size = int(stdin_input[1])
            self._create_board_()
            return "OK"
        elif stdin_input[0] == "TURN":
            opp_x = int(stdin_input[1])
            opp_y = int(stdin_input[2])
            self._add_X_(opp_x,opp_y)
            return "TURN"
        elif stdin_input[0] == "BEGIN":
            return "BEGIN"
        elif stdin_input[0] == "BOARD":
            board_loop(self)
            return "BOARD"
        elif stdin_input[0] == "END":
            return "END"
        elif stdin_input[0] == "ABOUT":
            print ('name="EPIC BRAIN", version = "1.0", authors="Nicolas Keita" and "Warren OConnor", country="France"') 
            return "ABOUT"          
        else:
            return "ERROR unknown command"
        
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

    def board_loop(self):
        queue = Queue()
       # x = Thread(target=get_input, daemon=True)
        #x.start()
        while True:
        #print("while")
            if not queue.empty():
                stdin_input = queue.get()
            if stdin_input[0] == "DONE":
                break
            try:
                print("in try")
                if(int(stdin_input[2]) == 1):
                    self.board[int(stdin_input[0])][int(stdin_input[1])] = 'O'
                    print(self.board)
                elif(int(stdin_input[2]) == 2):
                    self.board[int(stdin_input[0])][int(stdin_input[1])] = 'X'
                    print(self.board)
            except (ValueError, IndexError):
                print("ERROR")