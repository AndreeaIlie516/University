from src.exceptions.exception import *

class UI:
    def __init__(self, game):
        self._game = game

    @staticmethod
    def print_menu():
        """
        UI function for printing the menu
        :return:
        """
        print("Welcome to Gomoku!!!")
        print("Please choose one of the following options")
        print("1.Play the game")
        print("2.Exit")

    def win_status(self):
        """
        Function for determining the winning status
        :return:
        """
        return self._game.get_board().win()

    def tie_status(self):
        """
        Function for determining the tie status
        :return:
        """
        return self._game.get_board().tie()

    def print_board(self):
        """
        Ui function for printing the board
        :return:
        """
        print(self._game.get_board())

    def create_menu(self):
        """
        Ui function for creating the menu
        :return:
        """
        while True:
            self.print_menu()
            try:
                option = int(input(">"))
                if option == 1:
                    self._game.get_board().reset()
                    while self.win_status() not in (-5, 5) and self.tie_status() is False:
                        self.print_board()
                        player_move = input('Please insert the coordinates of you move, separated by space: ').split(' ')
                        try:
                            self._game.player_move(player_move)
                        except WrongCoordinates:
                            print("Please insert exactly 2 coordinates!\n")
                            continue
                        except OutsideBoard:
                            print("Please insert coordinates that are inside the board!\n")
                            continue
                        except Overwrite:
                            print("Please insert a position that is not already occupied!\n")
                        except Exception:
                            continue
                        if self.win_status() == 5:
                            self.print_board()
                            print("You won this game. Congratulations!\n")
                            return
                        self._game.computer_move()
                        if self.win_status() == -5:
                            self.print_board()
                            print("Computer won. Good luck next time!\n")
                    if self.tie_status():
                        self.print_board()
                        print("Tie time!\n")
                elif option == 2:
                    print("You exited the game.\n")
                    return
                else:
                    print("Please insert a valid command!\n")
            except ValueError:
                print("Please insert a valid command!\n")
