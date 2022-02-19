import math
import random


class UI:
    def __init__(self, player_service):
        self._player_service = player_service

    @staticmethod
    def print_menu():
        """
        Print the menu
        :return:
        """
        print("Please select one of the following options:")
        print("\t 1.Display all the players in descending order")
        print("\t 2.Play")
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
                self.ui_order_by_strength()
            elif option == 2:
                self.ui_play()
            elif option == 3:
                print("You exited the application.")
                return 0
            else:
                print('Invalid number. Please select one of the five options!')

    @staticmethod
    def list_players(players):
        print('\n')
        print("There are " + str(len(players)) + " players.\n")
        for i in players:
            print(i)
        print('\n')

    @staticmethod
    def log2(x):
        return math.log10(x) / math.log10(2)

    def is_power_of_two(self, n):
        return math.ceil(self.log2(n)) == math.floor(self.log2(n))

    def ui_play(self):
        while self.ui_play_tournament() == 0:
            self.ui_play_tournament()
        print("The new champion is " + str(self._player_service.players[0].name))
        return 0

    def ui_order_by_strength(self):
        print('\n')
        print("The players sorted by strength are:\n")
        players_sorted = self._player_service.order_by_strength()
        for i in players_sorted:
            print(i)
        print('\n')

    def ui_playing_qualifying_round(self):
        """
        The function plays the qualifying round by checking the number of players and playing corresponding matches
        and eliminating the players which lost
        :return:
        """
        number_of_players = len(self._player_service.players)
        players_sorted = self._player_service.order_by_strength()
        player1 = players_sorted[number_of_players - 1]
        player2 = players_sorted[number_of_players - 2]
        if number_of_players == 5:
            print("One player has to leave.\n")
            print("The match is between:\n1." + str(player1) + "2." + str(
                player2))
            choice = int(input('>'))
            if choice == 1:
                self._player_service.remove_player(player2.player_id)
                self._player_service.update_player(player1.player_id)
                print("The first player won\n")
            elif choice == 2:
                self._player_service.remove_player(player1.player_id)
                self._player_service.update_player(player2.player_id)
                print("The second player won\n")

        elif number_of_players == 7:
            print("Three players have to leave.\n")
            lowest_players = players_sorted[1:]

            for i in range(0, 3):
                player1 = random.choice(lowest_players)
                lowest_players.remove(player1)
                player2 = random.choice(lowest_players)
                lowest_players.remove(player2)
                print("The match is between:\n1." + str(player1) + "2." + str(
                    player2))
                choice = int(input('>'))
                if choice == 1:
                    self._player_service.remove_player(player2.player_id)
                    self._player_service.update_player(player1.player_id)
                    print("The first player won\n")
                elif choice == 2:
                    self._player_service.remove_player(player1.player_id)
                    self._player_service.update_player(player2.player_id)
                    print("The second player won\n")

        elif number_of_players == 13:
            print("Five players have to leave.\n")
            lowest_players = players_sorted[3:]
            for i in range(0, 5):
                player1 = random.choice(lowest_players)
                lowest_players.remove(player1)
                player2 = random.choice(lowest_players)
                lowest_players.remove(player2)
                print("The match is between:\n1." + str(player1) + "2." + str(
                    player2))
                choice = int(input('>'))
                if choice == 1:
                    self._player_service.remove_player(player2.player_id)
                    self._player_service.update_player(player1.player_id)
                    print("The first player won\n")
                elif choice == 2:
                    self._player_service.remove_player(player1.player_id)
                    self._player_service.update_player(player2.player_id)
                    print("The second player won\n")

    def ui_quarter_finals(self):
        """
        The function plays the quarter_finals  playing corresponding matches
        and eliminating the players which lost and goes to semi-finals and final
        :
        :return:
        """
        players_sorted = self._player_service.order_by_strength()
        new_players = []
        for i in players_sorted:
            new_players.append(i)
        print("We are in quarter-finals!\n")
        for i in range(0, 4):
            player1 = random.choice(new_players)
            new_players.remove(player1)
            player2 = random.choice(new_players)
            new_players.remove(player2)
            print("The match is between:\n1." + str(player1) + "2." + str(
                player2))
            choice = int(input('>'))
            if choice == 1:
                self._player_service.remove_player(player2.player_id)
                self._player_service.update_player(player1.player_id)
                print("The first player won\n")
            elif choice == 2:
                self._player_service.remove_player(player1.player_id)
                self._player_service.update_player(player2.player_id)
                print("The second player won\n")

    def ui_semi_finals(self):
        """
        The function plays the semi-finals by playing corresponding matches
        and eliminating the players which lost and goes to the final
        :return:
        """
        players_sorted = self._player_service.order_by_strength()
        new_players = []
        for i in players_sorted:
            new_players.append(i)
        print("We are in semi-finals!\n")
        for i in range(0, 2):
            player1 = random.choice(new_players)
            new_players.remove(player1)
            player2 = random.choice(new_players)
            new_players.remove(player2)
            print("The match is between:\n1." + str(player1) + "2." + str(
                player2))
            choice = int(input('>'))
            if choice == 1:
                self._player_service.remove_player(player2.player_id)
                self._player_service.update_player(player1.player_id)
                print("The first player won\n")
            elif choice == 2:
                self._player_service.remove_player(player1.player_id)
                self._player_service.update_player(player2.player_id)
                print("The second player won\n")

    def ui_final(self):
        """
        The function plays the final between the last two players
        :return:
        """
        players_sorted = self._player_service.order_by_strength()
        new_players = []
        for i in players_sorted:
            new_players.append(i)
        print("We are in the final\n")
        player1 = random.choice(new_players)
        new_players.remove(player1)
        player2 = random.choice(new_players)
        new_players.remove(player2)
        print("The match is between:\n1." + str(player1) + "2." + str(
            player2))
        choice = int(input('>'))
        if choice == 1:
            self._player_service.remove_player(player2.player_id)
            self._player_service.update_player(player1.player_id)
            print("The first player won\n")
        elif choice == 2:
            self._player_service.update_player(player2.player_id)
            print("The second player won\n")
        return 1

    def ui_play_tournament(self):
        """
        The function check if we can have a semi-final or a quarter-final and plays it until we reach the final,
        otherwise, it plays qualifications and goes to quarter-finals, semi-finals and final
        :return:
        """
        number_of_players = len(self._player_service.players)
        players_sorted = self._player_service.order_by_strength()
        new_players = []
        for i in players_sorted:
            new_players.append(i)
        if number_of_players == 4:
            self.ui_semi_finals()
            self.ui_final()
            return 1
        elif number_of_players == 8:
            self.ui_quarter_finals()
            self.ui_semi_finals()
            self.ui_final()
            return 1
        else:
            self.ui_playing_qualifying_round()
        return 0
