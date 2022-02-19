from src.exceptions.exception import *

class Game:
    def __init__(self, board, algorithm):
        self._board = board
        self._algorithm = algorithm

    def player_move(self, player):
        """
        Function for determining the player move and put on the board during the placement phase
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
        self._board.move(row, column, 'x')

    def player_move2(self, player_initial, player_new):
        """
        Function for determining the player move and put on the board during the movement phase
        :param player:
        :return:
        """
        if len(player_initial) != 2:
            raise WrongCoordinates

        row_init = player_initial[0]
        column_init = player_initial[1]
        try:
            row_init = int(row_init)
            column_init = int(column_init)
        except ValueError:
            print('Please insert integer coordinates!')

        if len(player_new) != 2:
            raise WrongCoordinates

        row_new = player_new[0]
        column_new = player_new[1]
        try:
            row_new = int(row_new)
            column_new = int(column_new)
        except ValueError:
            print('Please insert integer coordinates!')

        if abs(row_new - row_init) != 1 or abs(column_new - column_init) != 0:
            print('Please insert integer coordinates!')
            return


        self._board.move(row_init, column_init, ' ')
        self._board.move(row_new, column_new, 'x')


    def computer_move(self):
        """
        Function for determining the computer move during the placement phase
        :return:
        """
        square = self._algorithm.next_move_placement(self._board)
        self._board.move(square[0], square[1], 'o')
        return (square[0], square[1])

    def computer_move2(self):
        """
        Function for determining the computer move during the movement phase
        :return:
        """
        square = self._algorithm.next_move(self._board)
        self._board.move(square[0], square[1], 'o')
        return (square[0], square[1])

    def get_board(self):
        return self._board

    def get_matrix(self):
        return self._board.to_matrix()

    def set_board_from_matrix(self, matrix):
        board = self._board
        board.from_matrix_to_board(matrix)
