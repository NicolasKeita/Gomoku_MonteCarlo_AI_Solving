import numpy as np
from srcs.macros import *


class Position:
    def __init__(self, y, x):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Position):
            return NotImplemented
        return self.x == other.x and self.y == other.y

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

        if copy:
            self.board = np.copy(two_dim_board)
            self.size = np.shape(self.board)[0]
            self.empty_pos = empty_pos.copy()
        else:
            self.board = two_dim_board
            self.size = np.shape(self.board)[0]
            self._update_empty_positions()

    def perform_move(self, player, p):
        symbol = O_SQUARE if player == self.P1 else X_SQUARE
        self.board[p.y][p.x] = symbol
        self.lastest_move = Position(p.y, p.x)
        self._add_pos_to_the_lastest_move(p)
        #self._update_empty_positions()

    def check_status(self):
        # print("DEBUT")
        for run in self.get_runs(self.board, 5):
            return run['player']
        if self._is_full():
            return self.DRAW
        return self.IN_PROGRESS

    def _update_empty_positions(self):
        self.empty_pos = []
        for y in range(self.size):
            for x in range(self.size):
                if self.board[y][x] == BLANK and self.is_there_coin_around_last_move(y=y, x=x):
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

    def is_there_coin_around_last_move(self, y, x):
        for y_tmp in range(y - 2, y + 3):
            for x_tmp in range(x - 2, x + 3):
                try:
                    if self.board[y_tmp][x_tmp] > BLANK:
                        return True
                    pass
                except IndexError:
                    pass
        return False

    def _add_pos_to_the_lastest_move(self, p):
        for y in range(p.y - 2, p.y + 3):
            for x in range(p.x - 2, p.x + 3):
                try:
                    if y != p.y and x != p.x and self.board[y][x] == BLANK:
                        self.empty_pos.append(Position(y=y, x=x))
                except IndexError:
                    pass

    def get_runs(self, raw_grid, run_size):
        # Offsets to find the previous cell in all four directions.
        offsets = {
            'h': (0, -1),  # _
            'v': (-1, 0),  # |
            'f': (-1, 1),  # /
            'b': (-1, -1),  # \
        }

        # Helpers to check for valid array bounds and to return a new cell dict.
        size = len(raw_grid)
        in_bounds = lambda r, c: r >= 0 and c >= 0 and r < size and c < size
        new_cell = lambda i, j, p: dict(h=1, v=1, f=1, b=1, i=i, j=j, player=p)

        # Use the raw grid to create a grid of cell dicts.
        grid = []
        for i, row in enumerate(raw_grid):
            grid.append([])
            for j, player in enumerate(row):
                # Add a cell dict to the grid (or None for empty spots).
                cell = new_cell(i, j, player) if player else None
                grid[i].append(cell)
                if not cell: continue

                # For each direction, look to the previous cell. If it matches the
                # current player, we can extend the run in that direction.
                for d, offset in offsets.items():
                    r, c = (i + offset[0], j + offset[1])
                    if in_bounds(r, c):
                        prev = grid[r][c]
                        if prev and prev['player'] == cell['player']:
                            # We have a match, so the run size is one bigger,
                            # and we will track that run in the current cell,
                            # not the previous one.
                            cell[d] = prev[d] + 1
                            prev[d] = None

        # For all non-None cells, yield run info for any runs that are big enough.
        for cell in (c for row in grid for c in row if c):
            for d in offsets:
                if cell[d] and cell[d] >= run_size:
                    yield dict(
                        player=cell['player'],
                        endpoint=(cell['i'], cell['j']),
                        direction=d,
                        run_size=cell[d],
                    )
