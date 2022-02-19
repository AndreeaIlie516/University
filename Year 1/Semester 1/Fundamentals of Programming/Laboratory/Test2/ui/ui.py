import math
import random


class UI:
    def __init__(self, taxi_service):
        self._taxi_service = taxi_service

    @staticmethod
    def print_menu():
        """
        Print the menu
        :return:
        """
        print("Please select one of the following options:")
        print("\t 1.List the taxis")
        print("\t 2.Add a ride")
        print("\t 3.Exit")
        print()

    def create_menu(self):
        """
        Create the menu-driven console user interface
        """
        while True:
            UI.print_menu()
            option = int(input('>'))
            if option == 1:
                self.list_taxis(self._taxi_service.taxis)
            elif option == 2:
                self.ui_add_ride()
            elif option == 3:
                print("You exited the application.")
                return 0
            else:
                print('Invalid number. Please select one of the five options!')

    @staticmethod
    def list_taxis(taxis):
        print('\n')
        print("There are " + str(len(taxis)) + " taxis.\n")
        for i in list(taxis):
            print(i)
        print('\n')

    def ui_add_ride(self):
        print("Please insert the start point coordinates:")
        start_x = int(input('X:'))
        start_y = int(input('Y:'))

        print("Please insert the end point coordinates:")
        end_x = int(input('X:'))
        end_y = int(input('Y:'))
        distance = abs(start_x - end_x) + abs(start_y - end_y)
        if distance <= 5:
            print("Please insert a valid distance!\n")
        else:
            self._taxi_service.add_ride([start_x, start_y], [end_x, end_y])
