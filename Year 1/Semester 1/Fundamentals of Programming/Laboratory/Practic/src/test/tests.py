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
        for row in range(3):
            for col in range(3):
                self.assertEqual(board.get_square(row, col), 0)

    def test_board_move(self):
        board = Board()
        board.move(1, 1, 'x')
        self.assertEqual(board.get_square(1, 1), 1)

    def test_board_win(self):
        board = Board()

        board1 = board.get_board()
        self.assertEqual(board._board, board1)

        board.move(0, 0, 'x')
        board.move(0, 1, 'x')
        board.move(0, 2, 'x')
        self.assertEqual(board.win(), 3)


        board.reset()

        board.move(0, 0, 'o')
        board.move(0, 1, 'o')
        board.move(0, 2, 'o')
        self.assertEqual(board.win(), -3)

        board.reset()

        board.move(0, 2, 'x')
        board.move(1, 1, 'x')
        board.move(2, 0, 'x')
        self.assertEqual(board.win(), 3)

        board.reset()

        board.move(0, 2, 'o')
        board.move(1, 1, 'o')
        board.move(2, 0, 'o')
        self.assertEqual(board.win(), -3)

        board.reset()

        board.move(0, 0, 'x')
        board.move(1, 1, 'x')
        board.move(2, 2, 'x')
        self.assertEqual(board.win(), 3)

        board.reset()

        board.move(0, 0, 'o')
        board.move(1, 1, 'o')
        board.move(2, 2, 'o')
        self.assertEqual(board.win(), -3)

        board.reset()

        board.move(0, 0, 'x')
        board.move(1, 2, 'x')
        board.move(2, 2, 'x')
        self.assertNotEqual(board.win(), 3)

        with self.assertRaises(Overwrite):
            board.move(0, 0, 'x')

        with self.assertRaises(OutsideBoard):
            board.move(0, 3, 'x')

        self.assertEqual(board.get_square(0, 3), OutsideBoard)


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

        board.reset()
        board1 = game.get_board()
        self.assertEqual(board, board1)

        game.player_move2(['1', '1'], ['0', '0'])
        self.assertEqual(board.get_square(1, 1), 0)


class AlgorithmTest(unittest.TestCase):
    def test_algorithm(self):
        board = Board()
        algorithm = Algorithm()
        self.assertEqual(algorithm.next_move_placement(board), (0, 0))
        board.move(0, 0, 'x')
        self.assertEqual(algorithm.next_move_placement(board), (0, 1))
        board.move(0, 1, 'x')


if __name__ == '__main__':
    unittest.main()
