class Algorithm:
    @staticmethod
    def next_move(board):
        """
        compute the next move for the computer
        :param board:
        :return:
        """
        for row in range(15):
            for column in range(15):
                if board.get_square(row, column) == 0:
                    return (row, column)