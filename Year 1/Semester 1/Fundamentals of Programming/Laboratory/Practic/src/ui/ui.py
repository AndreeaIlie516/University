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
        print("Welcome to Achi game!!!")
        print("Please choose one of the following options:")
        print("1.Play the game")
        print("2.Load the game")
        print("3.Exit")

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

    def placement_status(self):
        """
        Function for determining the placement status
        :return:
        """
        return self._game.get_board().placement_ends()

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
        self._game.get_board().reset()
        while True:
            self.print_menu()
            try:
                option = int(input(">"))
                if option == 1:
                    # self.print_board()
                    # print('The placement phase begins:\n')
                    """
                    The placement phase
                    """
                    while self.win_status() not in (
                            -3, 3) and self.tie_status() is False and self.placement_status() is False:
                        self.print_board()
                        ok = 1
                        while ok == 1:
                            print("If you want to save to the file, please write 'save'. Otherwise, write 'no'")
                            save_option = input('>')
                            if save_option.upper() != "SAVE" and save_option.upper() != "NO":
                                print("Please insert a valid option\n")
                            else:
                                if save_option.upper() == "SAVE":
                                    file_name = "board_file.txt"
                                    file = open(file_name, "w")
                                    # board = self._game.get_board()
                                    matrix = self._game.get_matrix()
                                    for i in range(0, 3):
                                        for j in range(0, 3):
                                            file.write(str(matrix[i][j]))
                                            file.write(" ")
                                        file.write("\n")
                                    file.close()
                                ok = 0

                        print('The placement phase: ')
                        ok = 1
                        while ok == 1:
                            player_move = input(
                                'Please insert the coordinates of you move,  separated by space: ').split(
                                ' ')
                            try:
                                self._game.player_move(player_move)
                                ok = 0
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
                            if self.win_status() == 3:
                                self.print_board()
                                print("You won this game. Congratulations!\n")
                                return
                            self._game.computer_move()
                            if self.win_status() == -3:
                                self.print_board()
                                print("Computer won. Good luck next time!\n")
                    if self.tie_status():
                        self.print_board()
                        print("Tie time!\n")

                    if self.placement_status():
                        while self.win_status() not in (-3, 3) and self.tie_status() is False:
                            self.print_board()
                            print('The movement phase: ')

                            player_move_initial = input(
                                'Please insert the coordinates of the pion you want to move,  separated by space: ').split(
                                ' ')
                            player_move_new = input(
                                'Please insert the coordinates of the place you want to move the pion,  separated by space: ').split(
                                ' ')

                            try:
                                self._game.player_move2(player_move_initial, player_move_new)
                            except WrongCoordinates:
                                print("Please insert exactly 4 coordinates!\n")
                                continue
                            except OutsideBoard:
                                print("Please insert coordinates that are inside the board!\n")
                                continue
                            except Overwrite:
                                print("Please insert a position that is not already occupied!\n")
                            except Exception:
                                continue

                            if self.win_status() == 3:
                                self.print_board()
                                print("You won this game. Congratulations!\n")
                                return
                            self._game.computer_move()
                            if self.win_status() == -3:
                                self.print_board()
                                print("Computer won. Good luck next time!\n")
                elif option == 2:
                    print("You selected loading game from a file")
                    matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                    file_name = "board_file.txt"
                    file = open(file_name, "r")
                    i = 0
                    for line in file.readlines():
                        line = line.strip(" \n")
                        stuff = line.split(" ")
                        matrix[i][0] = int(stuff[0])
                        matrix[i][1] = int(stuff[1])
                        matrix[i][2] = int(stuff[2])
                        i += 1
                    file.close()

                    self._game.get_board().reset()
                    self._game.set_board_from_matrix(matrix)
                    # print(matrix)

                elif option == 3:
                    print("You exited the game.\n")
                    return
                else:
                    print("Please insert a valid command!\n")
            except ValueError:
                print("Please insert a valid command!\n")
