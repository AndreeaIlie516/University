from src.exceptions.exception import *

class Game:
    def __init__(self, board, algorithm):
        self._board = board
        self._algorithm = algorithm

    def player_move(self, player):
        """
        Function for determining the player move and put on the board
        :param player:
        :return:
        """
        if len(player) != 2:
            raise WrongCoordinates
        row = player[0]
        column = player[1]
        try:
            row = int(row)
            column = int(column)
        except ValueError:
            print('Please insert integer coordinates!')
        self._board.move(row, column, 'p')

    def computer_move(self):
        """
        Function for determining the computer move
        :return:
        """
        square = self._algorithm.next_move(self._board)
        self._board.move(square[0], square[1], 'c')
        return (square[0], square[1])

    def get_board(self):
        return self._board
