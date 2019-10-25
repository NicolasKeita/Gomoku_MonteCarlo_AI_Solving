import unittest
from UCT import UCT
from State import State
from Tnode import Tree
from Board import Board, Position
from MonteCarlo import MonteCarloTreeSearch


class TestMonteCarlo(unittest.TestCase):
    def test_uct_value(self):
        uct_value = 15.79
        self.assertAlmostEqual(UCT.uct_value(600, 300, 20), uct_value, delta=0.01)

    def test_all_possibles_states(self):
        t = Tree()
        initState = t.root.state
        possibleStates = initState.get_all_possible_states()
        self.assertTrue(len(possibleStates) > 0)

    def test_perform_move(self):
        board = Board()
        init_available_positions = len(board.get_empty_positions())
        board.perform_move(1, Position(1, 1))
        available_positions = len(board.get_empty_positions())
        self.assertTrue(init_available_positions > available_positions)

    def test_find_next_move_one_shoot(self):
        mcts = MonteCarloTreeSearch(timeout=4.8)
        board = Board(size=5)
        board.board = [
            ['X', 'O', ' ', ' ', ' '],
            ['X', 'O', ' ', ' ', ' '],
            ['X', 'O', ' ', ' ', ' '],
            ['X', 'O', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
        ]
        expected = [
            ['X', 'O', ' ', ' ', ' '],
            ['X', 'O', ' ', ' ', ' '],
            ['X', 'O', ' ', ' ', ' '],
            ['X', 'O', ' ', ' ', ' '],
            [' ', 'O', ' ', ' ', ' '],
        ]
        board = mcts.findNextMove(board, board.P1)
        print("Final board : ")
        board.print()
        self.assertTrue(board.board == expected)

    def test_find_next_move(self):
        return
        board = Board(size=19)
        player = board.P1
        mcts = MonteCarloTreeSearch(timeout=4.8)
        total_move = board.size * board.size
        for i in range(total_move):
            print("i = ", i)
            board.print()
            board = mcts.findNextMove(board, player)
            if board.check_status() != -1:
                break
            player = 3 - player
        win_status = board.check_status()
        board.print()
        self.assertTrue(win_status == board.DRAW)


if __name__ == '__main__':
    unittest.main()
