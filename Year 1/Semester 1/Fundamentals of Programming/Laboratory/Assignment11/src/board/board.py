from texttable import Texttable
from src.exceptions.exception import *


class Board:
    def __init__(self):
        self._moves = 0
        self._board = [[0 for _ in range(15)] for _ in range(15)]

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

                if counter1 == 5:
                    return counter1
                elif counter2 == -5:
                    return counter2

        """
        columns
        """
        for column in range(15):
            for row in range(15):
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
                if counter1 == 5:
                    return counter1
                elif counter2 == -5:
                    return counter2

        """
        main diagonal
        """
        for i in range(15):
            for d in range(14 - i, 15):
                position = board[d - (14 - i)][d]
                if position == 1:
                    counter1 += position
                    counter2 = 0
                elif position == -1:
                    counter2 += position
                    counter1 = 0
                else:
                    counter1 = 0
                    counter2 = 0
                if counter1 == 5:
                    return counter1
                elif counter2 == -5:
                    return counter2
        for i in range(13, -1, -1):
            for d in range(14 - i, 15):
                position = board[d][d - (14 - i)]
                if position == 1:
                    counter1 += position
                    counter2 = 0
                elif position == -1:
                    counter2 += position
                    counter1 = 0
                else:
                    counter1 = 0
                    counter2 = 0
                if counter1 == 5:
                    return counter1
                elif counter2 == -5:
                    return counter2

        """
        secondary diagonal
        """
        for i in range(31):
            if i < 15:
                for d in range(i + 1):
                    position = board[d][i - d]
                    if position == 1:
                        counter1 += position
                        counter2 = 0
                    elif position == -1:
                        counter2 += position
                        counter1 = 0
                    else:
                        counter1 = 0
                        counter2 = 0
                    if counter1 == 5:
                        return counter1
                    elif counter2 == -5:
                        return counter2
            else:
                for d in range(i - 14, 15):
                    position = board[d][i - d]
                    if position == 1:
                        counter1 += position
                        counter2 = 0
                    elif position == -1:
                        counter2 += position
                        counter1 = 0
                    else:
                        counter1 = 0
                        counter2 = 0
                    if counter1 == 5:
                        return counter1
                    elif counter2 == -5:
                        return counter2

    def tie(self):
        """
        Method for determining if there is tie
        :return:
        """
        if self.win() is False and self._moves == 15 * 15:
            return True
        else:
            return False

    def move(self, row, column, symbol):
        """
        Method for placing the move on the board
        :param row:
        :param column:
        :param symbol:
        :return:
        """
        if row < 0 or row >= 15 or column < 0 or column >= 15:
            raise OutsideBoard

        if self._board[row][column] != 0:
            print(self._board[row][column])
            raise Overwrite

        d = {'p': 1, 'c': -1}
        self._board[row][column] = d[symbol]
        self._moves += 1

    def reset(self):
        """
        Method for reseting the board
        :return:
        """
        self._board = [[0 for _ in range(15)] for _ in range(15)]

    def get_square(self, row, column):
        if row < 0 or row >= 15 or column < 0 or column >= 15:
            return OutsideBoard
        return self._board[row][column]

    def get_board(self):
        return self._board

    def __str__(self):
        t = Texttable()
        d = {0: ' ', 1: 'p', -1: 'c'}
        for row in self._board:
            row_copy = row[:]
            for j in range(15):
                row_copy[j] = d[row[j]]
            t.add_row(row_copy)

        return t.draw()

