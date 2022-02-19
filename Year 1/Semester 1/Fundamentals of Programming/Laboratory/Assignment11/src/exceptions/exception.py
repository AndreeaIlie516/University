class WrongCoordinates(Exception):
    """
    Exception for wrong coordinates
    """
    pass


class OutsideBoard(Exception):
    """
    Exception for coordinates outside the board
    """
    pass


class Overwrite(Exception):
    """
    Exception for overwriting a move
    """
    pass

