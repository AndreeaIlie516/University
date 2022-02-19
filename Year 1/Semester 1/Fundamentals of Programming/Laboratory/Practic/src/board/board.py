from texttable import Texttable
from src.exceptions.exception import *


class Board:
    def __init__(self):
        self._moves = 0
        self._board = [[0 for _ in range(3)] for _ in range(3)]

    def win(self):
        """
        Method for determining if there is any winner
        :return:
        """
        counter1 = 0
        counter2 = 0

        board = self._board

        """
        rows
        """
        for row in board:
            for position in row:
                if position == 1:
                    counter1 += position
                    counter2 = 0
                elif position == -1:
                    counter2 += position
                    counter1 = 0
                else:
                    counter1 = 0
                    counter2 = 0

                if counter1 == 3:
                    return counter1
                elif counter2 == -3:
                    return counter2

        counter1 = 0
        counter2 = 0

        """
        columns
        """
        for column in range(3):
            for row in range(3):
                position = board[row][column]
                if position == 1:
                    counter1 += position
                    counter2 = 0
                elif position == -1:
                    counter2 += position
                    counter1 = 0
                else:
                    counter1 = 0
                    counter2 = 0
                if counter1 == 3:
                    return counter1
                elif counter2 == -3:
                    return counter2

        counter1 = 0
        counter2 = 0
        """
        main diagonal
        """
        for i in range(3):
            position = board[i][i]
            if position == 1:
                counter1 += position
                counter2 = 0
            elif position == -1:
                counter2 += position
                counter1 = 0
            else:
                counter1 = 0
                counter2 = 0
            if counter1 == 3:
                return counter1
            elif counter2 == -3:
                return counter2

        counter1 = 0
        counter2 = 0

        """
        secondary diagonal
        """
        for i in range(3):
            position = board[i][3 - i - 1]
            if position == 1:
                counter1 += position
                counter2 = 0
            elif position == -1:
                counter2 += position
                counter1 = 0
            else:
                counter1 = 0
                counter2 = 0
            if counter1 == 3:
                return counter1
            elif counter2 == -3:
                return counter2


    def tie(self):
        """
        Method for determining if there is tie
        :return:
        """
        if self.win() is False and self._moves == 3 * 3:
            return True
        return False

    def placement_ends(self):
        """
        Method for determining if the placement phase ends
        :return:
        """
        if self.win() is False and self._moves == 8:
            return True
        return False

    def move(self, row, column, symbol):
        """
        Method for placing the move on the board
        :param row:
        :param column:
        :param symbol:
        :return:
        """
        if row < 0 or row >= 3 or column < 0 or column >= 3:
            raise OutsideBoard

        if self._board[row][column] != 0:
            print(self._board[row][column])
            raise Overwrite

        d = {'x': 1, 'o': -1}
        self._board[row][column] = d[symbol]
        self._moves += 1

    def reset(self):
        """
        Method for reseting the board
        :return:
        """
        self._board = [[0 for _ in range(3)] for _ in range(3)]

    def get_square(self, row, column):
        if row < 0 or row >= 3 or column < 0 or column >= 3:
            return OutsideBoard
        return self._board[row][column]

    def get_board(self):
        return self._board

    def __str__(self):
        t = Texttable()
        d = {0: ' ', 1: 'x', -1: 'o'}
        for row in self._board:
            row_copy = row[:]
            for j in range(3):
                row_copy[j] = d[row[j]]
            t.add_row(row_copy)

        return t.draw()

    def to_matrix(self):
        matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        board = self._board
        for row in range(3):
            for column in range(3):
                position = board[row][column]
                matrix[row][column] = position
        return matrix

    def from_matrix_to_board(self, matrix):
        board = self._board
        for row in range(0, 3):
            for column in range(0, 3):
                position = matrix[row][column]
                board[row][column] = position


