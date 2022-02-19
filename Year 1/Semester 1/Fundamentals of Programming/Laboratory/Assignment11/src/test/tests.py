from src.board.board import Board
from src.game.algorithm import Algorithm
from src.game.game import Game
from src.exceptions.exception import *
import unittest


class BoardTests(unittest.TestCase):
    def test_board_create(self):
        board = Board()
        self.assertEqual(board.win(), None)
        self.assertEqual(board.tie(), False)
        for row in range(15):
            for col in range(15):
                self.assertEqual(board.get_square(row, col), 0)

    def test_board_move(self):
        board = Board()
        board.move(1, 1, 'p')
        self.assertEqual(board.get_square(1, 1), 1)

    def test_board_win(self):
        board = Board()

        board1 = board.get_board()
        self.assertEqual(board._board, board1)

        board.move(1, 1, 'p')
        board.move(1, 5, 'p')
        board.move(1, 4, 'p')
        board.move(1, 3, 'p')
        board.move(1, 2, 'p')
        self.assertEqual(board.win(), 5)

        board.reset()

        board.move(1, 1, 'p')
        board.move(2, 1, 'p')
        board.move(3, 1, 'p')
        board.move(4, 1, 'p')
        board.move(5, 1, 'p')
        self.assertEqual(board.win(), 5)

        board.reset()

        board.move(1, 1, 'c')
        board.move(1, 5, 'c')
        board.move(1, 4, 'c')
        board.move(1, 3, 'c')
        board.move(1, 2, 'c')
        self.assertEqual(board.win(), -5)

        board.reset()

        board.move(1, 1, 'c')
        board.move(2, 1, 'c')
        board.move(3, 1, 'c')
        board.move(4, 1, 'c')
        board.move(5, 1, 'c')
        self.assertEqual(board.win(), -5)

        board.reset()

        board.move(1, 1, 'p')
        board.move(2, 2, 'p')
        board.move(3, 3, 'p')
        board.move(4, 4, 'p')
        board.move(5, 5, 'p')
        self.assertEqual(board.win(), 5)

        board.reset()

        board.move(1, 1, 'c')
        board.move(2, 2, 'c')
        board.move(3, 3, 'c')
        board.move(4, 4, 'c')
        board.move(5, 5, 'c')
        self.assertEqual(board.win(), -5)

        board.reset()

        board.move(10, 0, 'p')
        board.move(11, 1, 'p')
        board.move(12, 2, 'p')
        board.move(13, 3, 'p')
        board.move(14, 4, 'p')
        self.assertEqual(board.win(), 5)

        board.reset()

        board.move(10, 0, 'c')
        board.move(11, 1, 'c')
        board.move(12, 2, 'c')
        board.move(13, 3, 'c')
        board.move(14, 4, 'c')
        self.assertEqual(board.win(), -5)

        board.reset()

        board.move(0, 4, 'p')
        board.move(1, 3, 'p')
        board.move(2, 2, 'p')
        board.move(3, 1, 'p')
        board.move(4, 0, 'p')
        self.assertEqual(board.win(), 5)

        board.reset()

        board.move(0, 4, 'c')
        board.move(1, 3, 'c')
        board.move(2, 2, 'c')
        board.move(3, 1, 'c')
        board.move(4, 0, 'c')
        self.assertEqual(board.win(), -5)

        board.reset()

        board.move(10, 14, 'p')
        board.move(11, 13, 'p')
        board.move(12, 12, 'p')
        board.move(13, 11, 'p')
        board.move(14, 10, 'p')
        self.assertEqual(board.win(), 5)

        board.reset()

        board.move(10, 14, 'c')
        board.move(11, 13, 'c')
        board.move(12, 12, 'c')
        board.move(13, 11, 'c')
        board.move(14, 10, 'c')
        self.assertEqual(board.win(), -5)

        with self.assertRaises(Overwrite):
            board.move(10, 14, 'p')

        with self.assertRaises(OutsideBoard):
            board.move(10, 15, 'p')

        self.assertEqual(board.get_square(10, 15), OutsideBoard)


class GameTest(unittest.TestCase):
    def test_game(self):
        board = Board()
        algorithm = Algorithm()
        game = Game(board, algorithm)

        board1 = game.get_board()
        self.assertEqual(board, board1)

        game.player_move(['1', '1'])
        self.assertEqual(board.get_square(1, 1), 1)

        with self.assertRaises(WrongCoordinates):
            game.player_move(['1'])

        move = game.computer_move()
        self.assertEqual(move, (0, 0))


class AlgorithmTest(unittest.TestCase):
    def test_algorithm(self):
        board = Board()
        algorithm = Algorithm()
        self.assertEqual(algorithm.next_move(board), (0, 0))
        board.move(0, 0, 'p')
        self.assertEqual(algorithm.next_move(board), (0, 1))
        board.move(0, 1, 'p')
        self.assertEqual(algorithm.next_move(board), (0, 2))


if __name__ == '__main__':
    unittest.main()
