from src.game.algorithm import *
from src.board.board import Board
from src.game.game import Game
from src.ui.ui import UI

if __name__ == '__main__':
    """
    The main function
    """
    algorithm = Algorithm()
    board = Board()
    game = Game(board, algorithm)
    ui = UI(game)
    ui.create_menu()
