import random


class Algorithm:
    @staticmethod
    def next_move_placement(board):
        """
        compute the next move for the computer
        :param board:
        :return:
        """

        counter1 = 0
        counter2 = 0
        """
        rows
         """
        for row in range(3):
            for column in range(3):
                position = board.get_square(row, column)
                if position == 1:
                    counter1 += position
                    counter2 = 0
                elif position == -1:
                    counter2 += position
                    counter1 = 0
                else:
                    counter1 = 0
                    counter2 = 0

                if counter1 == 2:
                    if column < 2:
                        if board.get_square(row, column + 1) == 0:
                            return (row, column + 1)
                    else:
                        if board.get_square(row, 0) == 0:
                            return (row, 0)
                elif counter2 == -2:
                    if column < 2:
                        if board.get_square(row, column + 1) == 0:
                            return (row, column + 1)
                    else:
                        if board.get_square(row, 0) == 0:
                            return (row, 0)

        """
        columns
        """

        for column in range(3):
            for row in range(3):
                position = board.get_square(row, column)
                if position == 1:
                    counter1 += position
                    counter2 = 0
                elif position == -1:
                    counter2 += position
                    counter1 = 0
                else:
                    counter1 = 0
                    counter2 = 0
                if counter1 == 2:
                    if row < 2:
                        if board.get_square(row + 1, column) == 0:
                            return (row + 1, column)
                    else:
                        if board.get_square(0, column) == 0:
                            return (0, column)
                elif counter2 == -2:
                    if row < 2:
                        if board.get_square(row, column + 1) == 0:
                            return (row, column + 1)
                    else:
                        if board.get_square(0, column) == 0:
                            return (0, column)

        """
        main diagonal
        """
        for row in range(3):
            position = board.get_square(row, row)
            if position == 1:
                counter1 += position
                counter2 = 0
            elif position == -1:
                counter2 += position
                counter1 = 0
            else:
                counter1 = 0
                counter2 = 0
            if counter1 == 2:
                if row < 2:

                    if board.get_square(row + 1, row + 1) == 0:
                        return (row + 1, row + 1)
                else:
                    if board.get_square(0, 0) == 0:
                        return (0, 0)
            elif counter2 == -2:
                if row < 2:
                    if board.get_square(row + 1, row + 1) == 0:
                        return (row + 1, row + 1)
                else:
                    if board.get_square(0, 0) == 0:
                        return (0, 0)

        """
        secondary diagonal
        """
        for row in range(3):
            position = board.get_square(row, 3 - row - 1)
            if position == 1:
                counter1 += position
                counter2 = 0
            elif position == -1:
                counter2 += position
                counter1 = 0
            else:
                counter1 = 0
                counter2 = 0
            if counter1 == 2:
                if row < 2:
                    if board.get_square(row + 1, 0) == 0:
                        return (row + 1, 0)
                else:
                    if board.get_square(0, row) == 0:
                        return (0, row)
            elif counter2 == -2:
                if row < 2:
                    if board.get_square(row + 1, 0) == 0:
                        return (row + 1, 0)
                else:
                    if board.get_square(0, row) == 0:
                        return (0, row)
        for row in range(3):
            for column in range(3):
                if board.get_square(row, column) == 0:
                    return (row, column)


    @staticmethod
    def next_move_movement(board):
        """
        compute the next move for the computer
        :param board:
        :return:
        """
        while True:
            board = board.get_board()
            row = random.randint(0, 3)
            column = random.randint(0, 3)
            if board.get_square(row, column) == 0:
                return (row, column)

